from tkinter import *
from tkinter import ttk
import tkinter
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
from Student import Student
import os
from train import Train
from face_rec import Face_Rec
from attendance import Attendance
from developer import Developer
from help import Help
from chatbot import SmartAttendanceChatbot




class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # --- First Image ---
        img = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\IMG.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        # --- Second Image ---
        img1 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\scanner2.webp")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)
        
        # --- Third Image ---
        img2 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\image.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)
        
        # --- Background Image ---
        img3 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\rkumr.png")
        img3 = img3.resize((1530, 730), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=730)
        
        # --- Title Label ---
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        #=================time table=================
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), bg="white", fg="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()
        
        
        #student button
        img4 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\Students.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        # face Detector BUtton
        img5 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\face-recog.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        # Attendance Face button
        img6 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\pcface.webp")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attenance_data)
        b1.place(x=800, y=100, width=220, height=220)
        
        b1_1=Button(bg_img,text="Attendance Face",cursor="hand2",command=self.attenance_data,font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        # Help Face BUTTON
        # img7 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\help-desk.jpg")
        # img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        # self.photoimg7 = ImageTk.PhotoImage(img7)
        
        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        # b1.place(x=1100, y=100, width=220, height=220)
        
        # b1_1=Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_data,font=("time new roman",15,"bold"),bg ="black", fg="red")
        # b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        # Train data BUTTON
        img8 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\what.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        # Photo data BUTTON
        img9 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\happy-g.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)
        
        b1_1=Button(bg_img,text="Photo ",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        
        # Developer data BUTTON
        img10 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\image5-1.png")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)
        
        b1_1=Button(bg_img,text="Developer ",cursor="hand2",command=self.developer_data,font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
        # Exit data BUTTON
        img11 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\pngtree-exit (2).png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1100, y=380, width=220, height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("time new roman",15,"bold"),bg ="black", fg="red")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return    
        
    # ===========================function buttons=========================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Train(self.new_window)
        
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Face_Rec(self.new_window)
        
        
        
    def attenance_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Developer(self.new_window)
        
        
    def chatbot_data(self):
        self.new_window = Toplevel(self.root)
        self.app =SmartAttendanceChatbot(self.new_window)
        
        
    # def help_data(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app =Help(self.new_window)

    
           
        
        
  
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
