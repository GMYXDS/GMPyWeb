import pymysql
import redis
from config import Config

class SingleDB(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if SingleDB.init_flag:
            return
        print("初始化数据库单例")
        SingleDB.init_flag = True
        SingleDB.msyqlconn = pymysql.connect(host=Config.MYSQL_HOST, user=Config.MYSQL_USER, password=Config.MYSQL_PASSWORD, port=Config.MYSQL_PORT,cursorclass=pymysql.cursors.DictCursor, charset="utf8")
        SingleDB.redisconn = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0, password=Config.REDIS_PASSWORD,decode_responses=True)

    def getmysql(self):
        return SingleDB.msyqlconn

    def getredis(self):
        return SingleDB.redisconn


if __name__ == '__main__':

    # 创建多个对象
    mysql1conn = SingleDB()
    print(mysql1conn)
    mysql2conn = SingleDB()
    print(mysql2conn)

    conn = SingleDB().getmysql()
    conn.select_db('mysql')
    cursor = conn.cursor()
    cursor.execute("select * from user")
    print(cursor.fetchone())

    r = SingleDB().getredis()
    print(r)

    r.set('gm','1234')
    print(r.get('gm'))
    print(r.get('gm'))
    print(r.get('gm'))