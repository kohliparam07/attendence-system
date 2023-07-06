# # tkinter is used to make the gui
# # The tkinter.ttk module provides access to the Tk themed widget set, introduced in Tk 8.5.
# from tkinter import*
# from tkinter import ttk
# # pillow is used to for images
# from PIL import Image,ImageTk 
# # for image editing
# from Student import Student
# # from face_recognization import face_recognization
# from time import strftime
# from datetime import datetime
# import mysql.connector
# import os
# import cv2

# class face_recognization:
#     # call the constructor for creating the window
#     # (self, name_of_root_window)
#     def __init__(self,root):
#         # initialise self
#         self.root = root
#         # set dimensions of window
#         self.root.geometry("1270x650+0+0")
#         self.root.title("Attendence Makring System")

#         # set background image
#         img = Image.open(r"images\back.jpg")
#         img = img.resize((1270,650),Image.Resampling.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#         # make a label to set image on window
#         bg_img = Label(self.root, image=self.photoimg)
#         bg_img.place(x=0, y=0, width=1270, height=650)

#         # attendence button
#         attendance_btn_img = Image.open(r"images\student.png")
#         attendance_btn_img = attendance_btn_img.resize((200,200),Image.Resampling.LANCZOS)
#         self.attendance_btnphotoimg = ImageTk.PhotoImage(attendance_btn_img)
#         b3 = Button(bg_img, image=self.attendance_btnphotoimg, cursor="hand2", bg="lightblue",command=self.face_recognize)
#         b3.place(x=680, y=100, width=200, height=200)
#         b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman",12,"bold"), bg="lightblue", command=self.face_recognize)
#         b3_1.place(x=680, y=300, width=200, height=30)



#     # ================ attendance ========================
#     # ATTENDENCE

#     def mark_attendence(self,i,r,n,d):
#         with open("yash.csv","r+",newline="\n") as f:
#             myDataList=f.readlines()
#             name_list=[]
#             for line in myDataList:
#                 entry=line.split((","))
#                 name_list.append(entry[0])
#             if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
#                 now=datetime.now()
#                 d1=now.strftime("%d/%m/%Y")
#                 dtString=now.strftime("%H:%M:%S")
#                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
    
#     def face_recognize(self):
#         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)

#             coord=[]

#             for (x,y,w,h) in features:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict=clf.predict(gray[y:y+h,x:x+w])
#                 confidence=int((100*(1-predict/300)))

#                 conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="Pb022002@",database="face_recognizer")
#                 mycursor = conn.cursor()

#                 mycursor.execute("select Name from student where Student_id="+str(id))
#                 n=mycursor.fetchone()
#                 n="+".join(n)

#                 mycursor.execute("select Roll from student where Student_id="+str(id))
#                 r=mycursor.fetchone()
#                 r="+".join(r)

#                 mycursor.execute("select Dep from student where Student_id="+str(id))
#                 d=mycursor.fetchone()
#                 d="+".join(d)

#                 mycursor.execute("select Student_id from student where Student_id="+str(id))
#                 i=mycursor.fetchone()
#                 i="+".join(i)
                
#                 if confidence>77:
#                     cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                     self.mark_attendence(i,r,n,d)
#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
#                 coord=[x,y,w,y]
#             return coord 
#         def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap=cv2.VideoCapture(0)

#         while True:
#             ret,img=video_cap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Welcome to face Recognition",img)

#             # if cv2.waitKey(1)==1:
#             #     break
#             cv2.waitKey(5000)
#             video_cap.release()
#             cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = Tk()
#     obj = face_recognization(root)
#     root.mainloop()



import cv2
import numpy as np
# import pyttsx3
import face_recognition
import os
# from pyfirmata import Arduino
path = 'data'
#board = Arduino('COM7')
images = []
names = []
myList = os.listdir(path)
print(myList)
for mem in myList:
    curimg=cv2.imread(f'{path}/{mem}')
    images.append(curimg)
    names.append(os.path.splitext(mem)[0])
print(names)


# engine = pyttsx3.init()

# print(engine.getProperty('volume'))
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodings = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

#this is for arduino , not necessary

 #   board.digital[9].write(0)
  #  board.digital[11].write(0)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodings,encodeFace)
        faceDis = face_recognition.face_distance(encodings,encodeFace)
        matchIndex = np.argmin(faceDis)

        print(faceDis)
        # when program will detect face it will greet him/her

        if matches[matchIndex]:
            name = names[matchIndex]
            y1,x2,y2,x1= faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
            # engine.say("Hello"+name)
            # engine.runAndWait()
        
    cv2.imshow('camera',img)
    cv2.waitKey(1)