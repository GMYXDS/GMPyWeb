import  os
from  gevent import monkey
monkey.patch_all()
import multiprocessing
debug = False
bind = "0.0.0.0:7000"
pidfile = "gunicorn.pid"
loglevel='warning'     # debug error warning error critical
accesslog="logs/gunicorn.log" #| 文件夹要存在
errorlog='logs/gunicorn.err.log' #设置问题记录日志
workers = multiprocessing.cpu_count()*2 + 1
worker_class = "gevent"
#daemon=True           # 是否后台运行  交给supervisor
#reload=True            # 当代码有修改时，自动重启workers。适用于开发环境。