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

#插入一条数据
def insert(conn,username,password,email):
    sql_insert = '''
    INSERT INTO users(username,password,email) VALUES (?,?,?);
    '''
    conn.execute(sql_insert,(username,password,email))
    print('插入数据成功')


def select(conn,usr,pwd):
    sql = '''
    SELECT
    id,username,email
    FROM
    users
    WHERE
    username=? and password =?
    '''

    cursor = conn.execute(sql,(usr,pwd))
    print('一条数据',list(cursor))

def delete(conn,user_id):
    sql_delete = '''
    DELETE FROM
    users
    WHERE
    id=?
    '''
    conn.execute(sql_delete,(user_id,))

def update(conn,user_id,email):
    sql_update = '''
    UPDATE
    'users'
    SET
    'email'=?
    WHERE
    'id'=?
    '''
    conn.execute(sql_update,(email,user_id))


def main():
    db_path ='web.sqlite'
    conn = sqlite3.connect(db_path)
    print('打开了数据库')
    create(conn)
    # insert(conn,'sql_','123','a@qq.com')
    # delete(conn,1)
    update(conn,3,'119@qq.com')
    select(conn,'asdads','asd')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
