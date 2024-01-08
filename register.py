from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
from time import strftime
from tkinter import * 
from tkinter import ttk ,Tk
import tkinter
from PIL import Image,ImageTk 
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from datetime import datetime


class register_window:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1600x900+0+0")
            self.root.title("Face Recognition System")
            self.root.wm_iconbitmap('face.ico')


            #===========================Variables==================

            self.var_fname=StringVar()
            self.var_lname=StringVar()
            self.var_contact=StringVar()
            self.var_email=StringVar()
            self.var_sq=StringVar()
            self.var_sa=StringVar()
            self.var_pass=StringVar()
            self.var_repass=StringVar()
            self.var_check=IntVar()
            



            #bg-img
            self.bg_img=ImageTk.PhotoImage(file=r"images/0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
            bg_lbl = Label(self.root,image=self.bg_img)
            bg_lbl.place(x=0,y=0,relheight=1,relwidth=1) 

            #left-img
            self.bg_img2=ImageTk.PhotoImage(file=r"images/thought-good-morning-messages-LoveSove.jpg")
            bg_lbl = Label(self.root,image=self.bg_img2)
            bg_lbl.place(x=50,y=100,height=550,width=470) 


            #=========================frame======================
            frame=Frame(self.root,bg="white")
            frame.place(x=520,y=100,width=800,height=550)

            reg_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="darkgreen",bg="white")
            reg_lbl.place(x=20,y=20)

            #==========================Lablels - Entries===================
            
            #first-name
            first_name = Label(frame,text="First Name",font=("time new roman",  15,"bold"),bg="white")
            first_name.place(x=50,y=100) 


            self.first_name=ttk.Entry(frame,textvariable=self.var_fname,width=20,font=("time new roman",  15,"bold"))
            self.first_name.place(x=50,y=130,width=250)


            #last-name
            last_name = Label(frame,text="Last Name",font=("time new roman",  15,"bold"),bg="white")
            last_name.place(x=370,y=100) 


            self.last_name=ttk.Entry(frame,textvariable=self.var_lname,width=20,font=("time new roman",  15,"bold"))
            self.last_name.place(x=370,y=130,width=250)


            #contact
            contact = Label(frame,text="Contact",font=("time new roman",  15,"bold"),bg="white")
            contact.place(x=50,y=170) 


            self.contact=ttk.Entry(frame,width=20,textvariable=self.var_contact,font=("time new roman",  15,"bold"))
            self.contact.place(x=50,y=200,width=250)

            #e-mail

            
            email_lab = Label(frame,text="E-mail",font=("time new roman",  15,"bold"),bg="white")
            email_lab.place(x=370,y=170) 


            self.email=ttk.Entry(frame,width=20,textvariable=self.var_email,font=("time new roman",  15,"bold"))
            self.email.place(x=370,y=200,width=250)

            #securition-question

            
            secq = Label(frame,text="Select your Security Question",font=("time new roman",  15,"bold"),bg="white")
            secq.place(x=50,y=240)

            self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_sq,font=("time new roman",  15,"bold"),state="readonly")
            self.combo_security_Q["values"]=("select","your birth-date","your pet name","your gf name","your best friend name")
            self.combo_security_Q.place(x=50,y=270,width=250)
            self.combo_security_Q.current(0)







            #security-answer
            seca = Label(frame,text="Security Answer",font=("time new roman",  15,"bold"),bg="white")
            seca.place(x=370,y=240) 

            self.txt_security=ttk.Entry(frame,textvariable=self.var_sa,font=("time new roman",  15,"bold"))
            self.txt_security.place(x=370,y=270,width=250)

            #password
            pwds = Label(frame,text="Password",font=("time new roman",  15,"bold"),bg="white")
            pwds.place(x=50,y=310) 

            self.new_password=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",  15,"bold"))
            self.new_password.place(x=50,y=340,width=250)


            rpwds = Label(frame,text="Confirm Password",font=("time new roman",  15,"bold"),bg="white")
            rpwds.place(x=370,y=310) 

            self.confirm_password=ttk.Entry(frame,textvariable=self.var_repass,font=("time new roman",  15,"bold"))
            self.confirm_password.place(x=370,y=340,width=250)


            #check-box
            checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree Terms & Conditions",font=("time new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
            checkbtn.place(x=50,y=380)

            #buttons-------------------------------Register-Now button 
            img9 = Image.open(r"images\register-now-button1.jpg")
            img9 = img9.resize((200,50),Image.ANTIALIAS)
            self.photoimg9 = ImageTk.PhotoImage(img9)
            b1=Button(frame,image=self.photoimg9,borderwidth=0,cursor="hand2",bg="white",command=self.register_data)
            b1.place(x=10,y=420,width=200)

            #Login-button

            img8 = Image.open(r"images\loginpng.png")
            img8 = img8.resize((200,50),Image.ANTIALIAS)
            self.photoimg8 = ImageTk.PhotoImage(img8)
            b1=Button(frame,image=self.photoimg8,borderwidth=0,cursor="hand2",bg="white")
            b1.place(x=330,y=420,width=200)


            #=================function=============

        def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sq.get()=="select":
                messagebox.showerror("Error","All Fields are required !")
            elif self.var_pass.get()!=self.var_repass.get():
                messagebox.showerror("Error","password and confirm password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","please agree terms & conditions")
            else:
                try:
                    conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                    my_cursor=conn.cursor()
                    query=("select *from register where email=%s")
                    value=(self.var_email.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","Email Already Exist !,please try another email.")
                    else:
                        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                               self.var_fname.get(),
                                                                                                               self.var_lname.get(),
                                                                                                               self.var_contact.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_sq.get(),
                                                                                                               self.var_sa.get(),
                                                                                                               self.var_pass.get()
                                                                                                               
                       
                                                                                            ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                except Exception as es:
                    messagebox("Error",f"Due To :{str(es)}",parent=self.root)











            








            










          




if __name__ == "__main__":
    root=Tk()
    obj=register_window(root)
    root.mainloop()