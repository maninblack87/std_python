import os
from tkinter import *

root = Tk()
root.title("Jeon GUI")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open():
    pass

def save():
    pass

menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open)
menu_file.add_command(label="저장", command=save)
menu_file.add_separator()
menu_file.add_command(label="끝", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집 메뉴
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)

# 서식 메뉴
menu_lang = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_lang)

# 보기 메뉴
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view)

# 도움말 메뉴
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()