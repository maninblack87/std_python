from tkinter import *


win = Tk()
win.geometry("500x600")
win.title("공공데이터 API")
win.option_add("*Font", "맑은고딕 15")


# URL주소 라벨
lab1 = Label(win)
lab1.config(text="URL주소를 입력해주세요")
lab1.pack()
# URL주소 입력창
ent1 = Entry(win)
ent1.config(width=40)
ent1.pack()

# key 라벨
lab2 = Label(win)
lab2.config(text="key를 입력해주세요")
lab2.pack()
# key 입력창
ent2 = Entry(win)
ent2.config(width=40)
ent2.pack()

# 페이지당 열 개수 라벨
lab3 = Label(win)
lab3.config(text="페이지당 열개수를 입력해주세요")
lab3.pack()
# 페이지당 열 개수 입력창
ent3 = Entry(win)
ent3.config(width=40)
ent3.pack()


# 페이지당 열 개수 라벨
lab3 = Label(win)
lab3.config(text="페이지당 열개수를 입력해주세요")
lab3.pack()
# 페이지당 열 개수 입력창
ent3 = Entry(win)
ent3.config(width=40)
ent3.pack()


win.mainloop()
