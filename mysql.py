#-*- coding: utf-8 -*-

import pymysql

db = pymysql.connect("localhost", "root", "123456")
cursor = db.cursor()
cursor.execute("use aaa")
#cursor.execute("insert into user(name) values('aaa'), ('bbb'), ('ccc')")
cursor.execute("update user set name = 'aa1' where id = 1")
#cursor.execute("delete from user where id = 1")
cursor.execute("select * from user")

print(cursor.fetchall())