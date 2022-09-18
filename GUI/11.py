from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")

Label(root, text="음료를 선택해주세요").pack(side="top")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

# 주문하기 버튼
Button(root, text="주문하기").pack(side="bottom")

root.mainloop()
