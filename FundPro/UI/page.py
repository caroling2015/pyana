# -*- coding:utf-8 -*-

from Tkinter import *
import ttk


win = Tk()
win.title("CheckButton多选框+矩形框")
win.geometry("800x600+600+100")

def update():
    if hobby1.get()==True:
        print('hehe')
    if hobby2.get()==True:
        print ('23')


hobby1=BooleanVar()
check1=Checkbutton(win,text='兴全指数(163407)',variable=hobby1,command=update)
check1.pack()


hobby2=BooleanVar()
check2=Checkbutton(win,text='景顺指数(000311)',variable=hobby2,command=update)
check2.pack()

hobby3=BooleanVar()
check3=Checkbutton(win,text='招商白酒(161725)',variable=hobby3,command=update)
check3.pack()


hobby4=BooleanVar()
check4=Checkbutton(win,text='易方蓝筹(005827)',variable=hobby4,command=update)
check4.pack()

hobby5=BooleanVar()
check5=Checkbutton(win,text='景顺长城(260108)',variable=hobby5,command=update)
check5.pack()

hobby6=BooleanVar()
check6=Checkbutton(win,text='汇添中证(000248)',variable=hobby6,command=update)
check6.pack()



#
# frm_l=Frame(frm)
# Label(frm_l,text="左上",bg="pink").pack(side=TOP)#在frm上又创建Label
# Label(frm_l,text="左下",bg="blue").pack(side=TOP)
# frm_l.pack(side=LEFT)
# #Right
# frm_r=Frame(frm)
# Label(frm_r,text="右上",bg="yellow").pack(side=TOP)
# Label(frm_r,text="右下",bg="black").pack(side=TOP)
# frm_r.pack(side=RIGHT)
# #基础窗体左侧
# frm_l1=Frame(win)
# Label(frm_l1,text="左上",bg="pink").pack(side=TOP)#在frm上又创建Label
# Label(frm_l1,text="左下",bg="blue").pack(side=TOP)
# frm_l1.pack(side=LEFT)
# #基础窗体左侧
# frm_r1=Frame(win)
# Label(frm_r1,text="右上",bg="yellow").pack(side=TOP)
# Label(frm_r1,text="右下",bg="black").pack(side=TOP)
# frm_r1.pack(side=RIGHT)

#
# def updata():
#     message=""
#     if hobby1.get()==True:#如果check1被选择，那么hobby1被返回True
#         message+="money\n"
#     if hobby2.get()==True:
#         message+="power\n"
#     if hobby3.get()==True:
#         message+="fine foods"
#     text.delete(0.0,END)#清空文本中所有内容，从0开始，到最后
#     text.insert(INSERT,message)#在文本框中显示文本
# hobby1=BooleanVar()#绑定选择时的动作
# check1=Checkbutton(win,text="money",
#                            variable=hobby1,command=updata)
# check1.grid(row,sticky)
# hobby2=BooleanVar()#
# check2=Checkbutton(win,text="power",variable=hobby2
#                            ,command=updata)
# check2.grid(row,sticky)
# hobby3=BooleanVar()
# check3=Checkbutton(win,text="fine foods",variable=hobby3,
#                            command=updata)
# check3.grid(row,sticky)
#
#
# text=Text(win,width=50,height=5)#显示文本框
# text.grid(row,sticky)
win.mainloop()