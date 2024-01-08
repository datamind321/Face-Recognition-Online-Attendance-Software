from tkinter import * 
from tkinter import ttk
from tkinter import filedialog 
from PIL import Image,ImageTk 
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')


        title = Label(self.root,text="TRAIN DATA SET",font=("time new roman",35,"bold"),bg="white",fg='red')
        title.place(x=0,y=0,height=45,width=1530)


        b1_2=Button(title,command=self.back_btn,text="Back",cursor="hand2",font=("time new roman",15,"bold"),bg="green",fg="white")
        b1_2.place(x=1400,y=10,height=25, width=100)


        img_top = Image.open(r"images\facialrecognition.png")
        img_top = img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        self.btn2 = Button(self.root,image=self.photoimg_top,command=self.open_img4)
        self.btn2.place(x=0,y=55,height=325,width=1530)


    





        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("time new roman",35,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,height=60, width=1530) 



    


















        img_bottom = Image.open(r"images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        self.btn3 = Button(self.root,image=self.photoimg_bottom,command=self.open_img5)
        self.btn3.place(x=0,y=440,height=325,width=1530) 


    def train_data(self):
        data_dir=("data")
        path = [ os.path.join(data_dir,file) for file in os.listdir(data_dir) ] 

        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')  #gray-scale img
            imgNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training",imgNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

            #======================= Train the data and save =====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data-set completed",parent=self.root)



    def back_btn(self):
        self.root.destroy()

    def open_img4(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__902 = Image.open(fln)
        img_browse = img__902.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_7902 = ImageTk.PhotoImage(img_browse)
        self.btn2.config(image=self.photoimg_7902)
    def open_img5(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__903 = Image.open(fln)
        img_browse = img__903.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_7903 = ImageTk.PhotoImage(img_browse)
        self.btn3.config(image=self.photoimg_7903)





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()