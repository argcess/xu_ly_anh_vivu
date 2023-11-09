from tkinter import *

# thư viện chèn ảnh pillow
from PIL import ImageTk, Image

top = parent = Tk()  # mở lên cửa sổ chương trình


def an_vao():
    x = float(e1.get()) + float(e2.get())
    ket_qua = Label(top, text="gia tri tro loi :" + str(x), font=("Arial", 14))
    ket_qua.place(x=200, y=140)


top.title("giao diện")  # tên cửa sổ giao diện
top["bg"] = "white"  # màu nền trắng
top.attributes("-topmost", True)  # luôn hiển thị trên màn hình trừ khi mình tắt
top.geometry("700x500")  # kích thước ảnh XxY
name = Label(top, bg="red", text="Các màu điện trở", font=("Arial", 15)).place(
    x=30, y=50
)
email = Label(top, text="Giá trị điện trở", font=("Arial", 15)).place(
    x=30, y=90
)  # bg màu ô , fg màu chữ
password = Label(top, text="  BÁO LỖI  ", font=("Arial", 15)).place(x=30, y=130)
e1 = Entry(top, width=40, font=("Arial", 15)).place(
    x=200, y=50
)  # chiều cao của ô nhập phụ thuộc vào kích thước chứ
e2 = Entry(top, width=20, font=("Arial", 15)).place(x=200, y=90)
e3 = Entry(top, width=40, font=("Arial", 15)).place(x=200, y=130)


redbutton = Button(parent, text="Red", font=("Arial", 15), fg="red", command=an_vao)
redbutton.place(x=20, y=450, width=70, height=30)
greenbutton = Button(parent, text="Black", font=("Arial", 15), fg="black")
greenbutton.place(x=200, y=450, width=70, height=30)
bluebutton = Button(parent, text="Blue", font=("Arial", 15), fg="blue")
bluebutton.place(x=400, y=450, width=70, height=30)
blackbutton = Button(parent, text="Green", font=("Arial", 15), fg="green")
blackbutton.place(x=580, y=450, width=70, height=30)


img_import = Image.open("T.png")
resize = img_import.resize((250, 250), Image.LANCZOS)
img = ImageTk.PhotoImage(resize)

hinh_anh = Button(top, text="hinh", font=("Time New Roman", 11), image=img)
hinh_anh.place(x=410, y=180)

parent.mainloop()
top.mainloop()
