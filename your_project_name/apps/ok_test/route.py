import time

import rpyc
from flask import request, jsonify, current_app

from apps import apps_bp
from .module import *
from celery_tasks.sms.tasks import send_sms

@apps_bp.route("/apps_test", methods=['GET','POST'])
def apps_bdocr():
    s2 = app_test_data()
    return 'ok-'+ s2

@apps_bp.route("/celery")
def apps_celery():
    send_sms.delay(1,2,3)
    return "Hello world"

@apps_bp.route("/rpctest")
def apps_rpctest():
    # 参数主要是host, port
    conn = rpyc.connect('localhost', 7010)
    # test是服务端的那个以"exposed_"开头的方法
    start = time.time()
    cResult = conn.root.test(11)
    # conn.close()
    end = time.time()
    print("cost %s" % (end - start))
    print(cResult)
    return cResult

# 测试函数
@apps_bp.route("/py/hello")
def apps_py_index():
    return "/py/hello"

# 测试函数
@apps_bp.route("/hello")
def apps_index():
    return "Hello world"

@apps_bp.route("/json", methods=["GET", "POST"])
def apps_login():
    """登录"""
    name = request.form.get("name")
    password = request.form.get("password")
    # ""  0  [] () {} None 在逻辑判断时都是假
    if not all([name, password]):
        # 表示name或password中有一个为空或者都为空
        return jsonify(code=1, message=u"参数不完整")
    if name == "admin" and password =="python":
        return jsonify(code=0, message=u"OK")
    else:
        return jsonify(code=2, message=u"用户名或密码错误")

@apps_bp.route("/index")
def index():
    #print("hello")
    # logging.error()   # 记录错误信息
    # logging.warn()   # 警告
    # logging.info()   # 信息
    # logging.debug()   # 调试
    current_app.logger.error("error info")
    current_app.logger.warn("warn info")
    current_app.logger.info("info info")
    current_app.logger.debug("debug info")

    # request.cookies.get("csrf_token")
    # session.get
    return "index page"