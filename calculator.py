from tkinter import *
from fractions import *
from tkinter import messagebox
class app():
        
        def __init__(self, master):
             frame = Frame(master, width=1000, height=1000)
             frame.pack()

             self.number = 0
             root.title("my app")
             self.apptitle = Label(frame, text="my calculator".title(), border=3)
             self.apptitle.pack(side="top")
             """buttons to control calculator functions"""
             self.add = Button(frame, text="+", fg="red", border=1, command=self.add)
             self.add.pack(side="left")
             self.sub = Button(frame, text="-", fg="red", border=1, command=self.subt)
             self.sub.pack(side="left")
             self.mult = Button(frame, text="X", fg="red", border=1, command=self.mult)
             self.mult.pack(sid="left")
             self.div = Button(frame, text="/", fg="red", border=1, command=self.div)
             self.div.pack(side="left")
             self.expo = Button(frame, text="x^Y", fg="red", border=1, command=self.ex)
             self.expo.pack(side="left")
             self.check = Button(frame, text="x|y", fg="red", border=1, command=self.fractions)
             self.check.pack(side="left")
             self.button3 = Button(frame, text="quit", fg="red", bg="red", border=1, command=frame.quit)
             self.button3.pack(side="left")
             #numbers calculate
             self.x = StringVar(str(""))
             self.y = StringVar(str(""))
             self.r = StringVar(str(""))
             self.hc = StringVar(str(""))
             #first int and second
             self.int1 = Entry(frame, textvariable=self.x)
             self.int1.pack(side="top")
             self.int2 = Entry(frame, textvariable=self.y)
             self.int2.pack(side="top")
             #result calculation
             self.int3 = Entry(frame, textvariable=self.r)
             self.int3.pack(side="top")
            
        """basic math operation functions"""
        
        def subt(self):
             self.x2 = str(self.x.get())
             self.x3 = str(self.y.get())
             self.r3 = int(self.x2) -  int(self.x3)  
             if self.x2 == "" or self.x3 == "":
                 self.v = self.r.set("can't compute due to blank entry")
             else:
                 self.v = self.r.set(str(self.r3))
        def add(self):
             self.x2 = str(self.x.get())
             self.x3 = str(self.y.get())
             self.r3 = int(self.x2) +  int(self.x3)
             if self.x2 == "" or self.x3 == "":
                 self.v = self.r.set("can't compute due to blank entry")
             else:
                self.v = self.r.set(str(self.r3))     
        
        def mult(self):
             self.x2 = str(self.x.get())
             self.x3 = str(self.y.get())
             self.r3 = int(self.x2) *  int(self.x3)  
             if self.x2 == "" or self.x3 == "":
                 self.v = self.r.set("can't compute due to blank entry")
             else: 
                self.v = self.r.set(str(self.r3))     
        def div(self):
            try:
                self.x2 = str(self.x.get())
                self.x3 = str(self.y.get())
                self.r3 = int(self.x2) /  int(self.x3)
                self.v = self.r.set(str(self.r3))
            except:
                    messagebox.showerror("error","you can't divide by 0")
        
        def ex(self):
             self.x2 = str(self.x.get())
             self.x3 = str(self.y.get())
             self.r3 = int(self.x2) **  int(self.x3)  
             self.v = self.r.set(str(self.r3))  
        def fractions(self):
             self.x2 = str(self.x.get())
             self.x3 = str(self.y.get())
             self.r3 =  Fraction(int(self.x2), int(self.x3))  
             self.v = self.r.set(self.r3 ) 
             

root = Tk()


App = app(root)
root.mainloop()
