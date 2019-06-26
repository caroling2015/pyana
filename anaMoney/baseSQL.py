#-*- coding:UTF-8  -*-
import sqlite3

def create(conn):
    sql_create ='''
    CREATE TABLE 'users'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'username' TEXT NOT NULL UNIQUE,
    'password' TEXT NOT NULL,
    'email' TEXT
    )
    '''
    conn.execute(sql_create)
    print('创建成功')



print('abc')


 # if '__name__'=='__main__':
