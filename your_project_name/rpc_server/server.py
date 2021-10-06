# coding:utf-8

from rpyc import Service
from rpyc.utils.server import ThreadedServer

# 和celery 一样，要python3 的服务先写好
# rpc 有两种模式，这种在服务的跑起来，提供接口，效率最高
# 注意这个要单独用

class TestService(Service):
    # 对于服务端来说， 只有以"exposed_"打头的方法才能被客户端调用，所以要提供给客户端的方法都得加"exposed_"
    def exposed_test(self, num):
        res = 100
        return res


sr = ThreadedServer(TestService, port=7010, auto_register=False)
sr.start()
