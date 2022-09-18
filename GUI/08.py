import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")


# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 프로그레스 바 실행
# progressbar.pack()


# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(101):
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)
        progressbar2.update()  # ui 업데이트
        print(p_var2.get())  # 출력 progressbar2 진행정도 출력


btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()
