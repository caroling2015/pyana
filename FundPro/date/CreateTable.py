#-*- coding:UTF-8 -*-
import sqlite3
import time
import sys

#手续费全局变量
fees = {
    "000248":0.001,
    "260108":0.0015,
    "005827":0.0015,
    "161725":0.001,
    "000311":0.0012,
    "163407":0.0012
}

createTrade ='''
    CREATE TABLE 'Trade'(
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'Time' INTEGER,
    'Owner' TEXT,
    'FundID' CHAR(10),
    'Type' CHAR(5),
    'Amount' TEXT,
    'Price' TEXT,
    'Quantity' TEXT, 
    'Fee' TEXT,
    'Discount' TEXT,
    'Status'  CHAR(5),
    'FundType'  CHAR(5)
    )
    '''

insertTrade = '''
INSERT INTO 'Trade' 
("Time","Owner","FundID","Type","Amount","Price","Quantity","Fee","Discount","Status","FundType") 
VALUES (?,?,?,?,?,?,?,?,?,?,?)
'''

createFund = '''
CREATE TABLE 'FundInfo'(
    'FundID' NOT NULL PRIMARY KEY,
    'FundName' CHAR(100),
    'Rate' TEXT
)
'''

insertFund = '''
INSERT INTO 'FundInfo' VALUES (?,?,?)
'''

createValue = '''
CREATE TABLE 'Value'(
    'Date' TEXT,
    'Owner' TEXT,
    'FundID' CHAR(10),
    'Amount' TEXT,
    'Quantity' TEXT,
    'Rate' TEXT,
    'Value' TEXT,
    'minValue' TEXT,
)
'''

createQuota ='''
CREATE TABLE IF NOT EXISTS 'quota'(
    'FundID' CHAR(10)  PRIMARY KEY,
    'FundName' TEXT,
    'LastPrice' TEXT,
    'LastDay' TEXT,
    'NowPrice' TEXT,
    'Rise' TEXT,
    'UpdateTime' TEXT
)
'''
insertQuota = '''
INSERT INTO 'Quota' VALUES (?,?,?,?,?,?,?)
'''

updateQuota = '''
UPDATE Quota SET lastprice=?,lastday=?,nowprice=?,rise=?,updatetime=? WHERE fundid=?
'''


def runSQL(sql,vals=None):
    conn = sqlite3.connect('Fund.db')
    curs = conn.cursor()
    if vals == None:
        curs.execute (sql)
    else:
        curs.execute(sql,vals)
     # 打印SQL执行结果
    values = curs.fetchall ()
    conn.commit ()
    conn.close()
    return values
#结果为包含元组的列表

def insert_bat(sql,filename):
    conn = sqlite3.connect ('Fund.db')
    curs = conn.cursor ()
    conn.text_factory = lambda x: unicode (x, "gbk", "ignore")
    for line in open(filename):
        if line.endswith('\n') or line.endswith('\r'):
            line = line[:-2]
            # print line
        fields = line.split(',')
        curs.execute(sql,fields)
    conn.commit ()
    conn.close ()

def inserttx():
    inserttx = '''
    INSERT INTO 'Trade' 
    ("Time","Owner","FundID","Type","Amount","Price","Quantity","Fee","Discount","Status","FundType") 
    VALUES (?,?,?,1,?,?,?,?,0.1,0,1)
    '''
    conn = sqlite3.connect ('Fund.db')
    curs = conn.cursor ()
    conn.text_factory = lambda x: unicode (x, "gbk", "ignore")
    i = 1
    while (i):
        info = raw_input ("请输入购买日期，用户，购买金额，单价，如2019-08-09,644,000248,1000,0.123 用逗号隔开,0退出\n")
        if info == '0':
            i = 0
        else:
            fields = info.split (',')
            rate = float (fees[fields[2]])
            fee = float (fields[-2]) * rate
            quantity = round ((float (fields[-2]) - fee) / float (fields[-1]), 2)
            fields.append (str (quantity))
            fields.append (str (fee))
            curs.execute(inserttx,fields)
    conn.commit ()
    conn.close ()


def input_duo():
    strList = []
    print ("请输入多条数据,如2019-08-09,644,000248,1000,0.123,command+d 结束输入\n")
    for line in sys.stdin:
        if line.endswith ('\n') or line.endswith ('\r'):
            line = line[:-1]
        tempStr = line.split (',')
        strList.append (tempStr)
    return strList

def inserttx_bat(list):

    inserttx = '''
    INSERT INTO 'Trade' 
    ("Time","Owner","FundID","Type","Amount","Price","Quantity","Fee","Discount","Status","FundType") 
    VALUES (?,?,?,1,?,?,?,?,0.1,0,1)
    '''
    conn = sqlite3.connect ('Fund.db')
    curs = conn.cursor ()
    conn.text_factory = lambda x: unicode (x, "gbk", "ignore")
    for fields in list:
            # fields = each.split (',')
            rate = float (fees[fields[2]])
            fee = float (fields[-2]) * rate
            quantity = round ((float (fields[-2]) - fee) / float (fields[-1]), 2)
            fields.append (str (quantity))
            fields.append (str (fee))
            curs.execute(inserttx,fields)
    conn.commit ()
    conn.close ()

def checkAmount(owner):
    # 查看投入金额
    sumAmount = 'select ' \
                'Owner,FundID,sum(amount),sum(quantity),round(sum(amount)/sum(quantity),8) as value,min(price) ' \
                'from Trade ' \
                'where Owner =?' \
                'group by FundID'
    date = runSQL (sumAmount, (owner,))
    return date
#
# if __name__ == '__main__':
# 手动插入购买记录，可多次插入
#     inserttx ()


    # 创建信息表结构并插入数据
    # runSQL(createFund)
    # insert_bat(insertFund,'fund.csv')

    # 创建交易信息并插入数据
    # runSQL(createTrade)
    # insert_bat(insertTrade,'trade01.csv')
     # 自增长键如何插入数据,insert语句填写列名，并与插入数据一一对应

    #创建行情表
    # runSQL(createQuota)
    #插入行情表
    # insert_bat(insertQuota,'trade01.csv')

    #查询语句
    # data =  runSQL('select * from Trade where Owner =? and FundID=?',("644","161725"))
    # print data
    # print checkAmount('644')

    # print(insert())