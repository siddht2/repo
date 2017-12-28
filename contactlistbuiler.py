import csv
from tkinter import * 
from tkinter import ttk
from sys import *
from tkinter import messagebox as mbx
class Contactcreator:
    def __init__(self):
        """setup environment"""
        self.Font = ["verdena 14"]
        self.Bsize = ["verdena 16"]
        root.geometry("290x280")
        root.title("contact creator")
        root.resizable(0,0)
        ttk.Style().configure("TFrame", )
        ttk.Style().configure("TLabel", relief="raised", background="#0ff", font=self.Font)
        ttk.Style().configure("TEntry", relief="raised",background="#aff", font=self.Font)
        ttk.Style().configure("TButton", relief="raised", background="#aff", font=self.Bsize)
        self.lsize = 16
        self.esize = 28
        self.bsize = 15
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_command(label="about", command=self.about)
        menu.add_command(label="exit", command=root.quit)
        self.flabel = ttk.Label(text="filename", width=self.lsize)
        self.flabel.pack(side="top")
        self.filename = ttk.Entry(width=self.esize)
        self.filename.pack(side="top")
        self.contactname = ttk.Label(text="name", width=self.lsize)
        self.contactname.pack(side="top")
        self.name = ttk.Entry(width=self.esize)
        self.name.pack()
        self.phonenumber = ttk.Label(text="phonenumber", width=self.lsize) 
        self.phonenumber.pack(side="top")
        self.number = ttk.Entry(width=self.esize)
        self.number.pack()
        self.Email = ttk.Label(text="email", width=self.lsize)
        self.Email.pack(side="top")
        self.email = ttk.Entry(width=self.esize)
        self.email.pack()
        self.Save = ttk.Button(text="save data", command=self.save, width=self.bsize)
        self.Save.pack(side="top")
    """main function for creating contact data"""
    def save(self):
        with open(self.filename.get(), "a", newline='') as csvfile:
            self.fieldnames = ['name', "email-address","phonenumber"]
            self.writer =  csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            
            self.writer.writeheader()
            self.writer.writerow({'name':self.name.get(), "email-address":self.email.get(), "phonenumber":self.number.get()})

    def about(self):
        mbx.showinfo("about","created by austin Heisley-Cook.\n\nyear:2017")





        
root = Tk()  
contactcreator = Contactcreator()
root.mainloop()
