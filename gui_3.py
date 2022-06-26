from tkinter import *


win = Tk()
win.geometry("500x200")
win.title("로또 당첨번호")
win.option_add("*Font", "맑은고딕 20")


def lotto_p():
    import requests
    from bs4 import BeautifulSoup

    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(
        n)
    # div class="win_result"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()
    num = txt.split("\n")[7:13]
    print(num)
    bonus = txt.split("\n")[-4]
    print(bonus)


ent = Entry(win)

ent.pack()


btn = Button(win)
btn.config(width=20)
btn.config(text="당첨번호")
btn.config(command=lotto_p)

btn.pack()


win.mainloop()
