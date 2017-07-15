from tkinter import *
from tkinter import messagebox
import pyttsx
import pyperclip
import webbrowser

class app():
    
        def __init__(self, master):
             frame = Frame(master)
             frame.pack()
             root.title("my text editor")
             self.fileName = StringVar()
             self.filename = Label(text="filename")
             self.filename.pack(fill="both")
             self.filen = Entry(textvariable=self.fileName, width="20" )
             self.filen.pack(side="top")
             self.contentdisplay = Label(text="contents")
             self.contentdisplay.pack(fill="both")
             self.contents = Text()
             self.contents.pack(fill="both")
             self.openfile = Button(text="open", command=self.fileopen)
             self.openfile.pack(side="left")
             self.save = Button(text="save", command=self.save)
             self.save.pack(side="left")
             self.fullsave = Button(text="overwrite", command=self.overwrite)
             self.fullsave.pack(side="left")
             self.save.pack(side="left")
             self.Newfile = Button(text="new file", command=self.new)
             self.Newfile.pack(side="left")
             self.cleartext = Button(text="clear txt", command=self.clearfile)
             self.cleartext.pack(side="left")
             self.Speak = Button(text="speak text", command=self.textSpeak)
             self.Speak.pack(side="left")
             self.About = Button(text="about me", command=self.about)
             self.About.pack(side="left")
             self.Copy = Button(text="Copy text", command=self.copytext)
             self.Copy.pack(side="left")
             self.Copy = Button(text="Paste text", command=self.Pastetext)
             self.Copy.pack(side="left")
             self.webview = Button(text="view in web browser", command=self.webview)
             self.webview.pack(side="left")
            
            
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
                    engine = pyttsx.init()
                    engine.say(self.contents.get(1.0,  END))
                    engine.runAndWait()
                
        def about(self):
                    messagebox.showinfo("about", "created by @technowizard")
        
        
        def copytext(self):
            self.Copiedtext = pyperclip.copy(self.contents.get(1.0,  END))
                     
        def Pastetext(self):
            self.contents.insert(INSERT, pyperclip.paste())
                    
        def webview(self):
            self.v = self.fileName.get()
            with open(self.v, "r") as r:
                webbrowser.open(self.v)
                
                
        
    
        








root = Tk()
App = app(root)
root.mainloop()
