from time import strftime
from tkinter import * 
from tkinter import ttk ,Tk
import tkinter
from tkinter import filedialog
from PIL import Image,ImageTk  
from face_recognition import Face_Recognition
from student import Student
import os
from train import Train
from attendence import Attendence
from developer import Developer
from datetime import datetime

from chatbot import Chatbot

   
   

class Face_Recognition_System:
      def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')


        # add IMages 

        img1 = Image.open(r"images\Stanford.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.btn1 = Button(self.root,image=self.photoimg1,command=self.open_img)
        self.btn1.place(x=0,y=0,height=130,width=500)


        img2 = Image.open(r"images\facialrecognition.png")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.btn2 = Button(self.root,image=self.photoimg2,command=self.open_img2)
        self.btn2.place(x=500,y=0,height=130,width=500)

        img3 = Image.open(r"images\u.jpg")
        img3 = img3.resize((550,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.btn3 = Button(self.root,image=self.photoimg3,command=self.open_img3)
        self.btn3.place(x=1000,y=0,height=130,width=550) 

        #Background-img

        # main_frame=Frame(self.root,bd=5,relief=RIDGE)
        # main_frame.place(x=0,y=130,width=1530,height=710)

        img4 = Image.open(r"images\wp2551980.jpg")
        img4 = img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=130,height=710,width=1530) 

        #title-label 
        title = Label(bg_lbl,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("time new roman",35,"bold"),bg="white",fg='red')
        title.place(x=0,y=0,height=45,width=1530)

        #show time in my window 
        def time():
          string=strftime("%H:%M:%S %p")
          lbl.config(text=string)
          lbl.after(1000,time)
          

        lbl=Label(title,font=("time new roman",12,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

    

        #student-button
        img5 = Image.open(r"images\gettyimages-1022573162.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        self.b1=Button(bg_lbl ,image=self.photoimg5,cursor="hand2",command=self.open_img4)
        self.b1.place(x=200,y=100,height=220, width=220)

        b1_1=Button(bg_lbl,command=self.student_details,text="Student Details",cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,height=40, width=220)


        #face-detector button
        img6 = Image.open(r"images\face_detector1.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        self.b2=Button(bg_lbl,image=self.photoimg6,cursor="hand2",command=self.open_img5)
        self.b2.place(x=500,y=100,height=220, width=220)

        b1_1=Button(bg_lbl,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,height=40, width=220)

        #attendence - button
        img7 = Image.open(r"images\report.jpg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        self.b3=Button(bg_lbl,image=self.photoimg7,cursor="hand2",command=self.open_img6)
        self.b3.place(x=800,y=100,height=220, width=220)

        b1_1=Button(bg_lbl,text="Attendence",command=self.attendence_system,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,height=40, width=220) 

        #Chat-Bot button

        img8 = Image.open(r"images\chat.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        self.b4=Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.open_img7)
        self.b4.place(x=1100,y=100,height=220, width=220)

        b1_1=Button(bg_lbl,text="ChatBot",cursor="hand2",command=self.help_me,font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,height=40, width=220)

        #train-data button

        img9 = Image.open(r"images\Train.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        self.b5=Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img8)
        self.b5.place(x=200,y=380,height=220, width=220)

        b1_1=Button(bg_lbl,text="Train Data",command=self.train_data,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=580,height=40, width=220)
        
        #photo-data button

        img10 = Image.open(r"images\sample.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        self.b6=Button(bg_lbl,image=self.photoimg10,cursor="hand2",command=self.open_img9)
        self.b6.place(x=500,y=380,height=220, width=220)

        b1_1=Button(bg_lbl,text="Photo Data",command=self.open_img19,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=580,height=40, width=220) 
      

        #developer-info button

        img11 = Image.open(r"images\dev.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        self.b7=Button(bg_lbl,image=self.photoimg11,cursor="hand2",command=self.open_img10)
        self.b7.place(x=800,y=380,height=220, width=220)

        b1_1=Button(bg_lbl,text="Developer",command=self.developer_system,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=580,height=40, width=220)


          #exit button

        img12 = Image.open(r"images\exit.jpg")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        self.b8=Button(bg_lbl,image=self.photoimg12,cursor="hand2",command=self.open_img11)
        self.b8.place(x=1100,y=380,height=220, width=220)

        b1_1=Button(bg_lbl,text="Exit",command=self.iExit,cursor="hand2",font=("time new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=580,height=40, width=220)


      def open_img19(self):
        os.startfile("data")

      def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognize","Are you sure exit to project",parent=self.root)
        if self.iExit>0:
          self.root.destroy() 

        else:
          return 







        #Functions 

      def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


      def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

      def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
      def attendence_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    


      def developer_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

      def help_me(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)

      
      def open_img(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__8 = Image.open(fln)
        img_browse = img__8.resize((500,130),Image.ANTIALIAS)
        self.photoimg_78 = ImageTk.PhotoImage(img_browse)
        self.btn1.config(image=self.photoimg_78)
      
      def open_img2(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__9 = Image.open(fln)
        img_browse = img__9.resize((500,130),Image.ANTIALIAS)
        self.photoimg_79 = ImageTk.PhotoImage(img_browse)
        self.btn2.config(image=self.photoimg_79)

      def open_img3(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__90 = Image.open(fln)
        img_browse = img__90.resize((550,130),Image.ANTIALIAS)
        self.photoimg_790 = ImageTk.PhotoImage(img_browse)
        self.btn3.config(image=self.photoimg_790)
      def open_img4(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__901 = Image.open(fln)
        img_browse = img__901.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7901 = ImageTk.PhotoImage(img_browse)
        self.b1.config(image=self.photoimg_7901)
      def open_img5(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__902 = Image.open(fln)
        img_browse = img__902.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7902 = ImageTk.PhotoImage(img_browse)
        self.b2.config(image=self.photoimg_7902)
      def open_img6(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__903 = Image.open(fln)
        img_browse = img__903.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7903 = ImageTk.PhotoImage(img_browse)
        self.b3.config(image=self.photoimg_7903)
      def open_img7(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__904 = Image.open(fln)
        img_browse = img__904.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7904 = ImageTk.PhotoImage(img_browse)
        self.b4.config(image=self.photoimg_7904)
      def open_img8(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__905 = Image.open(fln)
        img_browse = img__905.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7905 = ImageTk.PhotoImage(img_browse)
        self.b5.config(image=self.photoimg_7905)
      def open_img9(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__906 = Image.open(fln)
        img_browse = img__906.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7906 = ImageTk.PhotoImage(img_browse)
        self.b6.config(image=self.photoimg_7906)
      def open_img10(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__907 = Image.open(fln)
        img_browse = img__907.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7907 = ImageTk.PhotoImage(img_browse)
        self.b7.config(image=self.photoimg_7907)
      def open_img11(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__908 = Image.open(fln)
        img_browse = img__908.resize((220,220),Image.ANTIALIAS)
        self.photoimg_7908 = ImageTk.PhotoImage(img_browse)
        self.b8.config(image=self.photoimg_7908)

      

      

     










    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()