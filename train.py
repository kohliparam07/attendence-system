from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1270, height=35)

        # top image 
        img_top = Image.open(r"images\facialrecognition.png")
        img_top = img_top.resize((1270,250),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=37,width=1270,height=340)

         # button
        # b11 = Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue")
        # b11.place(x=0, y=375, width=1270, height=60)
        train_btn = Button(
            self.root,
            width=1270,
            text="Train Data",
            command=self.train_classifier,
            font=("Times New Roman", 18, "bold"),
            bg="blue",
            fg="white",
        )
        train_btn.place(x=0, y=350, width=1270, height=50)

        # bottom image
        img_bottom = Image.open(r"images\facialrecognition.png")
        img_bottom = img_bottom.resize((1270,250),Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y=390,width=1270,height=340)

    # LBPH algorithm is used for face recognition
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # grayscale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            # C:\Users\singh\SEM6\minor project\DATA\user.3.1.jpg
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)


        # ============= Train the classifier ===============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data sets completed!!!")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()