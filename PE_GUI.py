import tkinter as tk

from PIL import ImageTk,Image
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk             #ttk为tk的一种简单升级


window=tk.Tk()
window.geometry('900x700')
window.title('for PE_calc')


window.update()

#设置画布的参数，长宽和背景颜色
cav_width=window.winfo_width()
cav_height=window.winfo_height()
#根据窗口的长宽改变画布长宽
canvas1=tk.Canvas(window,height=cav_height-100,width=cav_width)


img=Image.open('2.gif')
photo=ImageTk.PhotoImage(img)
#这里的坐标指的是图片的中心在画布中的位置,这里的参数第一个是宽度

canvas1.create_image(cav_width*0.5,cav_height*0.5,image=photo)
canvas1.pack()

#menubar为一个容器,增加菜单栏功能
menubar=Menu(window)
window.config(menu=menubar)

#创建file菜单栏
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
def do_job():
    pass

filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='open',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='exit',command=window.quit)

def hit_me():
    tk.messagebox.showinfo(title='Hi',message='haha')
btn1=ttk.Button(window,text='hit me',command=hit_me).pack()
window.iconbitmap('car.ico')

window.mainloop()