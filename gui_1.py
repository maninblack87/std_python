from tkinter import *

win = Tk()
win.geometry("1000x500")
win.title("jeon_coding")
win.option_add("*font", "맑은고딕 25")
win.configure(bg='orange')

btn = Button(win, text="버튼")
btn.pack()

win.mainloop()
