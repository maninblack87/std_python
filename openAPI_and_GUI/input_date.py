from tkinter import *
from datetime import datetime, timedelta

root = Tk()
root.title("날짜 입력")
root.geometry("640x480")

# 시작일 프레임 입력
start_frm = LabelFrame(root, text="시작일 입력")
start_frm.pack(fill="x", padx=5, pady=5)

start_ent = Entry(start_frm)
start_ent.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

# 종료일 프레임 입력
end_frm = LabelFrame(root, text="종료일 입력")
end_frm.pack(fill="x", padx=5, pady=5)

end_ent = Entry(end_frm)
end_ent.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

# 날짜 버튼
date_btn = Button(root, text="클릭", command=input_date)
date_btn.pack()

root.mainloop()


# 날짜 입력
def input_date():
    start = start_ent
    end = end_ent
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")


print("시작일 :{}".format(start_date))
