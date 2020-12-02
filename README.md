# 数据导入工具

**此项目仅为个人学习使用**

## 背景说明
40G
可以将格式化的文本通过解析成mongodb条目。
由于最开始开发的时候用的mysql，因此有一些残留

## 特点
+ 格式化的txt文件，通过输入header自动解析
+ 全部csv，excel文件，自动解析头，转英文存db
+ sql文件，按行细分的那种
+ 内置部分解析模板，支持通用空格分割txt的导入
+ 断点续传，使用redis进行缓存
+ celery异步处理，让数据导入自动智能化
+ 无头文件会自动用col进行命名
+ 支持文件批量导入

# 支持
xlrd 读取excel
python内置csv模块读取csv
正则读取其他文件

# 使用
> 由于本人python水平有限，而且celery的Worker貌似不支持解析环境变量，因此有部分配置仍无法通过修改环境变量或文件，只能写死在代码里。欢迎大家提pr共建

整个使用`flask`启动，只写了后端api，也欢迎大家适配前端界面。

## 配置文件说明
    根目录下带有 `.docker` 的会在docker运行时自动映射，如果不需要使用`.docker`直接修改不带`.docker`的即可
    为了顺利运行worker，需要`orm/database.py`中修改10-14行redis,33-34行mongo的配置；`reader/abstract_reader.py`中15-16的mongo配置

1. 修改配置文件：.env/.env.docker中的redis和mongo配置，mysql已经没用了。如果不使用docker不需要修改
2. 修改config.ini/config.ini.docker中的redis和mongo配置。

## 运行
在配置完成后
### 不需要docker
```bash
# 第一个终端
pip install -r requirements.txt
flask run
# 第二个终端
celery -A flaskr.tasks.celery_app worker -l Info
```
### 使用docker
首先起两个容器，mysql和redis，放在db网络中
docker-compose.yml中把volumes添加你要解析的目录的映射
```bash
docker network create db
docker run 
docker build -t reader .
docker-compose up -d reader celery
```

## 使用
目前提供了以下接口：
* POST /tasks 添加任务
    
    ```
    参数：
    + tc_id 没卵用
    + filename docker内对应的目录或文件名称(2000w)
    + table 你要存的collection名称
    + inter 是否读目录下的目录(ga) 可选
    + pattern 对于txt文件所使用的正则表达式(jd) 可选
    + header 表头，如果传了则优先使用 可选
    返回创建成功的任务id
    ```
* GET /tasks
    ```
    返回当前任务列表
    ```

+ POST /paths 容器内的路径查找，给前端准备的接口
    ```
    参数
    + path 要寻找的路径名称

    返回数组，内容是目录下的子文件和文件夹

没有前端怎么办？postman啊
## 没了
欢迎pr

欢迎适配前端

里面有个小工具大家可以试着用一下

本项目纯为技术交流，本人不存储也不提供任何违法数据，相关正则匹配规则均为网上流传的数据格式。

## 技术交流
    QQ群：（怎么发图啊）
## 没了
BUE mY a CoFfEE
BTC: 1PXr5iZ145ha7XTeJwDk5S1LVLLRW5seKe

