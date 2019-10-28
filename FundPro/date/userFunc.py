# -*- coding:utf-8 -*-
from CreateTable import *
import json
import requests
import time


#查看行情,并将行情数据写入数据库
def k_line():
    num = ("000248", "260108", "005827", "161725", "000311", "163407")
    data = []
    for each in num:
        url = "http://fundgz.1234567.com.cn/js/" + each + ".js"
        res = requests.get (url).content
        cc = json.loads (res[8:-2])
        field = (cc['dwjz'],cc['jzrq'],cc['gsz'],cc['gszzl'],cc['gztime'],cc['fundcode'])
        runSQL(updateQuota,field)  #行情更新入数据库
        data.append (cc)
    # print data
    return data


#打印行情数据，打印前更新数据库
def print_quto(data):
    title=['名称','编码','昨日','今日','幅度']
    print("{0[0]:^30}{0[1]:^30}{0[2]:^10}{0[3]:^20}{0[4]:^10}".format(title))
    for each in data:
        print ("%-30s%-10s%10s%15s%15s" % (each['name']+"--"+each['fundcode'], each['fundcode'],each['dwjz'], each['gsz'], each['gszzl']))
    print


#从数据库查找基金行情，减少行情请求操作
def checkinfo(fundid):
    checkinfo = 'select nowprice,rise from quota where fundid =?'
    dd =runSQL (checkinfo, (fundid,))
    fundgz = dd[0][0]
    fund_range = dd[0][1]
    return fundgz,fund_range

#用户查询操作
#查看总投资金额，分用户
def owner_invest():
    data = runSQL('select owner,sum(amount) from trade where status=0 group by owner ')
    return data

#查询某用户某金购买情况
def own_eachfund(owner):
    sql='SELECT owner,fundid,sum(amount),round(sum(quantity),2),round(sum(amount)/sum(quantity),5) as avr_price,min(price) ' \
        'FROM trade WHERE owner =? and status=0 ' \
        'GROUP BY fundid'
    data =  runSQL(sql,(owner,))
    return data


def check_fund_average(owner,fundid):
    # owner, fundid,
    # sum (amount), 资金总额
    # min (price), 最低单价
    # sum (Quantity), 总数量
    # round (sum (amount) / sum (Quantity), 5) 成本价，5位小数
    data = runSQL ('select owner,fundid,sum(amount),sum(Quantity),min(price),round(sum(amount)/sum(Quantity),5) from Trade where Owner =? and FundID=? and status=0', (owner, fundid))
    return data

#已达到20%收益可卖出的份额
def tosell(b):
    str_list = []
    k_line()
    sql_gz = 'select fundid,nowprice from quota;'
    info = runSQL(sql_gz)
    for each in info:
        fundid,fundgz =each
        fundgz = float(fundgz)
        sql = 'select owner,fundid,round(sum(quantity),2) from trade where price <(1-?)*? and fundid =? and status=0 group by owner'
        data = runSQL(sql,(b,fundgz,fundid))
        str_list.append(data)
    return str_list

# #建议购买金额：待优化，摊平成本
# def support_buy00(own):
#     fund_info=[]
#     data = own_eachfund (own)
#     # print '用户 基金 投资金额 持有份额 成本价 最低价 当前估值 涨跌幅 建议购买'
#     for each in data:
#         owner, fundid, amount, quantity, av_price, min_price = each
#         fundgz,fund_range = checkinfo(fundid)  #从数据库查找行情数据
#         sug_money = tactics(fundgz,min_price,av_price,fund_range)
#         sug_sell = quantity * float (fundgz) * (1 - fees[fundid])
#         sug_sell = round (sug_sell, 2)
#         profit = round (sug_sell - amount, 2)
#         rate = round (profit / amount, 4)
#         rate = str(rate*100)+'%'
#         # print '用户 基金  最低价 投资金额 持有份额 成本价 基金估值   差额  当日涨跌幅 建议购买 卖出到账 收益 收益率'
#         range = round(float(fundgz)-av_price,5)
#         info = (
#         owner, fundid, min_price,amount, quantity, av_price, fundgz, range,fund_range, sug_money, sug_sell, profit, rate)
#         fund_info.append(info)
#     return fund_info


def support_buy(own):
    fund_info=[]
    data = own_eachfund (own)
    # print '用户 基金 投资金额 持有份额 成本价 最低价 当前估值 涨跌幅 建议购买'
    for each in data:
        owner, fundid, amount, quantity, av_price, min_price = each
        fundgz,fund_range = checkinfo(fundid)  #从数据库查找行情数据
        sug_money = tactics(fundgz,min_price,av_price,fund_range)

        sug_sell = quantity * float (fundgz) * (1 - fees[fundid])
        sug_sell = round (sug_sell, 2)
        profit = round (sug_sell - amount, 2)
        rate = round (profit / amount, 4)
        rate = str(rate*100)+'%'
        # print '用户 基金  最低价 投资金额 持有份额 成本价 基金估值   差额  当日涨跌幅 建议购买 卖出到账 收益 收益率'
        range = round(float(fundgz)-av_price,5)
        info = (
        owner, fundid, min_price,amount, quantity, av_price, fundgz, range,fund_range, sug_money, sug_sell, profit, rate)
        fund_info.append(info)
    return fund_info


def all_support_buy():
    # print '用户 基金 投资金额 持有份额 成本价 最低价 当前估值 涨跌幅 建议购买'
    own = ['770', '644', '216']
    for each in own:
        info = support_buy (each)
        for id in info:
            print id
        print
        time.sleep(2)

def fun_menu():
    i = 1
    while (i):
        print("1: 查看实时行情    2：每日建议购买    3：当前持仓情况\n"
            "4.查看投入总额     5: 插入单条数据    6: 插入多条数据\n"
            "7.止盈点份额     0.退出")
        a = raw_input ("请输入：\n")
        if a == '1':
            print_quto (k_line ())
            print
        if a == '2':
            print '用户名称 基金序号  最低价 投资金额 持有份额  成本价   当前估值    差额  当日涨跌幅  建议购买  卖出   收益   收益率\n'
            all_support_buy ()
            print
        if a == '3':
            b=1
            while(b!='0'):
                b = raw_input ("请输入用户，644，216，770,输入 0 退出\n")
                data = own_eachfund (b)
                for each in data:
                    print each
                print
        if a == '4':
            print owner_invest ()
            print
        if a =='5':
            #插入单条数据
            inserttx()
        if a =='6':
            #插入多条数据
            inserttx_bat(input_duo())
            print "执行成功"
            return
        if a =='7':
            b = raw_input ("请输入止盈利点，如：10%输入0.1\n")
            print tosell(b)
            print
        if a == '0' or a == 'q':
            i = 0
            return

def tactics(fundgz,min_price,av_price,fund_range):
    fundgz = float(fundgz)
    min_price = float(min_price)
    av_price = float(av_price)
    fund_range = float(fund_range)
    if fundgz > av_price:
        return 0
    if min_price<fundgz<av_price :
        if  fund_range>0 or av_price - fundgz < 0.01:
            return 0
        if 0.01 <= av_price-fundgz <0.05:
            return 100
        if 0.05<=av_price-fundgz <0.1:
            return 200
        if 0.1<=av_price-fundgz <0.15:
            return 300
        if av_price-fundgz >=0.15:
            return 400

    if fundgz < min_price :
        if fund_range>0:
            return 500
        if 0<=min_price-fundgz <0.02:
            return 1000
        if 0.02<=min_price-fundgz <0.05:
            return 1500
        if 0.05<=min_price-fundgz <0.1:
            return 2000
        if 0.1<=min_price-fundgz <0.15:
            return 2500
        if 0.15<=min_price-fundgz <0.2:
            return 3000
        if min_price-fundgz >=0.2:
            return 3500

if __name__ == '__main__':
    fun_menu ()

