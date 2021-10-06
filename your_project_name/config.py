# coding:utf-8
import redis

class Celery_config(object):
    # celery
    REDIS_PASSWORD = r"root"
    BROKER_URL = f"redis://:{REDIS_PASSWORD}@127.0.0.1:6379/1"
    CELERY_RESULT_BACKEND = f"redis://:{REDIS_PASSWORD}@127.0.0.1:6379/2"

class Config(object):
    """配置信息"""
    SECRET_KEY = "sXHSdfOI*Y9dfffs9c23shd9"

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "root"

    # mysql
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT,password=REDIS_PASSWORD)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒

    flask_static_folder="static"
    flask_static_url_path="/static"
    flask_template_folder="templates"
    flask_log_filename="logs/logging.log"

    flask_run_host="0.0.0.0"
    flask_run_port=7000

class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}