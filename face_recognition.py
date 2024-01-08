from tkinter import * 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')


        title = Label(self.root,text="FACE RECOGNITION",font=("time new roman",35,"bold"),bg="white",fg='green')
        title.place(x=0,y=0,height=45,width=1530)

        #back-button
        b1_2=Button(self.root,command=self.back_btn,text="Back",cursor="hand2",font=("time new roman",20,"bold"),bg="black",fg="white")
        b1_2.place(x=1400,y=15,height=25, width=100)



        #1st image
        img_top = Image.open(r"images\face_detector1.jpg")
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,height=700,width=650) 

        #2nd image
        img_bottom = Image.open(r"images\show.jpg")
        img_bottom = img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,height=700,width=950) 
        #2nd image ke uper button lagana hain..............
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("time new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=365,y=620,height=40, width=200) 

        




        #========================Attendence======================================

    def mark_attendence(self,i,r,n,d):
        with open("attendance_report/attendence.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and ( n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S") 
                if d1 not in  f:
                    f.writelines(f"\n{i},{r},{n},{d1},{d},{dtString},Present")





        #======================   face recognition   =================
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select roll_number from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d) 


                if confidence>77:
                    cv2.putText(img,f"ID : {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name : {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Roll Number : {r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department : {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendence(i,r,n,d) 
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(0,0,255),"Face",clf)
            return img 
            
        faceCascade=cv2.CascadeClassifier( cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:  
                break
        video_cap.release()
        cv2.destroyAllWindows()


    def back_btn(self):
        self.root.destroy()












if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 