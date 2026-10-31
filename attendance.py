from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import mysql.connector
import cv2
import os
import csv

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #===================variables=================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        # ================= HEADER IMAGES =================
        img = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\portrait.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\group-stu.avif")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=800, y=0, width=800, height=200)

        # ================= BACKGROUND =================
        img3 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\rkumr.png")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # ================= TITLE =================
        title_lbl = Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=60, width=1480, height=600)

        # ================= LEFT FRAME =================
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold")
        )
        left_frame.place(x=10, y=10, width=720, height=560)

        img_left = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\portrait.jpg")
        img_left = img_left.resize((700, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=10, y=0, width=700, height=130)

        left_inside = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside.place(x=10, y=140, width=700, height=380)

        # ================= FORM =================
        #==attendance id====
        attendance_id_label = Label(left_inside, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        attendance_id_entry = ttk.Entry(left_inside, textvariable=self.var_atten_id, width=20, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        # ===roll====
        roll_label = Label(left_inside, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        roll_entry = ttk.Entry(left_inside, textvariable=self.var_atten_roll, width=20, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        #=====name====
        name_label = Label(left_inside, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside, textvariable=self.var_atten_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        #=====department====
        dep_label = Label(left_inside, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        dep_entry = ttk.Entry(left_inside, textvariable=self.var_atten_dep, width=20, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        #=====time====
        time_label = Label(left_inside, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside, textvariable=self.var_atten_time, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        #=====date====
        date_label = Label(left_inside, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside, textvariable=self.var_atten_date, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)
        #====status====
        status_label = Label(left_inside, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        status_label.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        status_combo = ttk.Combobox(left_inside, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly", width=18)
        status_combo["values"] = ("Status", "Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=6, column=1, padx=10, pady=5, sticky=W)
        

        # ================= BUTTONS =================
        btn_frame = Frame(left_inside, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=710, height=40)

        Button(btn_frame, text="Import CSV", command=self.import_csv,width=17, font=("times new roman", 13, "bold"),bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV",command=self.export_csv, width=17, font=("times new roman", 13, "bold"),bg="green", fg="white").grid(row=0, column=1)

        Button(btn_frame, text="Update",width=17, font=("times new roman", 13, "bold"),bg="red", fg="white").grid(row=0, column=2)

        Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("times new roman", 13, "bold"), bg="orange", fg="white").grid(row=0, column=3)

        # ================= RIGHT FRAME =================
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=720, height=560)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=700, height=480)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview( table_frame,columns=("attendance id", "roll", "department", "name", "date", "time", "status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        for col in ("attendance id", "roll", "department", "name", "date", "time", "status"):
            self.attendance_table.heading(col, text=col.title())
            self.attendance_table.column(col, width=100)

        self.attendance_table["show"] = "headings"
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # ================= METHODS =================
    def fetchData(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for row in rows:
            self.attendance_table.insert("", END, values=row)
    #================= import csv=========
    def import_csv(self):
        global mydata
        mydata.clear()

        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root
        )

        if fln == "":
            return

        with open(fln, newline="") as myfile:
            csvread = csv.reader(myfile)
            for row in csvread:
                mydata.append(row)

        self.fetchData(mydata)
        
    #=====================export csv=========
    def export_csv(self):
        if len(mydata) < 1:
            messagebox.showerror("No Data", "No data found to export", parent=self.root)
            return

        fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root
        )

        if fln == "":
            return

        with open(fln, mode="w", newline="") as myfile:
            csvwrite = csv.writer(myfile)
            for row in mydata:
                csvwrite.writerow(row)

        messagebox.showinfo("Data Exported", f"Data exported successfully to {fln}", parent=self.root)
        
    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        data = content["values"]

        self.var_atten_id.set(data[0])
        self.var_atten_roll.set(data[1])
        self.var_atten_dep.set(data[2])
        self.var_atten_name.set(data[3])
        self.var_atten_date.set(data[4])
        self.var_atten_time.set(data[5])
        self.var_atten_attendance.set(data[6])
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        

      
    

# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
