import csv
from tkinter import * 
from tkinter import ttk
class Contactcreator:
    def __init__(self):
        #setup environment
        self.Font = ["arial 16"]
        root.geometry("200x280")
        root.title("contact creator")
        ttk.Style().configure("TLabel", relief="raised",background="#0ff", font=self.Font)
        ttk.Style().configure("TEntry", relief="raised",background="#aff", font=self.Font)
        ttk.Style().configure("TButton", relief="raised", background="#aff", font=self.Font)
        self.flabel = ttk.Label(text="filename")
        self.flabel.pack(side="top")
        self.filename = ttk.Entry()
        self.filename.pack(side="top")
        self.contactname = ttk.Label(text="name")
        self.contactname.pack(side="top")
        self.name = ttk.Entry()
        self.name.pack()
        self.phonenumber = ttk.Label(text="phonenumber:") 
        self.phonenumber.pack(side="top")
        self.number = ttk.Entry()
        self.number.pack()
        self.Email = ttk.Label(text="email address")
        self.Email.pack(side="top")
        self.email = ttk.Entry()
        self.email.pack()
        self.Save = ttk.Button(text="save data", command=self.save)
        self.Save.pack(side="top")
    """main function for creating contact data"""
    
    def save(self):
        with open(self.filename.get(), "a", newline='') as csvfile:
            self.fieldnames = ['name', "email-address","phonenumber"]
            self.writer =  csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            
            self.writer.writeheader()
            self.writer.writerow({'name':self.name.get(), "email-address":self.email.get(), "phonenumber":self.number.get()})

       

        
root = Tk()  
contactcreator = Contactcreator()
root.mainloop()
