from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

# 주의: set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):  # 1~31일
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

root.mainloop()
