# coding:utf-8 
import rpyc
import time


# 参数主要是host, port
conn =rpyc.connect('localhost',7010)
# test是服务端的那个以"exposed_"开头的方法
start = time.time()
cResult =conn.root.test(11)
# conn.close()
end = time.time()
print("cost %s"% (end - start))
print(cResult)