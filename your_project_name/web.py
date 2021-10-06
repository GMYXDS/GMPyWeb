# -*- coding: utf-8 -*-
import logging
import re
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

from flask import Flask, request, abort, render_template, jsonify
from flask_session import Session
from flask_wtf import CSRFProtect
from utils.commons import ReConverter

from config import ProductionConfig

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
# file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
file_log_handler = TimedRotatingFileHandler(filename=ProductionConfig.flask_log_filename, when='MIDNIGHT', interval=1)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 设置生成日志文件名的格式，以年-月-日来命名
# suffix设置，会生成文件名为log.2020-02-25.log
file_log_handler.suffix = "%Y-%m-%d.log"
# extMatch是编译好正则表达式，用于匹配日志文件名后缀
# 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
file_log_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


# flask 初始化配置
app = Flask(__name__,static_url_path=ProductionConfig.flask_static_url_path,  # 访问静态资源的url前缀, 默认值是static
            static_folder=ProductionConfig.flask_static_folder,  # 静态文件的目录，默认就是static
            template_folder=ProductionConfig.flask_template_folder,  # 模板文件的目录，默认是templates
            )

# 利用flask-session，将session数据保存到redis中
Session(app)

# 为flask补充csrf防护
# CSRFProtect(app)

# 为flask添加自定义的转换器
app.url_map.converters["re"] = ReConverter

from config import Config as Configs
app.config.from_object(Configs)

# 引入其他模块
import apps
# app.register_blueprint(apps.apps_bp, url_prefix="/py")
app.register_blueprint(apps.apps_bp)

if __name__ == '__main__':
    print(app.url_map)
    # app.run(host="127.0.0.1", port=7000)
    app.run(host=ProductionConfig.flask_run_host, port=ProductionConfig.flask_run_port)

