from tkinter import *
from tkinter import  messagebox
import pyttsx3
import webbrowser as search
import speech_recognition as sr
class app():
        
        def __init__(self, master):
             frame = Frame(master, width=400, height=400)
             frame.pack()
            
             engine = pyttsx3.init()
             engine.say("welcome to my app")
             engine.runAndWait()
             self.number = 0
             root.title("my app")
             self.apptitle = Label(frame, text="my app", border=3 )
             self.apptitle.pack(side="top")
             self.button = Button(frame, text="add", fg="red", border=4, command=self.add)
             self.button.pack(side="left")
             self.button2 = Button(frame, text="remove", fg="blue", border=4, command=self.remove)
             self.button2.pack(side="right")
             self.button3 = Button(frame, text="quit", fg="purple", border=4, command=frame.quit)
             self.button3.pack(side="bottom")
             self.button3 = Button(frame, text="about me", fg="blue", bg="red", border=4, command=self.aboutme)
             self.button3.pack(side="bottom")
             self.n = StringVar()
             self.n.set("please enter some text or  clear this text" )
             self.numbershow = Entry(frame, textvariable=self.n, )
             self.numbershow.pack(side="top")
             textvariable=self.n,
             self.write = Button(frame, text="write",   command=self.write)
             self.write.pack(side="left")
             self.read = Button(frame, text="read",   command=self.read)
             self.read.pack(side="right")
             self.modify = Button(frame, text="append",   command=self.append)
             self.modify.pack(side="right")
             self.speak = Button(frame, text="speak",   command=self.speak)
             self.speak.pack(side="left")
             self.clear = Button(frame, text="clear contents",   command=self.clearfile)
             self.clear.pack(side="left")
             self.search = Button(frame, text="search google",   command=self.google)
             self.search.pack(side="left")
             self.search = Button(frame, text=" search anime",   command=self.anime)
             self.search.pack(side="left")
             self.voiceconverter = Button(frame, text="voice to text",   command=self.v2t)
             self.voiceconverter.pack(side="left")
             

             
             
        def add(self):
            v = self.n.get();
            if self.number >= 1000:
                
                engine = pyttsx3.init()
                engine.say("action not allowed")
                engine.runAndWait()
                messagebox.showerror("can not go higher")
            else:
                self.number+=1
                engine = pyttsx3.init()
                engine.say(str(self.number))
                self.n.set(self.number)
                engine.runAndWait()
                
        def remove(self):
            v = self.n.get();
            if self.number < 1 :
                engine = pyttsx3.init()
                engine.say("action not allowed")
                engine.runAndWait()
                self.n.set(v)
            else:
                self.number-=1
                engine = pyttsx3.init()
                engine.say(str(self.number))
                engine.runAndWait()
                self.n.set(self.number)
                
         
        def speak(self):
                v = self.n.get();
                response = ["hello","what are you"]
                if v == response[0]:
                    engine = pyttsx3.init()
                    engine.say("hello creator")
                    engine.runAndWait()
                elif v == response[1]:
                    engine = pyttsx3.init()
                    engine.say("i am a bot")
                    engine.runAndWait()
                else:
                    engine = pyttsx3.init()
                    engine.say(v)
                    engine.runAndWait()
                    
            
        def write(self):
            with open("test.txt", "w") as fb_obj:
                v = self.n.get();
                if v == "":
                    self.n.set("invalid input")
                elif v == "invalid input!":
                    self.n.set("")
                else:
                    v = self.n.get();
                    fb_obj.write(v)
                    fb_obj.close()
        
        
        def write(self):
            with open("test.txt", "w") as fb_obj:
                v = self.n.get();
                if v == "":
                    self.n.set("nothing to write")
                elif v == "nothing to write":
                    self.n.set("")
                else:
                    v = self.n.get();
                    fb_obj.write(v)
                    fb_obj.close()
                    
        
        def read(self):
            with open("test.txt", "r") as fb_obj:
                v = self.n.get();
                if v == "":
                    self.n.set("invalid input!")
                elif v == "invalid input!":
                    self.n.set("")
                else:
                    content = fb_obj.read()
                    self.n.get();
                    fb_obj.close()
                    print(content)
                    engine = pyttsx3.init()
                    engine.say(content)
                    engine.runAndWait()
                        
                
        
        def append(self):
            with open("test.txt", "a") as fb_obj:
                v = self.n.get();
                if v == "":
                    self.n.set("invalid search!")
                elif v == "invalid search!":
                    self.n.set("")
                else:
                    v = self.n.get();
                    fb_obj.write(v)
                    fb_obj.close()
                
                
                
        def clearfile(self):
            with open("test.txt", "w") as fb_obj:
                fb_obj.write("")
                fb_obj.close()
                self.n.set("")
        def aboutme(self):
                engine = pyttsx3.init()
                engine.say("I am austin heisley cook.  I program in python. my  mind is power my power is mind")
                engine.runAndWait()
        def google(self):
                v = self.n.get();
                if v == "":
                    self.n.set("invalid search!")
                elif v == "invalid search!":
                    self.n.set("")
                else:
                    search.open_new("https://www.google.com/search?q=" + v)
        def v2t(self):
            listening = True;
            while listening:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    engine = pyttsx3.init()
                    text = r.recognize_google(audio)
                    if text == "quit listening":
                        listening = False
                    else:
                       v = self.n.get();
                       self.n.set(v)
        def anime(self):
                v = self.n.get();
                if v == "":
                    self.n.set("invalid search!")
                elif v == "invalid search!":
                    self.n.set("")
                else:
                    search.open("https://www.zerochan.com/" + v)

root = Tk()


App = app(root)
root.mainloop()
