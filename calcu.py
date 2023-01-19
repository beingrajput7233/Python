from errno import ENETDOWN
import math
from tkinter import *

from numpy import pad
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,columnspan=3,padx=10,pady=10)

def click(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))


def clear():
    e.delete(0,END)

def add():
    first_number=e.get()
    global math
    math="addition"
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def sub():
    first_number=e.get()
    global math
    math="subtract"
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def mul():
    first_number=e.get()
    global math
    math="multiply"
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def div():
    first_number=e.get()
    global math
    math="divide"
    global f_num
    f_num=int(first_number)
    e.delete(0,END)


def equal():
    second_number=e.get()
    e.delete(0,END)
    s_num=int(second_number)
    if math=="addition":
        e.insert(0,f_num+s_num)
    if math=="subtract":
        e.insert(0,f_num-s_num)
    if math=="multiply":
        e.insert(0,f_num*s_num)
    if math=="divide":
        e.insert(0,float(f_num)/float(s_num))
    


#defining button
b1=Button(root,text="1",padx=35,pady=10,command=lambda: click(1))
b2=Button(root,text="2",padx=35,pady=10,command=lambda: click(2))
b3=Button(root,text="3",padx=35,pady=10,command=lambda: click(3))
b4=Button(root,text="4",padx=35,pady=10,command=lambda: click(4))
b5=Button(root,text="5",padx=35,pady=10,command=lambda: click(5))
b6=Button(root,text="6",padx=35,pady=10,command=lambda: click(6))
b7=Button(root,text="7",padx=35,pady=10,command=lambda: click(7))
b8=Button(root,text="8",padx=35,pady=10,command=lambda: click(8))
b9=Button(root,text="9",padx=35,pady=10,command=lambda: click(9))
b0=Button(root,text="0",padx=35,pady=10,command=lambda: click(0))
be=Button(root,text="=",padx=76,pady=10,command=equal)
ba=Button(root,text="+",padx=34,pady=10,command=add)
bc=Button(root,text="CLR",padx=70,pady=10,command=clear)

bs=Button(root,text="-",padx=35,pady=10,command=sub)
bm=Button(root,text="*",padx=34,pady=10,command=mul)
bd=Button(root,text="/",padx=35,pady=10,command=div)
#Placing button
b1.grid(row="3",column="0")
b2.grid(row="3",column="1")
b3.grid(row="3",column="2")
b4.grid(row="2",column="0")
b5.grid(row="2",column="1")
b6.grid(row="2",column="2")
b7.grid(row="1",column="0")
b8.grid(row="1",column="1")
b9.grid(row="1",column="2")
b0.grid(row="4",column="0")
ba.grid(row="5",column="0")
bc.grid(row="4",column="1",columnspan=2)
be.grid(row="5",column="1",columnspan=2)
bs.grid(row="6",column="0")
bm.grid(row="6",column="1")
bd.grid(row="6",column="2")
root.mainloop()