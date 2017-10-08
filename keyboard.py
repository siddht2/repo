
from tkinter import  *
import os
import  pyautogui
class Keyboard:
    #initialize_nvironment
    def __init__(self, master):
        window = Frame(master, width=30, height=90)
        window.grid()
        root.title("my keyboard")
        self.one_key = Button(master, text="1", command=self.presskey_1)
        self.one_key.grid(row=0, column=1)

        self.two_key = Button(master, text="2", command=self.presskey_2)
        self.two_key.grid(row=0, column=2)

        self.three_key = Button(master, text="3", command=self.presskey_3)
        self.three_key.grid(row=0, column=3)
        self.three_key = Button(master, text="4", command=self.presskey_3)
        self.three_key.grid(row=0, column=4)

        self.q_key = Button(master, text="q", command=self.presskey_q)
        self.q_key.grid(row=1, column=1)
        self.w_key = Button(master, text="w", command=self.presskey_w)
        self.w_key.grid(row=1, column=2)
        self.e_key = Button(master, text="e", command=self.presskey_e)
        self.e_key.grid(row=1, column=3)
        self.r_key = Button(master, text="r", command=self.presskey_r)
        self.r_key.grid(row=1, column=4)
        self.t_key = Button(master, text="t", command=self.presskey_t)
        self.t_key.grid(row=1, column=5)

    #keyboard_actions#
    def presskey_1(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("1", interval=0.1)

    def presskey_2(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("2", interval=0.1)

    def presskey_3(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("3", interval=0.1)

    def presskey_3(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("4", interval=0.1)

            #num keys only for now

    def presskey_q(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("q", interval=0.1)
    def presskey_w(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("w", interval=0.1)

    def presskey_e(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("e", interval=0.1)

    def presskey_r(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("r", interval=0.1)

    def presskey_t(self):
        x = pyautogui.position()
        pyautogui.click(x)
        pyautogui.press("t", interval=0.1)


root = Tk()
keyboard = Keyboard(root)
root.mainloop()
