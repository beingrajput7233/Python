from tkinter import *
from turtle import st

root=Tk()
def func():
    myLabel=Label(root,text="Clicked a button!").pack()



myButton1=Button(root,text="Click me!",command=func).pack()

#CHANGING SIZE
myButton2=Button(root,text="Click me!",state=DISABLED).pack()
myButton3=Button(root,text="Click me!",padx=50).pack()
myButton4=Button(root,text="Click me!",pady=50).pack()
myButton5=Button(root,text="Click me!",pady=50,padx=50).pack()

#CHANGING COLOUR
myButton6=Button(root,text="Click me!",command=func,fg="black",bg="red").pack()
root.mainloop()  #root is the mainloop
