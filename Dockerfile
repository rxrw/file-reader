FROM python:3.9-alpine

WORKDIR /usr/src/app

ENV FLASK_ENV production
ENV SECRET_KEY akflkubhwkvjsuhi729uiybkscjn
ENV REDIS_HOST redis
ENV REDIS_HOST 6379
ENV REDIS_PASS password
ENV UPLOAD_FOLDER /tmp

ENV MONGODB_HOST=127.0.0.1
ENV MONGODB_PORT=27017
ENV MONGODB_USERNAME=test
ENV MONGODB_PASSWORD=test
ENV MONGODB_DBNAME=se
ENV MONGODB_DBNAME_WEB=website

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add gcc libffi-dev musl-dev linux-headers libressl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
COPY . .
CMD ["sh","run.sh"]

EXPOSE 8000