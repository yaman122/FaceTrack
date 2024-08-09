from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition System")
        
        #===================Variables==============
        self.var_atten_id =StringVar()
        self.var_atten_roll =StringVar()
        self.var_atten_name =StringVar()
        self.var_atten_dep =StringVar()
        self.var_atten_time =StringVar()
        self.var_atten_date =StringVar()
        self.var_atten_attendance =StringVar()
        
        #first image
        img = Image.open("./college_images/smart-attendance.jpg")
        img = img.resize((800,200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x = 0, y=0, width = 800, height=200)
        #second image
        img1 = Image.open("./college_images/PES1.jpeg")
        img1 = img1.resize((800,200), Image.LANCZOS)
        
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800, y=0, width = 800, height=200)
        
        #Background image
        img2 = Image.open("./college_images/un.jpg")
        img2 = img2.resize((1530,710), Image.LANCZOS)
        
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0, y=200, width = 1530, height=710)
        
        title_lbl = Label(f_lbl, text = "ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman" ,35, "bold"), bg = "white", fg = "black")
        title_lbl.place(x = 0, y = 0, width=1530, height=45)
        
        main_frame = Frame(f_lbl, bd= 2)
        main_frame.place(x= 20, y = 55, width = 1480, height=600)
        
        #Left frame
        Left_frame = LabelFrame(main_frame, bd = 2,bg="white", relief= RIDGE, text="Student Attendance Details", font=("times new roman" ,12, "bold"))
        Left_frame.place(x= 10, y =10, width = 730, height = 550)
        
        img_left = Image.open("./college_images/ghi.jpeg")
        img_left = img_left.resize((720,130), Image.LANCZOS)
        
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width = 720, height=130)
        
        left_inside_frame = Frame(Left_frame, bd= 2, relief=RIDGE,bg="white")
        left_inside_frame.place(x= 0, y = 135, width = 720, height=370)
        
        #Labelandentry
        #Attendance id.
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:",font=("times new roman" ,12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)
        
        attendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable= self.var_atten_id,font=("times new roman" ,12, "bold"))
        attendanceID_entry.grid(row = 0, column =1, padx=10,pady=5,sticky=W )
        
        #Roll
        
        rolllabel = Label(left_inside_frame, text="Roll:",font="comicsansns  11  bold", bg="white")
        rolllabel.grid(row=0, column=2, padx=4,pady=8)
        
        atten_roll = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll, font="comicsansns  11  bold")
        atten_roll.grid(row = 0, column =3,pady=8 )
        
        #Name
        nameLabel = Label(left_inside_frame, text="Name:",font="comicsansns  11  bold", bg="white")
        nameLabel.grid(row=1, column=0)
        
        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20, font="comicsansns  11  bold")
        atten_name.grid(row = 1, column =1,pady=8)
        
        #Department
        
        deplabel = Label(left_inside_frame, text="Department:",font="comicsansns  11  bold", bg="white")
        deplabel.grid(row=1, column=2, padx=4,pady=8, sticky=W)
        
        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20, font="comicsansns  11  bold")
        atten_dep.grid(row = 1, column =3,pady=8 )
        
        #   time
        timeLabel = Label(left_inside_frame, text="Time:",font="comicsansns  11  bold", bg="white")
        timeLabel.grid(row=2, column=0)
        
        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20, font="comicsansns  11  bold")
        atten_time.grid(row = 2, column =1,pady=8)
        
        #Date
        dateLabel = Label(left_inside_frame, text="Date:",font="comicsansns  11  bold", bg="white")
        dateLabel.grid(row=2, column=2)
        
        atten_date = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date, font="comicsansns  11  bold")
        atten_date.grid(row = 2, column =3,pady=8)
        
        
        #Attendance
        
        attendancelabel = Label(left_inside_frame, text="Class Divison:",font="comicsansns  11  bold", bg="white")
        attendancelabel.grid(row=3, column=0)
        
        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, font="comicsansns  11  bold", state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)
        
        #buttons frame
        btn_frame = Frame(left_inside_frame, bd = 2, relief=RIDGE , bg="white")
        btn_frame.place(x = 0, y =250, width = 655, height=35)
        
        save_btn = Button(btn_frame, text = "Import csv",command=self.importCsv,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        save_btn.grid(row= 0, column= 0 )
        
        update_btn = Button(btn_frame, text = "Export csv",command=self.exportCsv,width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        update_btn.grid(row= 0, column= 1 )
        
        delete_btn = Button(btn_frame, text = "Update",width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        delete_btn.grid(row= 0, column= 2 )
        
        reset_btn = Button(btn_frame,command=self.reset_data, text = "Reset",width= 17,font=("times new roman" ,12, "bold"), bg="white", fg="black")
        reset_btn.grid(row= 0, column= 3 )
    
        
        #Right frame
        Right_frame = LabelFrame(main_frame, bd = 2,bg="white", relief= RIDGE, text="Student Attendance Details", font=("times new roman" ,12, "bold"))
        Right_frame.place(x= 750, y =10, width = 720, height = 580)
        
        
        table_frame = Frame(Right_frame, bd = 2, relief=RIDGE , bg="white")
        table_frame.place(x = 5, y =5, width = 700, height=455)
        
        #Scroll Bar table
        scroll_x =ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame, column = ("id","roll", "name","department","time","date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        
    #===============Fetch data============
    def fetchdata(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END, values = i)
            
    #===============IMPORT data============
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as  myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    #=============EXPORT =================
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data Found", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir= os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode= "w",newline="")as myfile:
                exp_write = csv.writer(myfile, delimiter= ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent = self.root)
        
    def get_cursor(self, event=""):
        cursor = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor)
        row = content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()