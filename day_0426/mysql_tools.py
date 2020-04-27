'''''''''
1、编程小练习，封装一个操作mysql的对象。需要实现的方法
- 连接数据库
- 执行查询sql
- 执行增删改sql
- 断开数据库连接

提示：
使用pymysql模块，模块内的api大家自行百度，不懂的地方可以在小组内讨论，也可以在大群里提问
'''
import pymysql
import traceback
import random


class MysqlDb():
    # 连接数据库
    def __init__(self, host, port, user, passwd, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        try:
            self.condb = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                         passwd=self.passwd, db=self.db, charset=self.charset)
        except Exception as abnormal:
            print("数据库连接错误，错误内容%s " % abnormal)
        # 创建一个游标对象
        self.cursor = self.condb.cursor()

    # 创建表
    def create_table(self, tablename, sql):
        # 获取数据库连接 使用cursor() 方法创建一个游标对象 cursor
        cursor = self.condb.cursor()
        # 使用execute()方法执行sql ，如果表存在则删除
        cursor.execute("drop table if exists %s" % (tablename))
        # 使用预处理语句创建表
        cursor.execute(sql)
        print("表:'%s' 创建成功" % tablename)

    # 增加sql
    def insert_sql(self,sql):
        # 获取数据库连接 使用cursor() 方法创建一个游标对象 cursor
        cursor = self.condb.cursor()
        # 使用execute()方法执行sql ，如果表存在则删除
        # SQL 插入语句

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.condb.commit()
        except Exception as abnormal:
            # 如果发生错误则回滚
            self.condb.rollback()
            print("执行失败 insert语句:'%s'，失败信息为 %s" % (sql, abnormal))
        print("新增数据成功")

    # 修改sql
    def update_sql(self,sql):
        # 获取数据库连接 使用cursor() 方法创建一个游标对象 cursor
        cursor = self.condb.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.condb.commit()
        except Exception as abnormal:
            self.condb.rollback()
            print("更新失败,sql语句:{}".format(sql))
            print("报错内容:{}".format(abnormal))

    # 查询sql
    def querysql(self, sqlquery):
        try:
            self.cursor.execute(sqlquery)  # 影响的行数
        except Exception as abnormal:
            print("SQL有误，错误内容 %s" % abnormal)
        if self.cursor.rowcount == 0:  # 判断 返回的sql数据行数如果为0则代表没有查询结果
            return "没有查询的结果.."
        elif self.cursor.rowcount == 1:  # 判断 返回的sql数据如果只有1条数据 返回该数据以list形式返回
            return list(self.cursor.fetchone())
        else:
            return list(self.cursor.fetchall())  # 如果返回多行情况下,用 fetchall()


    # 删除数据库
    def drop_biao(self):
        # 删除数据库
        sql = "DROP DATABASE {}".format(self.db)
        # 执行创建数据库的sql
        self.cursor.execute(sql)
        print("删除数据库成功")

    # 执行删除数据库表sql
    def delete_table_sql(self):
        print('删除表成功')

    # 析构函数,对象实例化调用之后会执行del函数
    def __del__(self):
        self.cursor.close()  # 关闭游标
        self.condb.close()  # 关闭数据库


if __name__ == '__main__':
    # 实例化
    mysql = MysqlDb(host="127.0.0.1", port=3306, user="root", passwd="xxx", db="leiyanghong", charset="utf8")
    '''
    新建一张leiyanghong的表,定义表结构,里面设置了主键id,必填字段:name,age.当前日期:table_date
    sql 建表需知:
    如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
    AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
    PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
    ENGINE 设置存储引擎，CHARSET 设置编码。
    '''
    mysql.create_table(tablename='tb_leiyanghong', sql="""\
                                                                CREATE TABLE IF NOT EXISTS `tb_leiyanghong`(
                                                                `id` INT UNSIGNED AUTO_INCREMENT,
                                                                `name` VARCHAR(100) NOT NULL,
                                                                `age` VARCHAR(40) NOT NULL,
                                                                PRIMARY KEY ( `id` ))
                                                                ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
    # 在tb_leiyanghong表中 插入一条数据
    mysql.insert_sql(sql = """INSERT INTO tb_leiyanghong
                                          (name,age)
                  VALUES                  ('leiyanghong{}','19');""".format(random.randint(1,100000)))
    # 查询表数据
    sql = mysql.querysql("select * from tb_leiyanghong limit 10")
    print(sql)
    # 修改表数据
    updata_data = mysql.update_sql("update tb_leiyanghong set name='彭敏' where id ='1'")
