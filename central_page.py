from tkinter import *
from tkinter import messagebox as mb
from PIL import Image , ImageTk

from cust_details import cust_detail
from cust_billing_details import booking_status
from room_page import room_page
from help_button import help_button
class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        #image upward
        img=Image.open("C:\\hotel management\\image\\hotel_logo.jpg")
        resize=img.resize((190,200),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(resize)

        label=Label(self.root,image=self.photo,bd=1,relief=RIDGE)
        label.place(x=0,y=0,width=190,height=150)

        # #image header
        img=Image.open("C:\\hotel management\\image\\back_hai.jpg")
        resize=img.resize((1380,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(resize)

        label=Label(self.root,image=self.photo1,bd=1,relief=RIDGE)
        label.place(x=190,y=0,width=1380,height=150)

        # #image of dashboard
        img=Image.open("C:\\hotel management\\image\\DASH_BG07.jpeg")
        resize=img.resize((1550,650),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(resize)

        label=Label(self.root,image=self.photo2,bd=1,relief=RIDGE)
        label.place(x=0,y=203,width=1550,height=650)

        
        #label for title
        label=Label(self.root,text="HOTEL    MANAGEMENT    SYSTEM",font=("new times roman",30,"italic bold"),bd=3,fg="white",bg="black")
        label.place(x=0,y=150,width=1550)

        #buttons
        customer_but=Button(self.root,command=self.cust_details,text="Guest",font=("times new roman",40,"bold"),bg="black",fg="violet",bd=5,cursor="hand2",activeforeground="black",activebackground="grey")
        #customer_but.place(x=30,y=250)
        customer_but.place(x=30,y=450)

        booking_but=Button(self.root,command=self.book_page,text="Booking",font=("times new roman",40,"bold"),bg="black",fg="lime green",bd=5,cursor="hand2",activeforeground="black",activebackground="grey")
        #booking_but.place(x=390,y=550)
        booking_but.place(x=350,y=450)

        room_but=Button(self.root,text="Room",command=self.room_page,font=("times new roman",40,"bold"),bg="black",fg="yellow",bd=5,cursor="hand2",activeforeground="black",activebackground="grey")
        #room_but.place(x=700,y=250)
        room_but.place(x=700,y=450)

        help_but=Button(self.root,text="Help",command=self.help_page,font=("times new roman",40,"bold"),bg="black",fg="cyan",bd=5,cursor="hand2",activeforeground="black",activebackground="grey")
        #help_but.place(x=1020,y=550)
        help_but.place(x=1020,y=450)

        log_out_but=Button(self.root,text="Logout",command=self.logout,font=("times new roman",40,"bold"),bg="black",fg="orange",bd=5,cursor="hand2",activeforeground="black",activebackground="grey")
        #log_out_but.place(x=1300,y=250)
        log_out_but.place(x=1300,y=450)

        #function for customer detail
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_detail(self.new_window)
    def book_page(self):
        self.new_window=Toplevel(self.root)
        self.app=booking_status(self.new_window)
    def room_page(self):
        self.new_window=Toplevel(self.root)
        self.app=room_page(self.new_window)
    def help_page(self):
        self.new_window=Toplevel(self.root)
        self.app=help_button(self.new_window)
    def logout(self):
        self.root.destroy()
        
    
    
        




if __name__=="__main__":
    root=Tk()    #it is tool kit and it is used provide window where you can use widgets 
    app=dashboard(root)
    root.mainloop()