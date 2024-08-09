from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_rocognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime
from chatbot import ChatBot
import subprocess

class Face_Recognisiton_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        
        #first image
        img = Image.open("./college_images/Stanford.jpg")
        img = img.resize((500,130), Image.LANCZOS) #high to low
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width = 500, height=130) # label ko place
        
        #second image
        img1 = Image.open("./college_images/facialrecognition.png")
        img1 = img1.resize((520,130), Image.LANCZOS)
        
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width = 550, height=130)
        
        
        # third image
        img2 = Image.open("./college_images/u.jpg")
        img2 = img2.resize((500,130), Image.LANCZOS)
        
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width = 550, height=130)
        
        # background image
        img3 = Image.open("./college_images/wp2551980.jpg")
        img3 = img3.resize((1530,710), Image.LANCZOS)
        
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width = 1530, height=710)
        
        title_lbl = Label(bg_img, text = "Face Track", font=("times new roman" ,35, "bold"), bg = "white", fg = "red")
        title_lbl.place(x = 0, y = 0, width=1530, height=45)
        
        #===========time============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text =string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, text = "", font=("times new roman",15, "bold"), bg = "white", fg = "red")
        lbl.place(x= 0, y=0, width =110, height = 50)
        time()
        
        # student button
        img4 = Image.open("./college_images/student.jpg")
        img4 = img4.resize((220,220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y = 100 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman" ,15, "bold"), bg = "darkblue", fg = "white")
        b1_1.place(x=200, y = 300 , width=220, height= 40)
        b1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1.place(x=200, y=200, width=220, height=40)

        
        # Detect face button
        img5 = Image.open("./college_images/front.jpg")
        img5 = img5.resize((220,220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y = 100 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=500, y = 200 , width=220, height= 40)
        
        # Attendance face button
        img6 = Image.open("./college_images/smart-attendance.jpg")
        img6 = img6.resize((220,220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y = 100 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=800, y = 200 , width=220, height= 40)
        
        # # chatbot
        img7 = Image.open("./college_images/chat.jpg")
        img7 = img7.resize((220,220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.chatbot)
        b1.place(x=1100, y = 100 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="chatbot", cursor="hand2",command=self.chatbot, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=1100, y = 200 , width=220, height= 40)
        
        
        # Train button
        img8 = Image.open("./college_images/Train.jpg")
        img8 = img8.resize((220,220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y = 380 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=200, y = 480 , width=220, height= 40)
        
        # Photos button
        img9 = Image.open("./college_images/opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220,220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y = 380 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=500, y = 480 , width=220, height= 40)
        
        # Developer button
        img10 = Image.open("./college_images/developer.jpg")
        img10 = img10.resize((220,220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y = 380 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Developer",command=self.developer_data, cursor="hand2", font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=800, y = 480 , width=220, height= 40)
        
        # Exit button
        img11 = Image.open("./college_images/exit.jpg")
        img11 = img11.resize((220,220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100, y = 380 , width=220, height= 220)
        
        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman" ,15, "bold"), bg = "white", fg = "black")
        b1_1.place(x=1100, y = 480 , width=220, height= 40)
    
    def open_img(self):
         os.startfile("data")
        #subprocess.Popen(["open", "data"])

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit", parent =self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
        
        #===============Functions=========================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    # def help_data(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Help(self.new_window)    
    
    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognisiton_System(root)
    root.mainloop()
