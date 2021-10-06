# coding:utf-8

from celery_tasks.main import celery_app
# from ihome.libs.yuntongxun.sms import CCP
import time

@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    # ccp = CCP()
    # ccp.send_template_sms(to, datas, temp_id)
    time.sleep(3)
    print("异步任务成功了")