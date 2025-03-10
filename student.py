from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("face recognition system")
        
        #===============variables=============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_stdname = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        
        #first image
        img = Image.open("./college_images/facialrecognition.png")
        img = img.resize((500,130), Image.LANCZOS)
        
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width = 500, height=130)
        #second image
        img1 = Image.open("./college_images/smart-attendance.jpg")
        img1 = img1.resize((500,130), Image.LANCZOS)
        
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width = 500, height=130)
        # third image
        img2 = Image.open("./college_images/uio.jpg")
        img2 = img2.resize((500,130), Image.LANCZOS)
        
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width = 550, height=130)
        
        # background image
        img3 = Image.open("./college_images/atten.png")
        img3 = img3.resize((1530,710), Image.LANCZOS)
         
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width = 1530, height=710)
        
        title_lbl = Label(bg_img, text = "STUDENT MANAGEMENT SYSTEM", font=("times new roman" ,35, "bold"), bg = "white", fg = "blue")
        title_lbl.place(x = 0, y = 0, width=1530, height=45)
        
        main_frame = Frame(bg_img, bd= 2)
        main_frame.place(x= 10, y = 55, width = 1500, height=600)
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd = 2,bg="white", relief= RIDGE, text="Student Details", font=("times new roman" ,12, "bold"))
        Left_frame.place(x= 10, y =10, width = 730, height = 580)
        
        img_left = Image.open("./college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720,130), Image.LANCZOS)
        
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width = 720, height=130)
        
        #current course
        current_course = LabelFrame(Left_frame, bd = 2,bg="white", relief= RIDGE, text="Current Course Information", font=("times new roman" ,12, "bold"))
        current_course.place(x= 5, y = 135, width = 720, height = 150)
       
       #Department
        dep_label = Label(current_course, text="Department",font=("times new roman" ,12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)
        
        deep_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=("times new roman" ,12, "bold"),state="readonly",width=20)
        deep_combo["values"] = ("Select Department","IT","CSE", "AIML", "DS", "CIVIL", "MECHANICAL")
        deep_combo.current(0)
        deep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        #Course
        course_label = Label(current_course,text="Course",font=("times new roman" ,12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10)
        
        course_combo = ttk.Combobox(current_course, textvariable=self.var_course,font=("times new roman" ,12, "bold"),state="readonly",width=20)
        course_combo["values"] = ("Select Course","NLP","DA", "PYTHON", "SE", "MECH", "ARCH","BT","BD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)
        
        #Year
        year_label = Label(current_course, text="Year",font=("times new roman" ,12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10)
        
        year_combo = ttk.Combobox(current_course,textvariable=self.var_year, font=("times new roman" ,12, "bold"),state="readonly",width=20)
        year_combo["values"] = ("Select Year","2020-21","2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)
        
        #semester
        semester_label = Label(current_course, text="Semester",font=("times new roman" ,12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10)
        
        semester_combo = ttk.Combobox(current_course, textvariable=self.var_semester,font=("times new roman" ,12, "bold"),state="readonly",width=20)
        semester_combo["values"] = ("Select Semester","Semester1","Semester2", "Semester3", "Semester4", "Semester5", "Semester6", "Semester7", "Semester8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)
        
        #class student information
        class_student_frame = LabelFrame(Left_frame, bd = 2,bg="white", relief= RIDGE, text="Current Course Information", font=("times new roman" ,12, "bold"))
        class_student_frame.place(x= 5, y = 250, width = 720, height = 300)
        #student_id
        student_label = Label(class_student_frame, text="Student ID:",font=("times new roman" ,12, "bold"), bg="white")
        student_label.grid(row=0, column=0, padx=10, sticky=W)
        
        Student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id,width=20, font=("times new roman" ,12, "bold"))
        Student_id_entry.grid(row = 0, column =1, padx=10,pady=5,sticky=W )
        
        #student_name
        student_name_label = Label(class_student_frame, text="Student Name:",font=("times new roman" ,12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10 ,pady=5, sticky=W)
        
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_stdname, width=20, font=("times new roman" ,12, "bold"))
        student_name_entry.grid(row = 0, column =3, padx=10,sticky=W )
        
        #class didivison
        class_div_label = Label(class_student_frame, text="Class Divison:",font=("times new roman" ,12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10 ,pady=5, sticky=W)
        
        # class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div,width=20, font=("times new roman" ,12, "bold"))
        # class_div_entry.grid(row = 1, column =1, padx=10,sticky=W )
        Divison_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman" ,12, "bold"),state="readonly",width=18)
        Divison_combo["values"] = ("Select Divison","A","B", "C","D")
        Divison_combo.current(0)
        Divison_combo.grid(row=1, column=1, padx=10, pady=5,sticky=W)
        
        #Roll No
        roll_no_label = Label(class_student_frame,text="Roll No:",font=("times new roman" ,12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10 ,pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll , width=20, font=("times new roman" ,12, "bold"))
        roll_no_entry.grid(row = 1, column =3, padx=10,sticky=W )
        
        #Gender
        Gender_label = Label(class_student_frame,text="Gender:",font=("times new roman" ,12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10 ,pady=5, sticky=W)
        
        # Gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender , width=20, font=("times new roman" ,12, "bold"))
        # Gender_entry.grid(row = 2, column =1, padx=10,sticky=W )
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman" ,12, "bold"),state="readonly",width=18)
        gender_combo["values"] = ("Select Gender","M","F", "OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5,sticky=W)
        
        #DOB
        DOB_label = Label(class_student_frame,text="DOB:",font=("times new roman" ,12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10 ,pady=5, sticky=W)
        
        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob ,width=20, font=("times new roman" ,12, "bold"))
        DOB_entry.grid(row = 2, column =3, padx=10,sticky=W )
        
        
        #Email
        email_label = Label(class_student_frame, text="Email:",font=("times new roman" ,12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10 ,pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman" ,12, "bold"))
        email_entry.grid(row = 3, column =1, padx=10,sticky=W )
        
        
        #Phone
        Phone_label = Label(class_student_frame, text="Phone No:",font=("times new roman" ,12, "bold"), bg="white")
        Phone_label.grid(row=3, column=2, padx=10 ,pady=5, sticky=W)
        
        Phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width=20, font=("times new roman" ,12, "bold"))
        Phone_entry.grid(row = 3, column =3, padx=10,sticky=W )
        
        
        #Address
        Address_label = Label(class_student_frame, text="Address:",font=("times new roman" ,12, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10 ,pady=5, sticky=W)
        
        Address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman" ,12, "bold"))
        Address_entry.grid(row = 4, column =1, padx=10,sticky=W )
        
        
        #Teacher_name
        Teacher_name_label = Label(class_student_frame, text="Teacher Name:",font=("times new roman" ,12, "bold"), bg="white")
        Teacher_name_label.grid(row=4, column=2, padx=10 ,pady=5, sticky=W)
        
        Teacher_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman" ,12, "bold"))
        Teacher_name_entry.grid(row = 4, column =3, padx=10,sticky=W )
        
        
        # Radio button
        self.var_radio = StringVar()
        radio1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio, text= "Take Photo Sample", value = "Yes")
        radio1.grid(row = 6, column=0)
        
        radio2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio, text= "No Photo Sample", value = "No")
        radio2.grid(row = 6, column=1)
        
        #buttons frame
        btn_frame = Frame(class_student_frame, bd = 2, relief=RIDGE , bg="white")
        btn_frame.place(x = 0, y =200, width = 655, height=35)
        
        save_btn = Button(btn_frame, text = "Save", command=self.add_data ,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        save_btn.grid(row= 0, column= 0 )
        
        update_btn = Button(btn_frame, text = "Update", command=self.update_data,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        update_btn.grid(row= 0, column= 1 )
        
        delete_btn = Button(btn_frame, text = "Delete", command= self.delete_data,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        delete_btn.grid(row= 0, column= 2 )
        
        reset_btn = Button(btn_frame, text = "Reset",command= self.reset_data ,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        reset_btn.grid(row= 0, column= 3 )
        
        btn_frame1 = Frame(class_student_frame, bd = 2, relief=RIDGE , bg="white")
        btn_frame1.place(x = 0, y =235, width = 655, height=35)
        
        take_photo_btn = Button(btn_frame1, text = "Take Photo Sample",command=self.generate_dataset ,width= 35,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        take_photo_btn.grid(row= 0, column= 0 )
        
        update_photo_btn = Button(btn_frame1, text = "Update Photo Sample", width= 35,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        update_photo_btn.grid(row= 0, column= 1 )
        
                
        #Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2,bg="white", relief= RIDGE, text="Student Details", font=("times new roman" ,12, "bold"))
        Right_frame.place(x= 750, y =10, width = 720, height = 580)
        
        img_right = Image.open("./college_images/face-recognition.png")
        img_right = img_right.resize((720,130), Image.LANCZOS)
        
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width = 710, height=130)
        
        #Search Sytem
        search_frame = LabelFrame(Right_frame, bd = 2,bg="white", relief= RIDGE, text="Search System", font=("times new roman" ,12, "bold"))
        search_frame.place(x= 5, y = 135, width = 710, height = 70)
        
        search_label = Label(search_frame, text="Search By:",font=("times new roman" ,15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10 ,pady=5, sticky=W)
        
        search_combo = ttk.Combobox(search_frame, font=("times new roman" ,12, "bold"),state="readonly",width=20)
        search_combo["values"] = ("Select","Roll no","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman" ,12, "bold"))
        search_entry.grid(row = 0, column =2, padx=10,sticky=W )
        
        search_btn = Button(search_frame, text = "Search", width= 12,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        search_btn.grid(row= 0, column= 3, padx=4)
        
        show_btn = Button(search_frame, text = "Show All", width= 12,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        show_btn.grid(row= 0, column= 4, padx=4 )
        
        #_________________tableframe============
        
        table_frame = Frame(Right_frame, bd = 2,bg="white", relief= RIDGE)
        table_frame.place(x= 5, y = 210, width = 710, height = 350)
        
        scroll_x =ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column = ("dep","course", "year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text = "Department")
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("sem", text = "Semester")
        self.student_table.heading("id", text = "StudentId")
        self.student_table.heading("name", text = "Name")
        self.student_table.heading("div", text = "Divison")
        self.student_table.heading("roll", text = "Roll_No")
        self.student_table.heading("gender", text = "Gender")
        self.student_table.heading("dob", text = "DOB")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("phone", text = "Phone")
        self.student_table.heading("address", text = "Address")
        self.student_table.heading("teacher", text = "Teacher")
        self.student_table.heading("photo", text = "Photo sample status")
        self.student_table['show'] = "headings"
        
        self.student_table.column("dep", width =100)
        self.student_table.column("course",width =100)
        self.student_table.column("year", width =100)
        self.student_table.column("sem", width =100)
        self.student_table.column("id", width =100)
        self.student_table.column("name",width =100)
        self.student_table.column("div",width =100)
        self.student_table.column("roll", width =100)
        self.student_table.column("gender", width =100)
        self.student_table.column("dob", width =100)
        self.student_table.column("email", width =100)
        self.student_table.column("phone", width =100)
        self.student_table.column("address", width =100)
        self.student_table.column("teacher", width =100)
        self.student_table.column("photo", width =150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
     #===============function declaration================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdname.get() == "" or self.var_std_id.get() =="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",user ="root", passwd = "7229900623", database = "face_recognizer")
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                          self.var_dep.get(),
                                                                                                          self.var_course.get(),
                                                                                                          self.var_year.get(),
                                                                                                          self.var_semester.get(),
                                                                                                          self.var_std_id.get(),
                                                                                                          self.var_stdname.get(),
                                                                                                          self.var_div.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_dob.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_phone.get(),
                                                                                                          self.var_address.get(),
                                                                                                          self.var_teacher.get(),
                                                                                                          self.var_radio.get()
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student detail has been added successfully",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
    #------------fetch data---- 
    
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",user ="root", passwd = "7229900623", database = "face_recognizer")
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data = mycursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values= i)
            conn.commit()
        conn.close()
    #===============get cursor===================
    def get_cursor(self, event= ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])
        
    #===============function UPDTAE================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdname.get() == "" or self.var_std_id.get() =="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Do you want to update", parent= self.root)
                if Update >0:
                    conn = mysql.connector.connect(host = "localhost",user ="root", passwd = "7229900623", database = "face_recognizer")
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Dep =%s ,course =%s,Year =%s,Semester =%s,Name = %s,Divison =%s,Roll =%s,Gender =%s,Dob =%s,Email =%s,Phone = %s,Address=%s,Teacher =%s,photoSample =%s where Student_id = %s",( 
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_stdname.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Student details updated", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
        #====================DELETE =============================
    def delete_data(self):
        if self.var_std_id.get() =="":
            messagebox.showerror("Error", "Student ids are required", parent = self.root)
        else:
            try:
                Delete = messagebox.askyesno("Do you want to delete", parent= self.root)
                if Delete >0:
                    conn = mysql.connector.connect(host = "localhost",user ="root", passwd = "7229900623", database = "face_recognizer")
                    mycursor = conn.cursor()
                    sql  = "delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Student details deleted", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
                
       #===================resrtools =============================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_stdname.set(""),
        self.var_div.set("Select Divison"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set("")
        
    #===================Generate dataset and take photo sample============================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stdname.get() == "" or self.var_std_id.get() =="":
            messagebox.showerror("Error", "All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",user ="root", passwd = "7229900623", database = "face_recognizer")
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult  = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                mycursor.execute("update student set Dep =%s ,course =%s,Year =%s,Semester =%s,Name = %s,Division =%s,Roll =%s,Gender =%s,Dob =%s,Email =%s,Phone = %s,Address=%s,Teacher =%s,photoSample =%s where Student_id = %s",( 
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_stdname.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio.get(),
                                                                                                                                                                                                        self.var_std_id.get() == id+1
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=====================Load Predefined data on face frontals from opencv=================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling_factor = 1.3
                    #Minimum Neighbor = 5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h ,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id = img_id + 1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
                 
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()