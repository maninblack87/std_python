from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")

# selectmode="single" 하나만 선택 가능한
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 리스트박스 삭제
    # listbox.delete(0) #listbox 삭제

    # 리스트박스 개수 확인
    # print("리스트에는", listbox.size())

    # 항목 확인
    # print("1번부터 3번까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인
    print("선택된 항목: ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
