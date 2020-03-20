# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import mysql.connector

# pip install mysql-connector-python

print('连接数据库'.center(100, '-'))
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456"  # 数据库密码
)
print(mydb)

# 使用 cursor() 方法创建一个游标对象 mycursor
mycursor = mydb.cursor()
# 创建时加上IF NOT EXISTS以便二次运行
mycursor.execute("CREATE DATABASE IF NOT EXISTS runoob_db")

print()
# 列出所有数据库
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# 切换到runoob_db数据库
mycursor.execute("USE runoob_db")

# 查询库中是否已有此表
mycursor.execute("SELECT count(*) FROM information_schema.TABLES WHERE table_name ='sites'")
print(mycursor.fetchall()[0][0])

print('创建表'.center(100, '-'))
mycursor.execute("CREATE TABLE IF NOT EXISTS sites (name VARCHAR(255), url VARCHAR(255))")

# 列出所有表
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


print('设置主键'.center(100, '-'))
# 查询表中是否已有字段
mycursor.execute("select count(*) from information_schema.columns where table_name = 'sites' and column_name = 'id'")
if mycursor.fetchall()[0][0] == 0:    # mycursor.fetchall() 返回包含一个元组的列表
    # 创建表时设置一个主键（PRIMARY KEY），可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 语句来创建一个主键，主键起始值为 1，逐步递增。
    # 如果表已经创建，需要使用 ALTER TABLE 来给表添加主键
    mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY ")
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")


print('插入数据'.center(100, '-'))

# 单行插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

# 批量插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

# 在数据记录插入后，获取该记录的 ID
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)
mydb.commit()
print("1 条记录已插入, ID:", mycursor.lastrowid)


print('查询数据'.center(100, '-'))

print("fetchall():")
# fetchall() 获取所有记录
mycursor.execute("SELECT id, name, url FROM sites")
# mycursor.execute("SELECT name, url FROM sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\nfetchone():")
# fetchone() 获取一条记录
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchone()
print(myresult)
myresult = mycursor.fetchone()
print(myresult)
mycursor.fetchall()     # 只需部分结果时，使用fetchall()清空缓冲区，否则报错
# mysql.connector.errors.InternalError: Unread result found

# fetchone() 返回的是 tuple
# fetchall() 返回的是 list，里面的每一个元素都是一个tuple

print("\nWhere:")
# 读取指定条件的数据
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
# print(myresult)
for x in myresult:
    print(x)

print("\n%:")
# 使用通配符 %
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n%s:")
# 防止数据库查询发生 SQL 注入的攻击，可以使用 %s 占位符来转义查询的条件
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\nASC:")
# 查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
sql = "SELECT * FROM sites ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\nDESC:")
sql = "SELECT * FROM sites ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\nLIMIT:")
# 设置查询的数据量，可以通过 "LIMIT" 语句来指定
mycursor.execute("SELECT * FROM sites LIMIT 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("OFFSET:")
# 指定起始位置，使用的关键字是 OFFSET
mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


print('删除数据'.center(100, '-'))
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")
# 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件
sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow",)
mycursor.execute(sql, na)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")


print('更新数据'.center(100, '-'))
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")
# 注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")


print('删除表'.center(100, '-'))
# 删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
mycursor.execute(sql)
