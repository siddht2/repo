# from Tkinter import  * # 2.7
from tkinter import * 
import turtle
# import tkMessageBox as mbx # 2.7
from tkinter import messagebox as mbx
import sys




class drawing_app:
    def __init__(self, master):

        turtle.position()
        (11.122,122.122)
        # Initiate environment
        self.speedSet =  Entry(master)
        self.speedSet.grid(row=3, column=5)
        self.speedset = Label(master,text="set speed")
        self.speedset.grid(row=3, column=4)

        self.colorset = Button(master, text="setcolor", command=self.setcolor)
        self.colorset.grid(row=4, column=4)

        self.colorentry = Entry(master)
        self.colorentry.grid(row=4, column=5)

        self.title = Label(master, text="my drawing app with turtle")
        self.title.grid(row=0, column=3)

        self.left = Button(master, text="left", command=self.goleft)
        self.left.grid(row=1, column=1)

        self.right = Button(master, text="right", command=self.goright)
        self.right.grid(row=1, column=2)

        self.forward = Button(master, text="forward", command=self.goforward)
        self.forward.grid(row=1, column=3, sticky=E)

        self.backward = Button(master, text="backward", command=self.gobackward)
        self.backward.grid(row=1, column=4)

        self.save = Button(master, text="save", command=self.saveimage)
        self.save.grid(row=6, column=4, sticky=W)

        self.stop = Button(master, text="exit", command=sys.exit)
        self.stop.grid(row=6, column=6)

        self.dissapear = Button(master, text="hide", command=self.hide)
        self.dissapear.grid(row=6, column=1)

        self.show = Button(master, text="show", command=self.appear)
        self.show.grid(row=6, column=2, stick=N + E)

        self.restart = Button(master, text="resetP", command=self.reset)
        self.restart.grid(row=6, column=5, sticky=E)

        self.currentP = Button(text="show current position", command=self.showcurrent)
        self.currentP.grid(row=7, column=5)
    def goright(self):
      try:
        speed = float(self.speedSet.get())
        turtle.right(speed)
      except:
          mbx.showerror("error", " the input  was not a numerical character")

    def goleft(self):
      try:
         speed = float(self.speedSet.get())
         turtle.left(speed)
      except:
         mbx.showerror("error"," the input  was not a numerical character")


    def goforward(self):
      try:
        speed = float(self.speedSet.get())
        turtle.forward(speed)
      except:
        mbx.showerror("error", " the input  was not a numerical character")



    def gobackward(self):
      try:
        speed = float(self.speedSet.get())
        turtle.backward(speed)
      except:
        mbx.showerror("error", " the input  was not a numerical character")

    def setcolor(self):
       color = self.colorentry.get()
       turtle.color(color)

    def saveimage(self):
        self.ts = turtle.getscreen()
        self.ts.getcanvas().postscript(file="c:\\users\owner\\pictures\img.jpg")
        self.mbx.showinfo("done","image is saved")

    def hide(self):
        turtle.ht()

    def appear(self):
        turtle.st()

    def reset(self):
        turtle.penup()
        self.start = (11.122,122.122)
        turtle.goto(self.start)
        turtle.pendown()
        turtle.st()

    def saveimage(self):
        self.ts = turtle.getscreen()
        self.ts.getcanvas().postscript(file="img.ps")

    def showcurrent(self):
        self.current = turtle.position()
        mbx.showinfo("current coordinates", self.current)




root = Tk()
# Make object app using drawing_appp class
obj = drawing_app(root)
root.mainloop()

    
    



