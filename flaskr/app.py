import json
import os
from celery.result import AsyncResult
from flask import Flask, request, jsonify, url_for
from flaskr.tasks import celery_app, import_new_data, import_website
from flask_cors import CORS
from orm.database import rds_instance

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/tasks', methods=['POST'])
def index():
    if request.method == 'POST':
        tc_id = request.form['tc_id']
        filename = request.form['filename']
        header = request.form.get('header') or None
        table = request.form.get("table") or None
        inter = request.form['inter'] if "inter" in request.form else False
        pattern = request.form.get('pattern') or None
        # 加一个判断了，引入文件夹
        files = _get_filenames(filename, inter)

        summary = []
        for file in files:

            result = import_new_data.delay(tc_id, file, table, header, pattern)
            
            rds_instance.hset("QUEUE_TASKS", result.id, json.dumps({"filename": file}))

            summary.append({"task_id": result.id,
                            "filename": file,
                            "location": str(url_for('get_task_state', task_id=result.id))
                            })
        return jsonify(summary), 202


def _get_filenames(path=None, inter=None):
    if not os.path.exists(path):
        return []
    elif os.path.isdir(path):
        files = []
        for file in os.scandir(path):
            if os.path.isfile(file):
                files.append(file.path)
            elif os.path.isdir(file):
                if inter is not None and inter != '0':
                    files.extend(_get_filenames(file.path))
                else:
                    pass
        return files
    else:
        return [path]


@app.route('/tasks/<string:task_id>/state')
def get_task_state(task_id):
    result = AsyncResult(task_id, app=celery_app)
    summary = {
        "state": result.state,
        "result": result.result,
        "id": result.id,
    }
    return jsonify(summary), 200


@app.route('/tasks', methods=['GET'])
def get_task_list():
    keys = rds_instance.hgetall("QUEUE_TASKS")

    results = []
    for key in keys:
        result = AsyncResult(key, app=celery_app)
        data = json.loads(keys[key])
        results.append({
            "state": result.state,
            "filename": data["filename"],
            "result": result.result,
            "id": result.id,
        })
    return jsonify(results), 200

@app.route('/paths', methods=['POST'])
def get_path():
    path = request.form['path']
    if os.path.exists(path):
        if os.path.isdir(path):
            ls = os.listdir(path)
            return jsonify(ls), 200
    return jsonify([]), 200

# 接口爬取过来的数据直接存mongo
@app.route("/website_info", methods=["POST"])
def website_info():
    url = request.form["url"]
    table = request.form["table"]
    cookie = request.form.get("cookie") or None
    key = request.form.get("key") or None
    page_num = request.form.get("page_num") or None
    import_website.delay(url, table, cookie, key, page_num)
    return jsonify([]),200

