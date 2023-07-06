from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recognition System")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_sem = StringVar()

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=0, y=100, relwidth=100.00, height=500)

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("Times New Roman", 12, "bold"),
        )
        Left_frame.place(x=2, y=10, width=650, height=480)

        Current_course = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("Times New Roman", 12, "bold"),
        )
        Current_course.place(x=10, y=10, width=630, height=120)

        Dep_Label = Label(
            Current_course,
            bd=2,
            text="Department",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Dep_Label.grid(row=0, column=0, padx=10)

        Dep_Combo = ttk.Combobox(
            Current_course,
            textvariable=self.var_dep,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Dep_Combo["values"] = (
            "Select Department",
            "CSE",
            "IT",
            "Civil",
            "Mechanical",
            "Chemical",
            "ICE",
        )
        Dep_Combo.current(0)
        Dep_Combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Dep_Label.place(x=10, y=10, width=650, height=400)

        Course_Label = Label(
            Current_course,
            bd=2,
            text="Course",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Course_Label.grid(row=0, column=2, padx=10)

        Course_Combo = ttk.Combobox(
            Current_course,
            textvariable=self.var_course,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Course_Combo["values"] = (
            "Select Course",
            "CSE",
            "IT",
            "Civil",
            "Mechanical",
            "Chemical",
            "ICE",
        )
        Course_Combo.current(0)
        Course_Combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        Year_Label = Label(
            Current_course,
            bd=2,
            text="Year",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Year_Label.grid(row=1, column=0, padx=10)

        Year_Combo = ttk.Combobox(
            Current_course,
            textvariable=self.var_year,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Year_Combo["values"] = (
            "Select Year",
            "1",
            "2",
            "3",
            "4",
        )
        Year_Combo.current(0)
        Year_Combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        Semester_Label = Label(
            Current_course,
            bd=2,
            text="Semester",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Semester_Label.grid(row=1, column=2, padx=10)

        Semester_Combo = ttk.Combobox(
            Current_course,
            textvariable=self.var_sem,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Semester_Combo["values"] = (
            "Select Year",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
        )
        Semester_Combo.current(0)
        Semester_Combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        Class_Student_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Class Student Information",
            font=("Times New Roman", 12, "bold"),
        )
        Class_Student_frame.place(x=10, y=140, width=630, height=310)

        StudentID_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Student ID:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        StudentID_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_id,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        StudentName_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Student Name:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        StudentName_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_name,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        StudentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Div_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Class Division:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Div_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Div_Combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_div,
            width=16,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Div_Combo["values"] = ("A", "B", "Other")
        Div_Combo.current(0)
        Div_Combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        RollNo_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Roll No.:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        RollNo_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        RollNo_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_roll,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        RollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Gender_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Gender:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Gender_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        Gender_Combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_gender,
            width=16,
            font=("Times New Roman", 12, "bold"),
            state="read only",
        )
        Gender_Combo["values"] = ("Male", "Female", "Other")
        Gender_Combo.current(0)
        Gender_Combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        DOB_Label = Label(
            Class_Student_frame,
            bd=2,
            text="DOB:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        DOB_Label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_dob,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Email_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Email Address:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Email_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_email,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        PhoneNo_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Phone No.:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        PhoneNo_Label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        PhoneNo_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_phone,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        PhoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        Address_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Address:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Address_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_address,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        Teacher_Label = Label(
            Class_Student_frame,
            bd=2,
            text="Teacher Name:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Teacher_Label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_teacher,
            width=18,
            font=("Times New Roman", 12, "bold"),
        )
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_radio1,
            text="No Photo Sample",
            value="No",
        )
        radiobtn2.grid(row=6, column=1)

        Btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        Btn_frame1.place(x=4, y=205, width=618, height=35)

        savebtn = Button(
            Btn_frame1,
            width=16,
            text="Save",
            command=self.add_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        savebtn.grid(row=0, column=0)

        updatebtn = Button(
            Btn_frame1,
            width=16,
            text="Update",
            command=self.update_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        updatebtn.grid(row=0, column=1)

        deletebtn = Button(
            Btn_frame1,
            width=16,
            text="Delete",
            command=self.delete_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        deletebtn.grid(row=0, column=2)

        resetbtn = Button(
            Btn_frame1,
            width=16,
            text="Reset",
            command=self.reset_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        resetbtn.grid(row=0, column=3)

        Btn_frame2 = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        Btn_frame2.place(x=4, y=240, width=618, height=35)

        takephotobtn = Button(
            Btn_frame2,
            command=self.generate_dataset,
            width=33,
            text="Take Photo",
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        takephotobtn.grid(row=0, column=0)

        updatephotobtn = Button(
            Btn_frame2,
            width=34,
            text="Update Photo",
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        updatephotobtn.grid(row=0, column=1)

        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("Times New Roman", 12, "bold"),
        )
        Right_frame.place(x=660, y=10, width=600, height=480)

        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search System",
            font=("Times New Roman", 12, "bold"),
        )
        Search_frame.place(x=10, y=10, width=580, height=80)

        Search_Label = Label(
            Search_frame,
            bd=2,
            text="Search By:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        Search_Label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        Search_Combo = ttk.Combobox(
            Search_frame, font=("Times New Roman", 12, "bold"), state="read only"
        )
        Search_Combo["values"] = (
            "Select",
            "Roll No",
            "Phone No",
        )
        Search_Combo.current(0)
        Search_Combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(
            Search_frame, width=10, font=("Times New Roman", 12, "bold")
        )
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        searchbtn = Button(
            Search_frame,
            width=9,
            text="Search",
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        searchbtn.grid(row=0, column=3, padx=1)

        showAllbtn = Button(
            Search_frame,
            width=9,
            text="Show All",
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        showAllbtn.grid(row=0, column=4, padx=1)

        Table_frame = LabelFrame(
            Right_frame,
            bd=2,
            relief=RIDGE,
        )
        Table_frame.place(x=10, y=100, width=580, height=350)

        scrollX = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_frame, column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.Student_table.xview)
        scrollY.config(command=self.Student_table.yview)

        self.Student_table.heading("dep", text="Department")
        self.Student_table.heading("course", text="Course")
        self.Student_table.heading("year", text="Year")
        self.Student_table.heading("sem", text="Semester")
        self.Student_table.heading("id", text="StudentID")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("div", text="Division")
        self.Student_table.heading("roll", text="RollNo")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("phone", text="PhoneNo")
        self.Student_table.heading("address", text="Address")
        self.Student_table.heading("teacher", text="Teacher")
        self.Student_table.heading("photo", text="PhotoSampleStatus")
        self.Student_table["show"] = "headings"

        self.Student_table.column("dep", width=100)
        self.Student_table.column("course", width=100)
        self.Student_table.column("year", width=100)
        self.Student_table.column("sem", width=100)
        self.Student_table.column("id", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("div", width=100)
        self.Student_table.column("roll", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("phone", width=100)
        self.Student_table.column("address", width=100)
        self.Student_table.column("teacher", width=100)
        self.Student_table.column("photo", width=100)

        self.Student_table.pack(fill=BOTH, expand=1)

        self.Student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="Pb022002@", database="face_recognizer")
                mycursor = conn.cursor()
                mycursor.execute(
                    "insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student added successfully", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", "Due To:" + str(es), parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Pb022002@",
            database="face_recognizer",
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.Student_table.focus()
        content = self.Student_table.item(cursor_focus)

        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[10])
        self.var_email.set(data[9])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update",
                    "Do you want to update student details ?",
                    parent=self.root,
                )
                if update > 0:
                    conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="Pb022002@",database="face_recognizer")
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Student_id = %s, Name = %s, Division = %s, Roll  = %s, Gender = %s, DOB = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_ID = %s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_id.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_id.get()
                        )
                    )
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student details Updated", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete",
                    "Do you want to delete this student record ?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        port="3306",
                        user="root",
                        password="Pb022002@",
                        database="face_recognizer",
                    ) 
                    mycursor = conn.cursor()
                    sql = "delete from student where Student_ID = %s"
                    val = (self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student record deleted", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ======================== generate dataset or take photo samples ===========================
    # haarcascade is used for face detection
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="Pb022002@",
                    database="face_recognizer",
                )
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                mycursor.execute(
                    "update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Student_id = %s, Name = %s, Division = %s, Roll  = %s, Gender = %s, DOB = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_ID = %s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get() == id+1
                    )
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ================= load predefinded data on face frontals from opencv ==================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", "Due to: {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
