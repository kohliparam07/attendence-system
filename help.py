from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1260x650+0+0")
        self.root.title("Face Recogniton System")

        # copied from train.py
        title_lbl = Label(self.root, text="Help Desk", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1270, height=45)

        img_top = Image.open(r"images\helpdesk.jpg")
        img_top = img_top.resize((1270, 650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1lbl = Label(self.root, image=self.photoimg_top)
        f_1lbl.place(x=0, y=55, width=1270, height=650)

        dev_label = Label(f_1lbl, text="Email:ngoyal2299@gmail.com ",
                          font=("Times New Roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=550, y=220)

        # main.py

        # 154

        # 144 and 147 both exit button
        # command = self.iExit

        # 4

        # 57 along title label
        # ==========time========
        # def time():
        # string = strftime('%H:%M:%S %p')
        # lbl.config(text=string)
        # lbl.after(1000, time)

        # lbl = Label(title_lbl, font=('times new roman', 14, 'bold'),
        #             background='white', foreground='blue')
        # lbl.place(x=0, y=0, width=110, height=50)
        # time()

        # 6 and 7
        # from time import strftime
        # from datetime import datetime


if __name__ == "_main_":
    root = Tk()
    obj = Help(root)
    root.mainloop()