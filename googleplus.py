from tkinter import *
import webbrowser
class App:
    def __init__(self, master):
        #structcure
        self.searchbox = Entry(master)
        self.searchbox.grid(row=1, column=1)

        self.searchbutton = Button(master, text="search", bg="red", fg="white",  command=self.search)
        self.searchbutton.grid(row=1, column=2, sticky=W)



    def search(self):
        self.query = self.searchbox.get()
        webbrowser.open("https://plus.google.com/u/0/s/" + self.query)







root = Tk()
app = App(root)
root.mainloop()
