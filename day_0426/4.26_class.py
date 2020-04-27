'''1、编程小练习，封装一个操作mysql的对象。需要实现的方法
- 连接数据库- 执行查询sql- 执行增删改sql- 断开数据库连接'''
import pymysql
class MysqlConnect:
    #连接数据库
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='jmeter', charset='utf8')
        self.cursor=self.db.cursor()

    #执行查询sql,可指定表名和查询条件
    def select(self,tab_name,condition):
        try:
            sql = "select * from %s where %s "%(tab_name,condition)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as error:
            print("SQL查询执行错误，原因：%s" % error)

    #执行增加命令
    def add(self,table_name,values):
        try:
            sql = "insert into %s values (%s)"%(table_name,values)
            self.cursor.execute(sql)
            self.db.commit()
            print('新增数据成功！')
        except Exception as error:
            print("数据新增错误，原因：%s" % error)

    #执行改命令
    def update(self,table_name,key,values,condition):
        try:
            sql = "UPDATE %s set %s=%s where %s"%(table_name,key,values,condition)
            self.cursor.execute(sql)
            self.db.commit()
            print('数据更改成功！')
        except Exception as error:
            print("数据更新错误，原因：%s" % error)

    #执行删除命令
    def delete(self,table_name,condition):
        try:
            sql = "delete from %s where %s"%(table_name,condition)
            self.cursor.execute(sql)
            self.db.commit()
            print('数据删除成功!')
        except Exception as error:
            print("数据删除错误，原因：%s" % error)
     #关闭数据库连接
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()
        print('数据库已关闭！')

my_select=MysqlConnect()
#表名：user_list  字段：id(int)自增长 name(varchar) age(int)
table_name='user_list'
add1="NULL,'王五',15"
my_select.add(table_name,add1)#增
condition='id=1'
my_select.update(table_name,'age',29,condition)#改
my_select.delete(table_name,'id = 12')
print(my_select.select(table_name,'age=29'))#查