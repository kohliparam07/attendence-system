# tkinter is used to make the gui
# The tkinter.ttk module provides access to the Tk themed widget set, introduced in Tk 8.5.
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# pillow is used to for images
from PIL import Image,ImageTk
# for image editing
from Student import Student
from temp import face_recognization
from train import Train
from developer import Developer
from help import Help
import os

class faceRecogSystem:
    # call the constructor for creating the window
    # (self, name_of_root_window)
    def __init__(self,root):
        # initialise self
        self.root = root
        # set dimensions of window
        self.root.geometry("1270x650+0+0")
        self.root.title("Attendence Makring System")

        # set background image
        img = Image.open(r"images\dev.jpg")
        img = img.resize((1270,650),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # make a label to set image on window
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1270, height=650)

        # student button
        student_btn_img = Image.open(r"images\gettyimages-1022573162.jpg")
        student_btn_img = student_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.student_btnphotoimg = ImageTk.PhotoImage(student_btn_img)
        b1 = Button(bg_img, image=self.student_btnphotoimg, command=self.student_details, cursor="hand2", bg="lightblue")
        b1.place(x=100, y=100, width=200, height=200)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue")
        b1_1.place(x=100, y=300, width=200, height=30)

        # detect face button
        detect_face_btn_img = Image.open(r"images\face_detector1.jpg")
        detect_face_btn_img = detect_face_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.detect_face_btnphotoimg = ImageTk.PhotoImage(detect_face_btn_img)
        b2 = Button(bg_img, image=self.detect_face_btnphotoimg, cursor="hand2", bg="lightblue",command=self.face_data)
        b2.place(x=390, y=100, width=200, height=200)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman",12,"bold"), bg="lightblue")
        b2_1.place(x=390, y=300, width=200, height=30)

        # attendence button
        attendance_btn_img = Image.open(r"images\bg1.jpg")
        attendance_btn_img = attendance_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.attendance_btnphotoimg = ImageTk.PhotoImage(attendance_btn_img)
        b3 = Button(bg_img, image=self.attendance_btnphotoimg, cursor="hand2", bg="lightblue")
        b3.place(x=680, y=100, width=200, height=200)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue")
        b3_1.place(x=680, y=300, width=200, height=30)

        # helpdesk button
        helpdesk_btn_img = Image.open(r"images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        helpdesk_btn_img = helpdesk_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.helpdesk_btnphotoimg = ImageTk.PhotoImage(helpdesk_btn_img)
        b4 = Button(bg_img, image=self.helpdesk_btnphotoimg, cursor="hand2", bg="lightblue", command=self.help_data)
        b4.place(x=970, y=100, width=200, height=200)
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman",12,"bold"), bg="lightblue")
        b4_1.place(x=970, y=300, width=200, height=30)

        # tain data button
        train_btn_img = Image.open(r"images\di.jpg")
        train_btn_img = train_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.train_btnphotoimg = ImageTk.PhotoImage(train_btn_img)
        b5 = Button(bg_img, image=self.train_btnphotoimg, cursor="hand2", bg="lightblue", command=self.train_data)
        b5.place(x=100, y=380, width=200, height=200)
        b5_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman",12,"bold"), bg="lightblue")
        b5_1.place(x=100, y=580, width=200, height=30)

        # photos button
        photos_btn_img = Image.open(r"images\opencv_face_reco_more_data.jpg")
        photos_btn_img = photos_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.photos_btnphotoimg = ImageTk.PhotoImage(photos_btn_img)
        b6 = Button(bg_img, image=self.photos_btnphotoimg, cursor="hand2", command=self.open_img, bg="lightblue")
        b6.place(x=390, y=380, width=200, height=200)
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman",12,"bold"), bg="lightblue")
        b6_1.place(x=390, y=580, width=200, height=30)

        # hdeveloper button
        developer_btn_img = Image.open(r"images\developer.jpg")
        developer_btn_img = developer_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.developer_btnphotoimg = ImageTk.PhotoImage(developer_btn_img)
        b7 = Button(bg_img, image=self.developer_btnphotoimg, cursor="hand2", bg="lightblue", command=self.developer_data)
        b7.place(x=680, y=380, width=200, height=200)
        b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman",12,"bold"), bg="lightblue")
        b7_1.place(x=680, y=580, width=200, height=30)

        # exit button
        exit_btn_img = Image.open(r"images\exit.jpg")
        exit_btn_img = exit_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.exit_btnphotoimg = ImageTk.PhotoImage(exit_btn_img)
        b8 = Button(bg_img, image=self.exit_btnphotoimg, cursor="hand2", bg="lightblue", command=self.iExit)
        b8.place(x=970, y=380, width=200, height=200)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman",12,"bold"), bg="lightblue")
        b8_1.place(x=970, y=580, width=200, height=30)


    def open_img(self):
        os.startfile("data")
        


        # =================== function button ========================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognization(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def iExit(self):
        self.iExit = messagebox.askyesno(
            "Face Recognization", "Are you sure to exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


 
if __name__ == "__main__":
    root = Tk()
    obj = faceRecogSystem(root)
    root.mainloop()