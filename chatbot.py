from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Chatbot:
        def __init__(self,root):
            self.root=root
            self.root.geometry("730x620+0+0")
            self.root.title("Face Recognition System")
            self.root.bind("<Return>",self.enter_func)
            self.root.wm_iconbitmap('face.ico')


            frame=Frame(self.root,bd=4,bg="powder blue",width=610)
            frame.pack()

            img_chat = Image.open(r"images/chat.jpg")
            img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img_chat)
            title_lbl=Label(frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="Chat Me",font=("times new roman",30,"bold"),bg="white",fg="green")
            title_lbl.pack(side=TOP)


            self.scroll_y=ttk.Scrollbar(frame,orient=VERTICAL)
            self.text=Text(frame,width=65,height=20,bd=3,relief=RAISED,font=("times new roman",14,"bold"),yscrollcommand=self.scroll_y)
            self.scroll_y.pack(side=RIGHT,fill=Y)
            self.text.pack()

            btn_frame=Frame(self.root,bd=4,bg="white",width=730)
            btn_frame.pack()

            labl=Label(btn_frame,text="Type Something",font=("times new roman",14,"bold"),fg="green",bg="white")
            labl.grid(row=0,column=0,padx=5,sticky=W)
            

            self.entry=StringVar()
            self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("times new roman",17))
            self.entry1.grid(row=0,column=1,padx=5,sticky=W)

            self.send=Button(btn_frame,command=self.send,text="Send",font=("times new roman",12,"bold"),width=8,bg="green")
            self.send.grid(row=0,column=2,padx=5,sticky=W)

            
            self.clear=Button(btn_frame,command=self.clear_func,text="Clear",font=("times new roman",12,"bold"),width=8,bg="red",fg="white")
            self.clear.grid(row=1,column=0,padx=5,sticky=W)
            
            self.msg=''
            self.labl_12=Label(btn_frame,text=self.msg,font=("times new roman",14,"bold"),fg="red",bg="white")
            self.labl_12.grid(row=1,column=1,padx=5,sticky=W)


            #=================== Main Function ====================


        def enter_func(self,event=''):
            self.send.invoke()
            self.entry.set('')

        def clear_func(self):
            self.text.delete('1.0',END)
            self.entry.set('')












        def send(self):
            send='\t\t\t'+'You : '+self.entry.get()
            self.text.insert(END,'\n'+send)
            self.text.yview(END)

            if(self.entry.get()==""):
                self.msg='Please Enter Some Input.'
                self.labl_12.config(text=self.msg,fg="red")
            else:
                self.msg=''
                self.labl_12.config(text=self.msg,fg="red")
            if(self.entry.get()=="hello"):
                self.text.insert(END,'\n\n'+'Bot : Hii ')
            elif(self.entry.get()=="hii"):
                self.text.insert(END,'\n\n'+'Bot : hello ')
            elif(self.entry.get()=="who are you"):
                self.text.insert(END,'\n\n'+'Bot : I am chatbot')
            elif(self.entry.get()=="who created you"):
                self.text.insert(END,'\n\n'+'Bot : rahul created me using python language ')
            elif(self.entry.get()=="how are you"):
                self.text.insert(END,'\n\n'+'Bot : Fantastic ...!!!!!!')
            elif(self.entry.get()=="what is python"):
                self.text.insert(END,'\n\n'+'Bot : Python is most popular programming language which used to developed softwares, webapps and etc.')
            elif(self.entry.get()=="how old are you"):
                self.text.insert(END,'\n\n'+'Bot : i am just a machine, not human')
            elif(self.entry.get()=="what is lbph"):
                self.text.insert(END,'\n\n'+'Bot : LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person.')
            elif(self.entry.get()=="how to use app"):
                self.text.insert(END,'\n\n'+'Bot : step 1 -> Login my app , if your not account , first register yourself, after login. \n step2 -> Go to Student Details page, and provide student details with photo sample.  \n step 3-> Train your data using train data window.\n final step -> After trained data go to face detector and marked your attendence with open camera , if you show the attendenvce status(present or not) go to attence page and import attendence.csv file. your attendence show there. \n')
            elif(self.entry.get()=="what is face recognition"):
                self.text.insert(END,'\n\n'+'Bot : Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition systems can be used to identify people in photos, videos, or in real-time. ')
            elif(self.entry.get()=="what is opencv"):
                self.text.insert(END,'\n\n'+'Bot : OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems')
            elif(self.entry.get()=="4 steps to use app"):
                self.text.insert(END,'\n\n'+'Bot : step1 -> Enter student data with photo sample \n step2 -> Train the data \n step3-> face recognize in camera \n step4 -> show your attendance in attendence.csv file')
            elif(self.entry.get()=="advantage"):
                self.text.insert(END,'\n\n'+'Bot : 1. Better Communication \n 2. save time and money \n 3. Energy Saving \n 4. No Paperwork is required \n 5.Business Opportunities')
            elif(self.entry.get()=="modules"):
                self.text.insert(END,'\n\n'+'Bot : \n Modules :- \n 1. Python \n 2. OpenCV  \n 3. Tk \n  4. LBPH FaceRecognizer Algorithm \n ')
            elif(self.entry.get()=="scope"):
                self.text.insert(END,'\n\n'+'Bot : Provides an automated attendance system that is practical, reliable and eliminate disturbance and time loss of traditional attendance systems. \n • Present a system that can accurately evaluate student’s performance depending on their recorded attendance rate')
            elif(self.entry.get()=="what is facial recognition attendance system"):
                self.text.insert(END,'\n\n'+'Bot : A facial recognition attendance system uses facial recognition technology to identify and verify a person using the person''s facial features and automatically mark attendance. The software can be used for different groups of people such as employees, students, etc. The system records and stores the data in real-time.')
            elif(self.entry.get()=="bye"):
                self.text.insert(END,'\n\n'+'Bot : Bye, Nice to chat you !')
            
            
            

            
            
            else:
                self.text.insert(END,'\n\n'+'Bot : Sorry, I did not get it .')

    
                
            




if __name__ == "__main__":
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()