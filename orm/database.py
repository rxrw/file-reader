
from utils.configs import get_config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import redis

from sqlalchemy.sql.schema import MetaData

redis_config = {
    "host": get_config('REDIS_HOST', 'redis'), 
    "port": get_config('REDIS_PORT', '6379'),
    "pass": get_config('REDIS_PASS', 'pass'),
}

mysql_url = 'mysql+pymysql://'+get_config("MYSQL_USERNAME", "root")+':'+get_config(
    "MYSQL_PASSWORD", "")+'@'+get_config("MYSQL_HOST", "mysql")+'/'+get_config("MYSQL_DBNAME", "se")

if redis_config["pass"]:
    redis_url = "redis://:" + redis_config["pass"] + "@" + redis_config["host"] + ":" + redis_config["port"]

    rds_instance = redis.Redis(host=redis_config["host"],
                              port=redis_config["port"], 
                              password=redis_config["pass"]
                              )
else:
    redis_url = "redis://" + redis_config["host"] + ":" + redis_config["port"]
    rds_instance = redis.Redis(host=redis_config["host"],
                              port=redis_config["port"]
                              )


mongo_url = "mongodb://{username}:{password}@{host}:{port}".format(username=get_config("MONGODB_USERNAME", ""), password=get_config(
    "MONGODB_PASSWORD", ""), host=get_config("MONGODB_HOST", "mongodb"), port=get_config("MONGODB_PORT", "27017"))



engine = create_engine(mysql_url)

metadata = MetaData()

Base = declarative_base()

# Base.prepare(engine, reflect=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()

