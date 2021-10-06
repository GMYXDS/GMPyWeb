#coding=utf-8
import sys
import os

# 加入环境变量
flaskPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 不限文件位置 添加环境变量

if flaskPath not in sys.path:
    sys.path.insert(0, flaskPath)

from web import app

application = app