# coding:utf-8

from flask import Blueprint

apps_bp = Blueprint("apps_bp", __name__)
# apps_bp = Blueprint("apps_bp", __name__, template_folder="templates")

#确保视图执行了一遍，不然没法调用
from .ok_test import route