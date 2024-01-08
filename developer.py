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
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')

        title = Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg='green')
        title.place(x=0,y=0,height=45,width=1530)

        b1_2=Button(title,command=self.back_btn,text="Back",cursor="hand2",font=("time new roman",15,"bold"),bg="red",fg="white")
        b1_2.place(x=1400,y=10,height=25, width=100)

        #1st image
        img_top = Image.open(r"images\fg.png")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,height=720,width=1530)


        

    def back_btn(self):
        self.root.destroy()
       


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()