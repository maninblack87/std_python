from tkinter import *
from datetime import datetime


win = Tk()
win.geometry("1000x500")
win.title("현재 시간")
win.option_add("*Font", "맑은고딕 25")


def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)


btn = Button(win)
btn.config(text="현재 시간")
btn.config(width=25)
btn.config(command=what_time)

btn.pack()


win.mainloop()
