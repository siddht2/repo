from tkinter import *
from tkinter import messagebox

import pyttsx3
import pyperclip
import webbrowser
from tkinter import  font
import sys
#modules_used
class app():
        """user interface layout """
        def __init__(self, frame):
             frame = Frame()
             frame.pack()
             root.title("my text editor")
             self.fileName = StringVar()
             self.filename = Label(text="filename")
             self.filename.pack(fill="both")
             self.filen = Entry(textvariable=self.fileName, width="20")
             self.filen.pack(side="top")
             self.contentdisplay = Label(text="contents", font="Arial 12"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         )
             self.contentdisplay.pack(fill="both", padx=19)
             self.contents = Text()
             self.contents.pack(fill="both")
             self.openfile = Button(text="open", command=self.fileopen, font="Arial 12")
             self.openfile.pack(side="left")
             self.save = Button(text="add content", command=self.save , font="Arial 12")
             self.save.pack(side="left")
             self.fullsave = Button(text="save", command=self.overwrite , font="Arial 12")
             self.fullsave.pack(side="left")
             self.Newfile = Button(text="new file", command=self.new, font="Arial 12")
             self.Newfile.pack(side="left")
             self.cleartext = Button(text="clear txt", command=self.clearfile, font="Arial 12")
             self.cleartext.pack(side="left")
             self.Speak = Button(text="speak text", command=self.textSpeak, font="Arial 12")
             self.Speak.pack(side="left")
             self.About = Button(text="about me", command=self.about, font="Arial 12")
             self.About.pack(side="left")
             self.Copy = Button(text="Copy text", command=self.copytext, font="Arial 12")
             self.Copy.pack(side="left")
             self.Copy = Button(text="Paste text", command=self.Pastetext, font="Arial 12")
             self.Copy.pack(side="left")
             self.webview = Button(text="web view", command=self.webview, font="Arial 12")
             self.webview.pack(side="left")
             self.search = Button(text="search", command=self.searchit, font="Arial 12")
             self.search.pack(side="left")
             self.Exit = Button(text="exit", command=self.Exitprogram, font="Arial 12")
             self.Exit.pack(side="left")

        """user interface controls and functions"""      
            
        def fileopen(self):
         try:
            self.v = self.fileName.get()
            with open(self.v, "r") as r:
                content = r.read()
                self.contents.insert(INSERT, content)
         except:
                messagebox.showwarning("error", "file not found")
                
        def save(self):
         try:
            self.v = self.fileName.get()
            with open(self.v, "a") as w:
                w.write(self.contents.get(1.0,  END))
         except:
                messagebox.showwarning("error", "file not found")
                
        def new(self):
            self.v = self.fileName.get()
            with open(self.v, "w") as w:
                w.write("") 
                    
        def clearfile(self):
            try:
                self.v = self.fileName.get()
                with open(self.v, "w+") as w:
                    w.write("")
                    self.contents.insert(INSERT, "")
            except:
                messagebox.showwarning("file not found")
                
        def overwrite(self):
            try:
                self.v = self.fileName.get()
                with open(self.v, "w") as w:
                    w.write(self.contents.get(1.0,  END))
            except:
                messagebox.showwarning("error", "file not found")
                
        def textSpeak(self):
                    self.engine = pyttsx3.init()
                    self.engine.say(self.contents.get(1.0,  END))
                    self.engine.runAndWait()
                
        def about(self):
                    messagebox.showinfo("about", "created by:Technowizard \n\nyear:2017")
        
        
        def copytext(self):
            self.Copiedtext = pyperclip.copy(self.contents.get(1.0,  END))
                     
        def Pastetext(self):
            self.contents.insert(INSERT, pyperclip.paste())
                    
        def webview(self):
            try:
                self.v = self.fileName.get()
                with open(self.v, "r") as r:
                    webbrowser.open_new(self.v)
            except:
                messagebox.showwarning("error", "file not found")

        def searchit(self):
            self.v = self.fileName.get()
            webbrowser.open_new_tab("https://www.google.com/search?q=" + self.v)
                     
        def Exitprogram(self):
            sys.exit()
        








root = Tk()
App = app(root)
root.mainloop()
