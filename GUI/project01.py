import os
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.messagebox as msgbox
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Jeon GUI")

# 1. 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)


def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.",
                                        filetypes=(
                                            ("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir="C:/jeon/python/GUI")

    for file in files:
        list_file.insert(END, file)


def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def brows_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # 사용자가 취소를 누를 때
        print("폴더 선택 취소")
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합
def merge_image():

    try:

        # 가로넓이 옵션
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)

        # 간격 옵션
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        if img_space == "보통":
            img_space = 60
        if img_space == "넓게":
            img_space = 90
        else:  # 없음
            img_space = 0

        # 포맷 옵션
        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 사이즈처리 : 이미지 사이즈 리스트에 넣어서 하나씩 처리
        img_sizes = []
        if img_width > -1:
            img_sizes = [(int(img_width), int(img_width*x.size[1]/x.size[0]))
                         for x in images]
        else:
            img_sizes = [(x.size[0], x.size[1]) for x in images]
        # x : y = ' : y'
        # xy' = x'y
        # y' = x'y/x

        widths, heights = zip(*(img_sizes))

        max_width, total_height = max(widths), sum(heights)

        # 스케치북 준비
        if img_space > 0:  # total_height(스케치북 높이)에 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))
        result_img = Image.new(
            "RGB", (max_width, total_height), (255, 255, 255))

        y_offset = 0  # y의 위치
        for idx, img in enumerate(images):
            # width가 원본유지가 아닐 때에는 이미지 크기를 조정해야 됨
            if img_width > -1:
                img = img.resize(img_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100  # 실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "project01_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료")

    except Exception as err:  # 예외처리
        msgbox.showerror("에러", err)


def start():
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가해주세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장경로를 선택해주세요")
        return

    # 이미지 통합 작업
    merge_image()


# 1-1. 파일추가 버튼
btn_add_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

# 1-2. 선택삭제 버튼
btn_del_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 2. 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

# 2-1. 스크롤바(오른쪽)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# 2-2. 리스트박스(왼쪽)
list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 3. 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

# 3-1. 저장경로
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

# 3-2. 찾아보기 버튼
browse_dest_path = Button(path_frame, text="찾아보기",
                          width=10, command=brows_dest_path)
browse_dest_path.pack(side="right", padx=5)

# 4. 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5)

# 4-1-1. 가로 넓이 옵션
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# 4-1-2. 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 4-2-1. 간격 옵션
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 4-2-2. 간격옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 4-3-1. 파일포맷 옵션
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# 4-3-2. 파일포맷 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 5. 진행상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")

# 5-1. 진행상황 프로그레스 바
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

# 6. 실행/닫기 프레임
run_frame = Frame(root)
run_frame.pack(side="right", padx=5, pady=5)

# 6-2. 닫기 버튼
btn_close = Button(run_frame, text="닫기", command=root.quit, width=5)
btn_close.pack(side="right", padx=2)

# 6-1. 실행 버튼
btn_start = Button(run_frame, text="실행", width=5, command=start)
btn_start.pack(side="right", padx=2)

root.resizable(False, False)
root.mainloop()
