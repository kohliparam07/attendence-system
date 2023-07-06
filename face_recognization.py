# tkinter is used to make the gui
# The tkinter.ttk module provides access to the Tk themed widget set, introduced in Tk 8.5.
from tkinter import*
from tkinter import ttk
# pillow is used to for images
from PIL import Image,ImageTk 
# for image editing
from Student import Student
# from face_recognization import face_recognization
import mysql.connector
import os
import cv2

class face_recognization:
    # call the constructor for creating the window
    # (self, name_of_root_window)
    def __init__(self,root):
        # initialise self
        self.root = root
        # set dimensions of window
        self.root.geometry("1270x650+0+0")
        self.root.title("Attendence Makring System")

        # set background image
        img = Image.open(r"images\back.jpg")
        img = img.resize((1270,650),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # make a label to set image on window
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1270, height=650)

        # attendence button
        attendance_btn_img = Image.open(r"images\student.png")
        attendance_btn_img = attendance_btn_img.resize((200,200),Image.Resampling.LANCZOS)
        self.attendance_btnphotoimg = ImageTk.PhotoImage(attendance_btn_img)
        b3 = Button(bg_img, image=self.attendance_btnphotoimg, cursor="hand2", bg="lightblue",command=self.face_recognize)
        b3.place(x=680, y=100, width=200, height=200)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue", command=self.face_recognize)
        b3_1.place(x=680, y=300, width=200, height=30)


    
    def face_recognize(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
            print("Hello World")
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="Pb022002@",database="face_recognizer")
                mycursor = conn.cursor()
                print("Hello World1")
                mycursor.execute("select Name from student where Student_id="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)

                mycursor.execute("select Roll from student where Student_id="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)
                mycursor.execute("select Dep from student where Student_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)

                # mycursor.execute("select Student_id from student where Student_id="+str(id))
                # i=mycursor.fetchone()
                # i="+".join(i)
                
                if confidence>77:
                    # cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    print("Hello World1 - if")
                    # self.mark_attendence(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    print("Hello World1 - else")
                coord=[x,y,w,y]
            return coord 
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            print("Hello World1- recognise")
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        print("Hello World - 12")
        video_cap=cv2.VideoCapture(0)
        print("Hello World1 - 123")
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==1:
                break
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_recognization(root)
    root.mainloop()




# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# # from time import strftime
# # from datetime import datetime
# import cv2 
# import os
# # import numpy as np

# class face_recognization:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1270x650+0+0")
#         self.root.title("Face Recognition System") 
#          #title
#         title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1270,height=45)
#        #first image
#         # img_top=Image.open(r"images\face_detector1.jpg")
#         # img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
#         # self.photoimg_top=ImageTk.PhotoImage(img_top)
        
#         # f_lbl=Label(self.root,image=self.photoimg_top)
#         # f_lbl.place(x=0,y=45,width=550,height=600)

#         #button
#         # face_btn=Button(self.root, command=self.face_recognize, text="FACE RECOGNITION",cursor="hand2",font=("times new roman",18,"bold"),bg="red",fg="white")
#         # face_btn.place(x=50,y=250,width=300,height=40)
#         b3_1 = Button(self.root, text="Attendance", cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue", command=self.face_recognize)
#         b3_1.place(x=680, y=300, width=200, height=30)

#        #second image
#         # img_bottom=Image.open(r"images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
#         # img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
#         # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
#         # f_lbl=Label(self.root,image=self.photoimg_bottom)
#         # f_lbl.place(x=550,y=45,width=950,height=600)
         
# # ATTENDENCE

# # def mark_attendence(self,i,r,n,d):
# #     with open("yash.csv","r+",newline="\n") as f:
# #         myDataList=f.readlines()
# #         name_list=[]
# #         for line in myDataList:
# #             entry=line.split((","))
# #             name_list.append(entry[0])
# #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
# #             now=datetime.now()
# #             d1=now.strftime("%d/%m/%Y")
# #             dtString=now.strftime("%H:%M:%S")
# #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
                             
           
# # FACE RECOGNITION

# def face_recognize(self):
#     def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#         gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#         coord=[]

#         for (x,y,w,h) in features:
#             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#             id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#             confidence=int((100*(1-predict/300)))

#             conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="Pb022002@",database="face_recognizer")
#             mycursor = conn.cursor()

#             mycursor.execute("select Name from student where Student_id="+str(id))
#             n=mycursor.fetchone()
#             n="+".join(n)

#             mycursor.execute("select Roll from student where Student_id="+str(id))
#             r=mycursor.fetchone()
#             r="+".join(r)

#             mycursor.execute("select Dep from student where Student_id="+str(id))
#             d=mycursor.fetchone()
#             d="+".join(d)

#             mycursor.execute("select Student_id from student where Student_id="+str(id))
#             i=mycursor.fetchone()
#             i="+".join(i)
            
#             if confidence>77:
#                 cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 self.mark_attendence(i,r,n,d)
#             else:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                 cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            
#             coord=[x,y,w,y]
#         return coord 
#     def recognize(img,clf,faceCascade):
#         coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#         return img
#     faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#     clf=cv2.face.LBPHFaceRecognizer_create()
#     clf.read("classifier.xml")

#     video_cap=cv2.VideoCapture(0)

#     while True:
#         ret,img=video_cap.read()
#         img=recognize(img,clf,faceCascade)
#         cv2.imshow("Welcome to face Recognition",img)

#         if cv2.waitKey(1)==13:
#             break
#         video_cap.release()
#         cv2.destroyAllWindows()


# # def generate_dataset(self):
# #         if (
# #             self.var_dep.get() == "Select Department"
# #             or self.var_name.get() == ""
# #             or self.var_id.get() == ""
# #         ):
# #             messagebox.showerror("Error", "All Fields are Required", parent=self.root)
# #         else:
# #             try:
# #                 conn = mysql.connector.connect(
# #                     host="localhost",
# #                     port="3306",
# #                     user="root",
# #                     password="Pb022002@",
# #                     database="face_recognizer",
# #                 )
# #                 mycursor = conn.cursor()
# #                 mycursor.execute("select * from student")
# #                 myresult = mycursor.fetchall()
# #                 id = 0
# #                 for x in myresult:
# #                     id+=1
# #                 mycursor.execute(
# #                     "update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Student_id = %s, Name = %s, Division = %s, Roll  = %s, Gender = %s, DOB = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s, PhotoSample = %s where Student_ID = %s",
# #                     (
# #                         self.var_dep.get(),
# #                         self.var_course.get(),
# #                         self.var_year.get(),
# #                         self.var_sem.get(),
# #                         self.var_id.get(),
# #                         self.var_name.get(),
# #                         self.var_div.get(),
# #                         self.var_roll.get(),
# #                         self.var_gender.get(),
# #                         self.var_dob.get(),
# #                         self.var_email.get(),
# #                         self.var_phone.get(),
# #                         self.var_address.get(),
# #                         self.var_teacher.get(),
# #                         self.var_radio1.get(),
# #                         self.var_id.get() == id+1
# #                     )
# #                 )
# #                 conn.commit()
# #                 self.fetch_data()
# #                 self.reset_data()
# #                 conn.close()


# #                 # ================= load predefinded data on face frontals from opencv ==================
# #                 face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #                 def face_cropped(img):
# #                     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #                     faces = face_classifier.detectMultiScale(gray,1.3,5)

# #                     for(x,y,w,h) in faces:
# #                         face_cropped = img[y:y+h,x:x+w]
# #                         return face_cropped
                
# #                 cap = cv2.VideoCapture(0)
# #                 img_id = 0
# #                 while True:
# #                     ret,my_frame = cap.read()
# #                     if face_cropped(my_frame) is not None:
# #                         img_id+=1
# #                         face = cv2.resize(face_cropped(my_frame),(450,450))
# #                         face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
# #                         file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
# #                         cv2.imwrite(file_name_path,face)
# #                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
# #                         cv2.imshow("Cropped face",face)

# #                     if cv2.waitKey(1)==13 or int(img_id)==100:
# #                         break
# #                 cap.release()
# #                 cv2.destroyAllWindows()
# #                 messagebox.showinfo("Result","Generating data sets completed!!!")
# #             except Exception as es:
# #                 messagebox.showerror("Error", "Due to: {str(es)}", parent=self.root)


# if __name__=="__main__":
#     root=Tk()
#     obj=face_recognization(root)
#     root.mainloop()
        