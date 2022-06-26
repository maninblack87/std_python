from tkinter import *


win = Tk()
win.title("Jeon")
win.geometry("500x300")
win.option_add("*Font", "궁서 20")

lab1 = Label(win)
lab1.config(text="입력1")
lab1.pack()
ent1 = Entry(win)
ent1.pack()
res1 = Entry(win)
res1.pack()

lab2 = Label(win)
lab2.config(text="입력2")
lab2.pack()
ent2 = Entry(win)
ent2.pack()
res2 = Entry(win)
res2.pack()


def m_str():


btn = Button(win)
btn.config(text="문자열병합")
btn.pack(m_str)


win.mainloop()
