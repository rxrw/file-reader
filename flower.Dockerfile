FROM reader:latest

WORKDIR /usr/src/app

RUN pip install celery==4.4.7 flower -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 5555

CMD ["celery", "flower", "-A", "flaskr.tasks.celery_app", "worker", "--address=0.0.0.0"]
