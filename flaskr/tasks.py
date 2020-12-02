
from http import cookiejar
from flask.json import jsonify
import pymongo
import requests
from utils.configs import get_config
from reader.reader_manager import ReaderManager
from celery import Celery
from orm.database import mongo_url, redis_url

celery_app = Celery(
    'celery_app',
    backend=redis_url,
    broker=redis_url,
)

# 创建导入数据任务，接参数{"file":"本地file路径","config":"本地config路径"}


@celery_app.task()
def import_new_data(tc_id, file: str, tablename, header=None, pattern=None):
    print(f'开始执行{file}的导入任务，任务id: {tc_id}')
    # 调用方法了
    manager = ReaderManager(file, tablename, header, pattern)
    instance = manager.check()

    mongo_conn = pymongo.MongoClient(mongo_url)
    mongo_engine = mongo_conn[get_config("MONGODB_DBNAME", "se")]

    table = manager.get_tablename()
    print("{filename}的表名为{table}".format(filename=file, table=table))
    # 存db
    for res in instance.run():
        if res is None:
            continue
        try:
            mongo_engine[table].insert(res)
        except BaseException as e:
            print("err,{}".format(e))
            pass
    print(f'{tc_id} is completed!')
    return {"result": 'pass',
            "testCaseId": tc_id
            }


@celery_app.task()
def import_website(url, table, cookie, key=None, page_num=None):
    next_num = None
    if page_num is not None:
        url = "{}{}".format(url, page_num)
        next_num = int(page_num) + 1
    print("导入网站数据。。。{}".format(url))
    headers = {
        "Content-Type": "application/json",
        "Charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
    }
    if cookie is not None:
        response = requests.get(url, cookies=cookie, headers=headers)
    else:
        response = requests.get(url, headers=headers)
    if response.status_code > 399:
        return
    content = response.json()
    if content is None:
        return
    mongo_conn = pymongo.MongoClient(mongo_url)
    mongo_engine = mongo_conn[get_config("MONGODB_DBNAME_WEB", "website")]
    if type(content) is dict:
        content = content[key] if key in content else {}
        mongo_engine[table].insert(content)
    elif type(content) is list:
        print("Content is not a list")
        mongo_engine[table].insert_many(content)

    return import_website(url, table, cookie, key, next_num)
