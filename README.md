## 简介

这是一个python web的结构建议框架

本项目基于flask，并规定一些规则，方便web的可持续开发

并且加入了celery 和pythonrpc 集成

我们知道flask框架的自由度很高，所以这个项目只是想给大家一些启发

## 注意

这只是一个框架建议

里面的flask ,celery 等开发知识需要自己掌握

## 框架目录

```shell
your_project_name:
│  config.py  #配置你的项目的一些配置
│  gunicorn.py #这个使使用gunicorn部署的脚本
│  requirements.txt #这个使依赖包
│  web.py #这是flask启动文件
│  wsgi.py #这个是wsgi 协议用的，如果在liunx上部署，这个就没有用
├─apps #这个是一个主应用包，你可以看自己在项目里面见多个这个样的包
│  │  __init__.py #这是这个包的加载文件，你需要在这里定义蓝图，并加载路由文件
│  └─ok_test #这就是一个子模块包 ，一个应用里面可以有很多个子应用包
│          module.py #这是具体逻辑的封装函数，类似于MVC 里面的M
│          route.py #这个是定义具体路由路径和主要业务逻辑判断 ，相当 于MVC 里面的C
│          __init__.py
├─celery_tasks #这是celery_server包的路径,如果不知道怎么用的话，需要自行百度
│  │  main.py #主执行函数
│  │  test_task_sms.py #这个是单独运行的 celery 制作参考，可以忽略
│  │  __init__.py
│  └─sms #这个是一个个小的celery_tasks 任务
│          tasks.py #这里面写具体的异步逻辑
│          __init__.py
├─logs #日志文件夹
├─module #这边你可以定义一些所有项目都可以使用到的模块，例如数据库等
│      gmtools.py #常用函数
│      m_singledb.py #数据库连接函数
│      __init__.py
├─rpc_server #这是 rpc_server ，因为我的python 使用的是pypy,所有用pythonrpc提高兼容性
│      client_example.py #这是调用案例
│      server.py #这是运行函数
├─static #静态目录 一般静态目录由nginx 提供
├─templates #模块目录
└─utils #常用变量和flask 函数相关模块 类似于module但又有不同
        commons.py　#flask的一些模块 向re 路由等 钩子等
        response_code.py #常用状态码返回
        __init__.py

```

## 如何使用

```shell
#安装依赖
pip install -r requirements.txt

#运行falsk 
pypy Web.py

#gunicorn 运行 faslk
gunicorn -c gunicorn.py web:app

#运行pythonrpc
cd your_project_name/rpc_server
python server.py

#运行celery
cd your_project_name
celery -A celery_tasks.main worker -l info
```

访问测试

http://127.0.0.1/hello

## 应用说明

应用设计思路

所有的应用都放在类似于apps的文件夹里面

然后里面可以有N个小的模块

每个小模块有自己的route和数据库操作和数据获取代码



如果公共模块，可以放在module里面用，否则就写在自己的模块里面



如果模块有交叉应用，直接按照包引用就行



## celery说明

celery可以将一些耗时操作放在后台执行，从而简化用户前台的等待时间，提升用户体验

例如发送邮箱，发送短信，一堆数据库操作或者记录内容等

具体使用，先看上面的文件夹模型

然后我们的逻辑主要以包的形式写在celery_tasks 里面，然后再main.py 里面定义路由

```python
# 自动搜寻异步任务
celery_app.autodiscover_tasks(["celery_tasks.sms"])
```

这样就可以在项目其他位置调用该异步函数

```python
例如
from celery_tasks.sms.tasks import send_sms

@apps_bp.route("/celery")
def apps_celery():
    send_sms.delay(1,2,3)
    return "Hello world"
```

## pythonrpc使用

这个就类似于一个python_server

直接在里面定义好函数，然后直接调用就行

```python
server
    # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"
    def exposed_test(self, num):
        res = 100
        return res

```

```python
client
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
```

## 最后

有问题欢迎pr,issue