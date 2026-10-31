from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #=================== variables =========================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll_no = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone_no = StringVar()
        self.var_address = StringVar()
        self.var_teacher_name = StringVar()
        self.var_radio1 = StringVar()
        
        # --- First Image ---
        img = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\sengunthar.jpg")
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
        img2 = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\diverse.jpg")
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
            text="STUDENTS MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)
        
        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)
        
        img_left = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\portrait.jpg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        # current course information
        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=135, width=720, height=125)
        
        # Department
        dep_label = Label(Current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Civil", "Mechanical", "EEE", "ECE", "MBA", "Cyber Security")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        # Course name
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=2, sticky=W)
        
        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "BE", "FE", "SE", "TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        # Year
        year_label = Label(Current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2023-2024", "2024-2025", "2025-2026", "2026-2027")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        # Semester
        semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        
        semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        # Class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)
        
        # Student ID
        studentid_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Student name
        studentname_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Class division 
        classdiv_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        classdiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
        div_combo["values"] = ("Select Division", "A", "B", "C", "D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # Roll No 
        Rollno_label = Label(class_student_frame, text="Roll NO:", font=("times new roman", 13, "bold"), bg="white")
        Rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        Rollno_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no, width=20, font=("times new roman", 13, "bold"))
        Rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        # Gender 
        Gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gen, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # DOB
        DOB_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # Email
        Email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Phone No
        PhoneNo_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        PhoneNo_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        PhoneNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone_no, width=20, font=("times new roman", 13, "bold"))
        PhoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Address
        Address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        # Teacher Name
        TeacherName_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        TeacherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        TeacherName_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher_name, width=20, font=("times new roman", 13, "bold"))
        TeacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        # Radio Button
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)
        
        # Button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=200, width=710, height=40)
        
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=3, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1, padx=3, pady=5)
        
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=3, pady=5)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3, padx=3, pady=5)
        
        # Second button frame for photo operations
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=245, width=710, height=35)
        
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=34, font=("times new roman", 12, "bold"), bg="purple", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=5, pady=3)
        
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", command=self.generate_dataset, width=34, font=("times new roman", 12, "bold"), bg="brown", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=5, pady=3)
        
        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        img_right = Image.open(r"C:\Users\rayra\OneDrive\Desktop\Face Attendance\college_images\friends-enjoying.jpg")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        # ================= Search System ===========
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)
        
        search_label = Label(search_frame, text="Search by:", font=("times new roman", 13, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        self.search_var = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.search_var, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No", "Student_ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        self.search_entry_var = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_entry_var, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn = Button(search_frame, text="Search", command=self.search_data, width=12, font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_btn.grid(row=0, column=3)
        
        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data, width=12, font=("times new roman", 12, "bold"), bg="red", fg="white")
        showAll_btn.grid(row=0, column=4)
        
        # ============== table frame ============
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        
        self.fetch_data()

    # ================ Function to add data ================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll_no.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone_no.get(),
                    self.var_address.get(),
                    self.var_teacher_name.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
    # ================ Fetch data ===============
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
        
    # ================ Get cursor ================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if not data:
            return

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gen.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone_no.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher_name.set(data[13])
        self.var_radio1.set(data[14])

    # ================ Update data ================
    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                        Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                        Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                        Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll_no.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone_no.get(),
                        self.var_address.get(),
                        self.var_teacher_name.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ================ Delete data ================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE Student_id=%s", (self.var_std_id.get(),))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                    self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ================ Reset data ================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll_no.set("")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_teacher_name.set("")
        self.var_radio1.set("")

    # ================ Search data ================
    def search_data(self):
        if self.search_var.get() == "Select" or self.search_entry_var.get() == "":
            messagebox.showerror("Error", "Select search criteria and enter value", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                my_cursor = conn.cursor()
                
                if self.search_var.get() == "Roll_No":
                    my_cursor.execute("SELECT * FROM student WHERE Roll=%s", (self.search_entry_var.get(),))
                elif self.search_var.get() == "Phone_No":
                    my_cursor.execute("SELECT * FROM student WHERE Phone=%s", (self.search_entry_var.get(),))
                elif self.search_var.get() == "Student_ID":
                    my_cursor.execute("SELECT * FROM student WHERE Student_id=%s", (self.search_entry_var.get(),))
                
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Info", "No record found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                

    # ================ Photo Sample Functions ================
    
    def take_photo_sample(self):
        messagebox.showinfo("Info", "Take Photo Sample functionality will be implemented", parent=self.root)

    def update_photo_sample(self):
        messagebox.showinfo("Info", "Update Photo Sample functionality will be implemented", parent=self.root)
        
    #=====================generate dataset or take photo sample==========================
    def generate_dataset(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Rajkumar7070@", database="rajdb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                        UPDATE student SET 
                        Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                        Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                        Teacher=%s, PhotoSample=%s 
                        WHERE student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll_no.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone_no.get(),
                        self.var_address.get(),
                        self.var_teacher_name.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 
                
                #=====  load predefined data on face frane===========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_croppend(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        return img[y:y+h,x:x+w]
                    return None
                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,my_Frame=cap.read()
                    if not ret:
                        continue
                    face=face_croppend(my_Frame)
                    if face is not None:
                        img_id+=1
                        face=cv2.resize(face,(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(self.var_std_id.get())+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
                        
            
                    
                    
                    
            
                    
                                         

if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















    






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    