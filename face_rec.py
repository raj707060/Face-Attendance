from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Rec:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label( self.root, text="Face_Rec", font=("times new roman", 35, "bold"),bg="white",fg="burlywood")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        #---- first image
        img_top = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\facial-recogni.jpg.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        
        #----2nd image
        img_bottum = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\scanner2.webp")
        img_bottum= img_bottum.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottum = ImageTk.PhotoImage(img_bottum)
        
        f_lbl = Label(self.root,image=self.photoimg_bottum)
        f_lbl.place(x=650, y=55, width=950, height=700)
        #-----face recognition button
        b1_1=Button(f_lbl,text="Face_Rec",cursor="hand2",font=("time new roman",18,"bold"),bg ="darkgreen", fg="red")
        b1_1.place(x=365,y=620,width=200,height=40)
        
    #------ mark attendance---
    def mark_attendance(self, name, roll, dep):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((name not in name_list) and (roll not in name_list) and (dep not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{name},{roll},{dep},{dtString},{d1},Present")
    
        
    #----face recognition----
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
 
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                
                # if confidence > 77:

                conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                

                if confidence > 77:
                    cv2.putText(img, f"Name:{n}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    self.mark_attendance(n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        facecascade = cv2.cascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, facecascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13: #13 is the Enter Key
                break
            
            video_cap.release()
            cv2.destroyAllWindows()
            
            
if __name__ == "__main__":
    root = Tk()
    app =Face_Rec(root)
    root.mainloop()  