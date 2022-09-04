from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")


def btncmd():
    print(txt.get("1.0", END))  # 1.0(1줄 0열) 부터 끝(END)까지 출력해라

    txt.delete("1.0", END)  # 텍스트 전부 삭제
    e.delete(0, END)  # 엔트리 전부 삭제


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
