from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox as mb
from central_page import dashboard

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_text=StringVar()
        self.var_text.set("admin")
        #image(big frame)
        image=Image.open("C:\\hotel management\\image\\DASH_BG003.jpg")
        resized_image=image.resize((1550,800),Image.Resampling.LANCZOS)
        sharpened_image=resized_image.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=3))
        self.photo=ImageTk.PhotoImage(resized_image)
        
        label=Label(self.root,image=self.photo,bd=4,relief=RIDGE)
        label.place(x=0,y=0,width=1550,height=800)

        #frame
        
        frame=Frame(self.root,bg="white")
        frame.place(x=640,y=250,height=380,width=250)


        
        
        #image01(big frame)
        image3=Image.open("C:\\hotel management\\image\\frame2.jpg")
        resized_image=image3.resize((100,100),Image.Resampling.LANCZOS)
        sharpened_image=resized_image.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=3))
        self.photoimg2=ImageTk.PhotoImage(resized_image)
        
        label=Label(frame,image=self.photoimg2,bd=0,relief=RIDGE)
        label.place(x=78,y=10)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="white",fg="red")
        get_str.place(x=55,y=110)


        #username label
        username_lbl=Label(frame,text="username",font=("times new roman",16,"bold"),bg="white",fg="red")
        username_lbl.place(x=55,y=145)

        self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
        self.txtuser.place(x=30,y=180)

        #password lebel
        password_labl=Label(frame,text="password",font=("times new roman",16,"bold"),bg="white",fg="red")
        password_labl.place(x=55,y=210)

        self.txtpass=ttk.Entry(frame,font=("times new roman",14,"bold"),show="*")
        self.txtpass.place(x=30,y=250)

        #user Icon
        image4=Image.open("C:\\hotel management\\image\\images.png")
        resized_image=image4.resize((20,20),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(resized_image)
        
        label=Label(image=self.photo3,bd=0,relief=RIDGE)
        label.place(x=670,y=402,width=20,height=20)
        #Password Icon
        image=Image.open("C:\\hotel management\\image\\image2.png")
        resized_image=image.resize((25,25),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(resized_image)
        
        label=Label(image=self.photo4,bd=0,relief=RIDGE)
        label.place(x=667,y=460,width=30,height=40)

        #Login button

        login_btn=Button(frame,command=self.login,text="Login",width=20,font=("times new roman",14,"bold"),bg="white",fg="red",bd=1,relief=RIDGE,activeforeground="red",activebackground="white",cursor="hand1")
        login_btn.place(x=85,y=290,width=80)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            mb.showerror("Error","all field required")
            self.txtuser.delete(0,tk.END)
            self.txtpass.delete(0,tk.END)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="123321":
            mb.showinfo("Success","welcome to manage your job")
            self.txtuser.delete(0,tk.END)
            self.txtpass.delete(0,tk.END)

            self.hotel_main_page()
            
        else:
            mb.showerror("Error","invalid user name and password")
            self.txtuser.delete(0,tk.END)
            self.txtpass.delete(0,tk.END)

    def hotel_main_page(self):
        self.new_window=Toplevel(self.root)
        self.app=dashboard(self.new_window)
            









if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()