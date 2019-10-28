# -*- coding:UTF-8 -*-
import sqlite3,sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

# 执行文件时获取的输入
#python *.py 'SQL语句'
query ='SELECT * FROM food'
# query ='SELECT * FROM food WHERE %s' %sys.argv[1]

curs.execute(query)
#curs.description,获取列字段
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    print row
    # for pair in zip(names,row):
    #     print '%s: %s' % pair
    # print