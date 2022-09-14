import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")


# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10ms 마다 움직임(밀리세컨드)
# progressbar.pack()


# def btncmd():
#     progressbar.stop()  # 작동중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()  # 정수 뿐만 아니라 소수점도 나타낼 수 있도록 하기위해
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    pass


btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()
