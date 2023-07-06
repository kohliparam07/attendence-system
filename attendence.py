from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recognition System")

#first image
        img1=Image.open(r"images\smart-attendance.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=635,height=200)
       #second image
        img2=Image.open(r"images\face-recognition.png")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=700,y=0,width=635,height=200)

 
        img3=Image.open(r"images\gettyimages-1022573162.jpg")
        img3=img3.resize((1270,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1270,height=650)

        title_lbl=Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1270,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=20,width=1240,height=700)

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="STUDEMT ATTENDENCE DETAILS",
            font=("Times New Roman", 12, "bold"),
        )
        Left_frame.place(x=2, y=10, width=650, height=480)
        
        
        img_left=Image.open(r"images\iStock-182059956_18390_t12.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=650,height=300)


# attendence id

        attendanceId_label = Label(
            left_inside_frame,
            bd=2,
            text="Attendence ID:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(
            left_inside_frame,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        StudentName_Label = Label(
            left_inside_frame,
            bd=2,
            text=" ROLL: ",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        StudentName_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(
            left_inside_frame,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        StudentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        # RollNo_Label = Label(
        #     left_inside_frame,
        #     bd=2,
        #     text="NAME.:",
        #     font=("Times New Roman", 12, "bold"),
        #     bg="white",
        # )
        # RollNo_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        # RollNo_entry = ttk.Entry(
        #     left_inside_frame,
        #     width=18,
        #     font=("Times New Roman", 12, "bold"),
        # )
        # RollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # DOB_Label = Label(
        #    left_inside_frame,
        #     bd=2,
        #     text="DOB:",
        #     font=("Times New Roman", 12, "bold"),
        #     bg="white",
        # )
        # DOB_Label.grid(row=2, column=0, padx=0, pady=5, sticky=W)

        # DOB_entry = ttk.Entry(
        #     left_inside_frame,
        #     width=18,
        #     font=("Times New Roman", 12, "bold"),
        # )
        # DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Email_Label = Label(
            left_inside_frame,
            bd=2,
            text="Email Address:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Email_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(
            left_inside_frame,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        PhoneNo_Label = Label(
            left_inside_frame,
            bd=2,
            text="Phone No.:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        PhoneNo_Label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        PhoneNo_entry = ttk.Entry(
            left_inside_frame,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        PhoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        Address_Label = Label(
           left_inside_frame,
            bd=2,
            text="Address:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Address_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(
            left_inside_frame,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        attendanceLabel=Label(left_inside_frame,text="ATTENDENCE STATUS",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=5,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=5,column=1,pady=0)
        self.atten_status.current(0)

        Btn_frame1 = Frame(left_inside_frame, bd=2, relief=RIDGE)
        Btn_frame1.place(x=4, y=205, width=618, height=35)

        savebtn = Button(
            Btn_frame1,
            width=16,
            text="Import csv",
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        savebtn.grid(row=0, column=0)

        updatebtn = Button(
            Btn_frame1,
            width=16,
            text="Export csv",
            # command=self.update_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        updatebtn.grid(row=0, column=1)

        deletebtn = Button(
            Btn_frame1,
            width=16,
            text="Update",
            
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        deletebtn.grid(row=0, column=2)

        resetbtn = Button(
            Btn_frame1,
            width=16,
            text="Reset",
            # command=self.reset_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        resetbtn.grid(row=0, column=3)


        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="ATTENDENCE DETAILS",
            font=("Times New Roman", 12, "bold"),
        )
        Right_frame.place(x=660, y=10, width=700, height=480)

        table_frame1 = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame1.place(x=4, y=5, width=670, height=400)

        #scroll bar table
        scoll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scoll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame1,columns={"id","roll","name","dep","time","date"},xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)
        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)

        scoll_x.config(command=self.AttendanceReportTable.xview)
        scoll_y.config(command=self.AttendanceReportTable.yview)
        

        # self.AttendanceReportTable.heading("id",text="Attendance ID")
        # self.AttendanceReportTable.heading("roll",text="ROLL")
        # self.AttendanceReportTable.heading("name",text="NAME")
        # self.AttendanceReportTable.heading("dep",text="DEPARTMENT")
        # self.AttendanceReportTable.heading("time",text="TIME")
        # self.AttendanceReportTable.heading("date",text="DATE")

        # self.AttendanceReportTable["show"]="headings"
        # self.AttendanceReportTable.column("id",width=100)
        # self.AttendanceReportTable.column("roll",width=100)
        # self.AttendanceReportTable.column("name",width=100)
        # self.AttendanceReportTable.column("dep",width=100)
        # self.AttendanceReportTable.column("time",width=100)
        # self.AttendanceReportTable.column("date",width=100)

        # self.AttendanceReportTable.pack(fill=BOTH,expand=1)


    

if __name__ == "__main__":
    root = Tk()
    obj = attendence(root)
    root.mainloop()
