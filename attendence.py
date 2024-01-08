from tkinter import * 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import csv 
from tkinter import filedialog
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

mydata = []
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')


        #======================variables=============
        self.att_id=StringVar()
        self.roll_no=StringVar()
        self.st_name=StringVar()
        self.att_date=StringVar()
        self.dep=StringVar()
        self.att_time=StringVar()
        self.att_status=StringVar()
                



        # add  two IMages top-lable


        #1st image
        img1 = Image.open(r"images\smart-attendance.jpg")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,height=200,width=800)

        #2nd image
        img2 = Image.open(r"images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,height=200,width=800)


        #bg-img
        img4 = Image.open(r"images\wp2551980.jpg")
        img4 = img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=200,height=710,width=1530) 


        #title-label 


        title = Label(bg_lbl,text=" ATTENDENCE MANAGEMENT SYSTEM ",font=("time new roman",35,"bold"),bg="white",fg='green')
        title.place(x=0,y=0,height=45,width=1530)

        def time():
          string=strftime("%H:%M:%S %p")
          lbl.config(text=string)
          lbl.after(1000,time)
          

        lbl=Label(title,font=("time new roman",12,"bold"),bg="white",fg="green")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #back-btn
        b1_2=Button(title,command=self.back_btn,text="Back",cursor="hand2",font=("time new roman",15,"bold"),bg="red",fg="white")
        b1_2.place(x=1400,y=10,height=25, width=100)

        #====================== main-frame ===================

        main_frame = Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,height=600, width=1480)

        #left-side frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
         
        #add-images-in-left frame
        img_left = Image.open(r"images\face-recognition.png")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_l = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_l)
        f_lbl.place(x=5,y=0,height=130,width=720)

        #INside-left-Frame

        mains_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        mains_frame.place(x=0,y=135,height=370, width=720)

        #labels-&-Entry


        #attendence-id

        attendenceId_lebel = Label(mains_frame,text="Attendence Id :",font=("time new roman",12,"bold"),bg="white")
        attendenceId_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W) 

        attendenceID_entry = ttk.Entry(mains_frame,width=20,textvariable=self.att_id,font=("time new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         #roll-number

        roll_lebel = Label(mains_frame,text="Roll Number :",font=("time new roman",12,"bold"),bg="white")
 
        roll_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W) 

        roll_label_entry = ttk.Entry(mains_frame,width=20,textvariable=self.roll_no,font=("time new roman",12,"bold"))
        roll_label_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student-name

        name_lebel = Label(mains_frame,text="Student Name :",font=("time new roman",12,"bold"),bg="white")
        name_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W) 

        name_entry = ttk.Entry(mains_frame,width=20,textvariable=self.st_name,font=("time new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


         #date

        date_lebel = Label(mains_frame,text="Date :",font=("time new roman",12,"bold"),bg="white")
        date_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W) 

        date_entry = ttk.Entry(mains_frame,width=20,textvariable=self.att_date,font=("time new roman",12,"bold"))
        date_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #department

        dep_lebel = Label(mains_frame,text="Department :",font=("time new roman",12,"bold"),bg="white")
        dep_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W) 

        dep_entry = ttk.Entry(mains_frame,width=20,textvariable=self.dep,font=("time new roman",12,"bold"))
        dep_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #time 

        tym_lebel = Label(mains_frame,text="Time :",font=("time new roman",12,"bold"),bg="white")
        tym_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W) 

        tym_entry = ttk.Entry(mains_frame,width=20,textvariable=self.att_time,font=("time new roman",12,"bold"))
        tym_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W) 


        #attendence-main

        att_lebel = Label(mains_frame,text="Attendence :",font=("time new roman",12,"bold"),bg="white")
        att_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W) 

        att_combo = ttk.Combobox(mains_frame,textvariable=self.att_status,font=("comicsansns",10),width=17,state="readonly")
        att_combo["values"]=("Status","Present","Absent")
        att_combo.current(0)
        att_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)


        #button-frames
        btn_frame= Frame(mains_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)
        #buttons
        import_btn=Button(btn_frame,text="Import csv",command=self.import_csv,width=14,font=("time new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
        exp_btn=Button(btn_frame,text="Export csv",command=self.export_csv,width=14,font=("time new roman",12,"bold"),bg="blue",fg="white")
        exp_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text="Update",width=14,font=("time new roman",12,"bold"),bg="blue",fg="white",command=self.action)
        update_btn.grid(row=0,column=2)
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("time new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=14,font=("time new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)






        #right-side frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        #table-frames
        tb_frame= Frame(right_frame,bd=2,relief=RIDGE,bg="White")
        tb_frame.place(x=5,y=5,width=700,height=455)

        #scroll bar and table

        #scroll-bar
        scroll_x = ttk.Scrollbar(tb_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tb_frame,orient=VERTICAL)

        self.attendence_table=ttk.Treeview(tb_frame,columns=("id","roll-number","name","date","department","time","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendence_table.xview)
        scroll_y.config(command=self.attendence_table.yview)
        self.attendence_table.heading("id",text="Attendence-Id")
        self.attendence_table.heading("roll-number",text="Roll Number")
        self.attendence_table.heading("name",text="Student Name")
        self.attendence_table.heading("date",text="Date")
        self.attendence_table.heading("department",text="Department")
        self.attendence_table.heading("time",text="Time")
        self.attendence_table.heading("attendence",text="Status")
        self.attendence_table["show"]="headings"
        self.attendence_table.column("id",width=100)
        self.attendence_table.column("roll-number",width=100)
        self.attendence_table.column("name",width=100)
        self.attendence_table.column("date",width=100)
        self.attendence_table.column("department",width=100)
        self.attendence_table.column("time",width=100)
        self.attendence_table.column("attendence",width=100)
        
        self.attendence_table.pack(fill=BOTH,expand=1)
        self.attendence_table.bind("<ButtonRelease>",self.get_cursor_left)



        #============================ face data function================
    # def fetch_data(self,rows):
    #     self.attendence_table.delete(*self.attendence_table.get_children())
    #     for i in rows:
    #         self.attendence_table.insert("",END,values=i)

   #======== Import csv --============================

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert("",END,values=i)
            print(i)






    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV FILE","*.csv"),("all file","*.*")),parent=self.root)
        with open (fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in  csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #=================== Export csv =======================

    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV FILE","*.csv"),("all file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                csvwrite=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+" successfully !",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    

    #===========================get_cursor_for_csv_file_________________________
    

    def get_cursor_left(self,event=""):
        cursor=self.attendence_table.focus()
        content=self.attendence_table.item(cursor)
        rows=content["values"]

        self.att_id.set(rows[0])
        self.roll_no.set(rows[1])
        self.st_name.set(rows[2])
        self.att_date.set(rows[3])
        self.dep.set(rows[4])
        self.att_time.set(rows[5])
        self.att_status.set(rows[6])

        

         #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.att_id.set(data[0]),
        self.roll_no.set(data[1]),
        self.st_name.set(data[2]),
        self.att_time.set(data[3]),
        self.att_date.set(data[4]),
        self.att_status.set(data[5]) 


    

    def reset(self):
         self.att_id.set("")
         self.roll_no.set("")
         self.st_name.set("")
         self.att_date.set("")
         self.dep.set("")
         self.att_time.set("")
         self.att_status.set("")

    
    def back_btn(self):
        self.root.destroy()



    def update_data(self):
        if self.att_id.get()=="" or self.roll_no.get=="" or self.st_name.get()=="" or self.att_time.get()=="" or self.att_date.get()=="" or self.att_status.get()=="Status":
            messagebox.showerror("Error","Please All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update attendence set id=%s,roll_no=%s,st_name=%s,att_date=%s,department=%s,att_time=%s,status=%s where id=%s",( 
                    self.att_id.get(),
                    self.roll_no.get(),
                    self.st_name.get(),
                    self.att_date.get(),
                    self.dep.get(),
                    self.att_time.get(),
                    self.att_status.get(),
                    self.att_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()   
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='12345678',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from attendence")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendence_table.delete(*self.attendence_table.get_children())
            for i in data:
                self.attendence_table.insert("",END,values=i)
            conn.commit()
        conn.close() 




    # export upadte
    def action(self):
        if self.att_id.get()=="" or self.roll_no.get=="" or self.st_name.get()=="" or self.att_time.get()=="" or self.att_date.get()=="" or self.att_status.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='12345678',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into attendence values(%s,%s,%s,%s,%s,%s,%s)",(
                self.att_id.get(),
                self.roll_no.get(),
                self.st_name.get(),
                self.att_date.get(),
                self.dep.get(),
                self.att_time.get(),
                self.att_status.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    

    def delete_data(self):
        if self.att_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='12345678',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from attendence where id=%s"
                    val=(self.att_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  


        




        








if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop() 