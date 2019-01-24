import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
window=tk.Tk()
window.geometry('1200x880')
window.title('for PE_calc')

#设置画布的参数，长宽和背景颜色
canvas1=tk.Canvas(window,height=1080,width=1920)
# img_file=tk.PhotoImage(file='2.gif')
img=Image.open('2.gif')
photo=ImageTk.PhotoImage(img)
#这里的坐标指的是图片的中心在画布中的位置

#这里的参数第一个是宽度
canvas1.create_image(960,540,image=photo)
# canvas1.pack(fill=BOTH)
canvas1.pack()

#为一个容器
menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
def do_job():
    pass
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单
filemenu.add_separator()##这里就是一条分割线

##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='Exit', command=window.quit)

window.mainloop()