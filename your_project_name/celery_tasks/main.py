# coding:utf-8


from celery import Celery
from config import Celery_config


# 定义celery对象
celery_app = Celery("ec_web")

# 引入配置信息
celery_app.config_from_object(Celery_config)

# 自动搜寻异步任务
celery_app.autodiscover_tasks(["celery_tasks.sms"])

# celery开启的命令
# cd your_project_name
# celery -A celery_tasks.main worker -l info