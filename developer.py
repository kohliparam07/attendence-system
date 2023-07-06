from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recogniton System")

        # copied from train.py
        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1270, height=45)

        img_top = Image.open(r"images\dev.jpg")
        img_top = img_top.resize((1270, 650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1lbl = Label(self.root, image=self.photoimg_top)
        f_1lbl.place(x=0, y=55, width=1270, height=650)

        # Frame
        main_frame = Frame(f_1lbl, bd=2, bg="white")
        main_frame.place(x=0, y=0, width=500, height=600)

        img_top1 = Image.open(r"images\kiran.jpg")
        img_top1 = img_top1 .resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top)

        f_1lbl = Label(main_frame, image=self.photoimg_top)
        f_1lbl.place(x=300, y=0, width=200, height=200)

        # Developer Info
        dev_label = Label(main_frame, text="Developer", font=(
            "Times New Roman", 20, "bold"), fg="blue", bg="white")
        dev_label.place(x=0, y=5)

        dev_label = Label(main_frame, text="I am full stack developer", font=("times new roman", 20, "bold"))
        dev_label.place(x=0, y=40)

        img2=Image.open(
            r"images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500, 390), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=390)


# main.py
# 9 line no


# 174


# 132 and 135both developer face button
 # command = self.develop_data,



if __name__ == "_main_":
    root=Tk()
    obj=Developer(root)
    root.mainloop()