# -*- coding:utf-8 -*-


# from userFunc import k_line
# import Tkinter as tk  # 使用Tkinter前需要先导入
# window = tk.Tk ()
# window.title ('My Window')
# window.geometry ('500x300')  # 这里的乘是小x
# var = tk.StringVar ()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# l = tk.Label (window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=300, height=2)
# l.pack ()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set(k_line())
#         # var.set ('you hit me')
#     else:
#         on_hit = False
#         var.set ('')
#
# b = tk.Button (window, text='刷新行情', font=('Arial', 12), width=10, height=1, command=hit_me)
# b.pack ()
# window.mainloop()
