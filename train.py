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
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label( self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\face.jpeg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        #-----Train data button
        b1_1=Button(self. root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("time new roman",30,"bold"),bg ="black", fg="red")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        img_bottum = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\face.jpeg")
        img_bottum= img_bottum.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottum = ImageTk.PhotoImage(img_bottum)
        
        f_lbl = Label(self.root,image=self.photoimg_bottum)
        f_lbl.place(x=0, y=440, width=1530, height=325)
        
        
    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!", parent=self.root)
            return
        # path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for file in os.listdir(data_dir):
            filepath = os.path.join(data_dir, file)
            
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
               parts = file.split('.')
               
               if len(parts) >= 3 and parts[1].isdigit():
                  id = int(parts[1])
                  
                  img = Image.open(filepath).convert('L')
                  imageNp = np.array(img, 'uint8')
                
                  faces.append(imageNp)
                  ids.append(id)
                
                  cv2.imshow("Training", imageNp)
                  cv2.waitKey(1)
                  
               else:
                   print(f"Skipping invalid file: {file}")
                   
                   
            if len(faces) == 0:
                messagebox.showerror("Error", "No valid images found for training.", parent=self.root)
                return

        

        ids = np.array(ids)

        # ===== Train the classifier and save =====
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)
        
        
            
            
        






if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()        