from tkinter import  *
import turtle
from tkinter import  messagebox
import sys

def goright():
  try:
    speed = int(speedSet.get())
    turtle.right(speed)
  except:
      messagebox.showerror("error", " the input  was not a numerical character")

def goleft():
  try:
     speed = int(speedSet.get())
     turtle.left(speed)
  except:
     messagebox.showerror("error"," the input  was not a numerical character")


def goforward():
  try:
    speed = int(speedSet.get())
    turtle.forward(speed)
  except:
    messagebox.showerror("error", " the input  was not a numerical character")



def gobackward():
  try:
    speed = int(speedSet.get())
    turtle.backward(speed)
  except:
    messagebox.showerror("error", " the input  was not a numerical character")

def setcolor():
   color = colorentry.get()
   turtle.color(color)

def saveimage():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="c:\\users\owner\\pictures\img.jpg")
    messagebox.showinfo("done","image is saved")
root = Tk()
speedSet =  Entry()
speedSet.grid(row=3, column=5)
speedset = Label(text="set speed")
speedset.grid(row=3, column=4)
colorset = Button(text="setcolor", command=setcolor)
colorset.grid(row=4, column=4)

colorentry = Entry()
colorentry.grid(row=4, column=5)
title = Label(text="my drawing app with turtle")
title.grid(row=0, column=3)
left = Button(text="left", command=goleft)
left.grid(row=1, column=1)
right = Button(text="right", command=goright)
right.grid(row=1, column=2)
forward = Button(text="forward", command=goforward)
forward.grid(row=1, column=3)
backward = Button(text="backward", command=gobackward)
backward.grid(row=1, column=4)
save = Button(text="save", command=saveimage)
save.grid(row=1, column=5)









root.mainloop()


