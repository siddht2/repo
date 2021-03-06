import  smtplib
from tkinter import  *
from tkinter import  messagebox as mbx
import sys

class email_app:


    def __init__(self, master):
        self.pn = Entry(master, width=30)
        self.pn.grid(column=2, row=0)
        self.portname = Label(master, text="portnumber")
        self.portname.grid(column=1, row=0)

        self.sn = Entry(master, width=30)
        self.sn.grid(column=2, row=1)

        self.servername =   Label(master, text="emailserver")
        self.servername.grid(column=1, row=1)

        self.usern = Label(master, text="username")
        self.usern.grid(column=1, row=2, sticky=E)

        self.userE = Entry(master, width=30)
        self.userE.grid(column=2, row=2, sticky=E)

        self.pass1 = Label(master, text="password")
        self.pass1.grid(column=1, row=3, sticky=E)

        self.passE = Entry(master, width=30)
        self.passE.grid(column=2, row=3, sticky=E)

        self.text = Label(master, text="receiver")
        self.text.grid(column=1, row=4, sticky=E)

        self.receivert = Entry(master,width=30)
        self.receivert.grid(column=2, row=4, sticky=W)

        self.Lmsg = Entry(master, width=30)
        self.Lmsg.grid(column=2, row=5, stick=W)

        self.Emsg = Label(master, text="message")
        self.Emsg.grid(column=1, row=5, sticky=E)

        self.start = Button(master, text="send", command=self.send)
        self.start.grid(column=1, row=6, sticky=S)
        self.quit = Button(master, text="quit", command=self.quit)
        self.quit.grid(column=2, row=6)

    def quit(self):
            sys.exit()

    def send(self):
            servername = self.sn.get()
            portnum = int(self.pn.get())
            server = smtplib.SMTP(servername, portnum)
            user = self.userE.get()
            passt = self.passE.get()
            server.starttls()
            msg = self.Lmsg.get()
            recipient = self.receivert.get()
            server.login(user, passt)
            server.sendmail(user, recipient, msg)
            server.quit()
            mbx.showinfo("test","mesage was sent")

root = Tk()

obj = email_app(root)

root.mainloop()


