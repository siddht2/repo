# from Tkinter import  * # 2.7
from tkinter import * 
import turtle
# import tkMessageBox as mbx # 2.7
from tkinter import messagebox as mbx
import sys




class drawing_app:
    def __init__(self, master):

        # Initiate environment
        self.speedSet =  Entry(master)
        self.speedSet.grid(row=3, column=5)
        self.speedset = Label(master,text="set speed")
        self.speedset.grid(row=3, column=4)

        self.colorset = Button(master, text="setcolor", command=self.setcolor)
        self.colorset.grid(row=4, column=4)

        self.colorentry = Entry(master)
        self.colorentry.grid(row=4, column=5)

        self.title = Label(master,text="my drawing app with turtle")
        self.title.grid(row=0, column=3)

        self.left = Button(master,text="left", command=self.goleft)
        self.left.grid(row=1, column=1)

        self.right = Button(master,text="right", command=self.goright)
        self.right.grid(row=1, column=2)

        self.forward = Button(master,text="forward", command=self.goforward)
        self.forward.grid(row=1, column=3, sticky=E)

        self.backward = Button(master,text="backward", command=self.gobackward)
        self.backward.grid(row=1, column=4)

        self.save = Button(master,text="save", command=self.saveimage)
        self.save.grid(row=1, column=5)
        self

    def goright(self):
      try:
        speed = int(self.speedSet.get())
        turtle.right(speed)
      except:
          mbx.showerror("error", " the input  was not a numerical character")

    def goleft(self):
      try:
         speed = int(self.speedSet.get())
         turtle.left(speed)
      except:
         mbx.showerror("error"," the input  was not a numerical character")


    def goforward(self):
      try:
        speed = int(self.speedSet.get())
        turtle.forward(speed)
      except:
        mbx.showerror("error", " the input  was not a numerical character")



    def gobackward(self):
      try:
        speed = int(self.speedSet.get())
        turtle.backward(speed)
      except:
        mbx.showerror("error", " the input  was not a numerical character")

    def setcolor(self):
       color = self.colorentry.get()
       turtle.color(color)

    def saveimage(self):
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="c:\\users\owner\\pictures\img.jpg")
        mbx.showinfo("done","image is saved")


root = Tk()
# Make object app using drawing_appp class
obj = drawing_app(root)
root.mainloop()

    
    



