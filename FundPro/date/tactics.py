# -*- coding:utf-8 -*-
#打印表格功能实现

from Tkinter import *
import ttk
from userFunc import k_line

def fun():
    root = Tk ()
    lbred = Label (root, text="红色沟槽状边缘", fg="red", font=('微软雅黑', 15), width=20, height=2, relief=GROOVE)
    lbred.pack ()
    lbgreen = Label (root, text="绿色凸起的", fg="green", font=('微软雅黑', 15), width=20, height=2, relief=RAISED)
    lbgreen.pack ()
    lbblue = Label (root, text="蓝色脊状边缘", fg="blue", font=('微软雅黑', 15), width=20, height=2, relief=RIDGE)
    lbblue.pack ()
    lbyellow = Label (root, text="黄色凹陷的", fg="yellow", font=('微软雅黑', 15), width=20, height=2, relief=SUNKEN)
    lbyellow.pack ()
    lbpink = Label (root, text="粉红色平的", fg="pink", font=('微软雅黑', 15), width=20, height=2, relief=FLAT)
    lbpink.pack ()
    mainloop()


def ui_k_line(tree):
    columns = ('编码','昨日','今日','幅度')
    #定义列
    tree["columns"]=columns
    #设置列属性，列不显示
    for each in columns:
        tree.column(each,width=100)
        tree.heading(each,text=each)
    data = k_line()
    for each in data:
        tree.insert("",0,text=each['name'],values=(each['fundcode'],each['dwjz'], each['gsz'], each['gszzl']))


if __name__=='__main__':
    # win = Tkinter.Tk()
    # win.title("表格数据")
    # win.geometry("800x600+600+50")
    # tree = ttk.Treeview (win)
    # ui_k_line(tree)
    # #表格
    # tree.pack()
    # win.mainloop()
    fun()