
        img_top = Image.open(r"images\facialrecognition.png")
        img_top = img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        self.btn2 = Button(self.root,image=self.photoimg_top,command=self.open_img4)
        self.btn2.place(x=0,y=55,height=325,width=1530)