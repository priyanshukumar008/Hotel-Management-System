from tkinter import *
class help_button:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+183")
        self.root.title("Help")

        #variable making
        self.cust_sup=StringVar()
        self.book_sup=StringVar()
        self.room_sup=StringVar()
        self.ent_dash=StringVar()
        self.ent_address=StringVar()


        

        #label for heading
        label=Label(self.root,text="Support",font=("new times roman",30,"bold"),bd=3,fg="white",bg="black")
        label.place(x=0,y=0,width=1550)

        #support frame for dashboard
        dash_frame=LabelFrame(self.root,text="Dashboard Related Support",font=("new times roman",16,"bold"),bd=2,fg="purple")
        dash_frame.place(x=10,y=70,width=1510,height=150)

        #buttons for dashboard
        guest_but=Button(dash_frame,command=self.guest_info,text="Guest",font=("new times roman",12,"bold"),bd=3,fg="black",bg="white",width=10)
        guest_but.place(x=10,y=9)

        booking_but=Button(dash_frame,command=self.booking_info,text="Booking",font=("new times roman",12,"bold"),bd=3,fg="black",bg="white",width=10)
        booking_but.place(x=420,y=9)
        
        roomm_but=Button(dash_frame,command=self.room_info,text="Room",font=("new times roman",12,"bold"),bd=3,fg="black",bg="white",width=10)
        roomm_but.place(x=910,y=9)

        logout_but=Button(dash_frame,command=self.logout_info,text="LogOut",font=("new times roman",12,"bold"),bd=3,fg="black",bg="white",width=10)
        logout_but.place(x=1370,y=9)

        #entry field for dashboard info
        ent_dash_help=Entry(dash_frame,textvariable=self.ent_dash,font=("new times roman",16,"bold"),state="readonly",bd=0)
        ent_dash_help.place(x=10,y=80,width=1400)



        #Support frame for Guest detail
        guest_frame=LabelFrame(self.root,bd=2,text="Guest Details Related Support",font=("new times roman",16,"bold"),fg="purple")
        guest_frame.place(x=10,y=260,height=225,width=500)

        #Support frame for Guest booking
        book_frame=LabelFrame(self.root,bd=2,text="Guest Booking Related Support",font=("new times roman",16,"bold"),fg="purple")
        book_frame.place(x=530,y=260,height=225,width=500)

        #support frame for room management
        room_frame=LabelFrame(self.root,bd=2,text="Room Management Support",font=("new times roman",16,"bold"),fg="purple")
        room_frame.place(x=1050,y=260,height=225,width=470)

        #buttons for guest details
        but_save=Button(guest_frame,command=self.cust_save,text="Save",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=10,y=35)

        but_save=Button(guest_frame,command=self.cust_update,text="Update",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=100,y=35)

        but_save=Button(guest_frame,command=self.cust_reset,text="Reset",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=205,y=35)

        but_save=Button(guest_frame,command=self.cust_check,text="Check",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=300,y=35)

        but_save=Button(guest_frame,command=self.cust_see,text="See all",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=405,y=35)



        #entry field
        ent_cust=Entry(guest_frame,textvariable=self.cust_sup,font=("new times roman",11,"bold"),state="readonly",bd=0)
        ent_cust.place(x=10,y=100,height=80,width=475)



        #buttons for booking details
        but_save=Button(book_frame,command=self.book_proceed,text="Proceed",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=10,y=35)

        but_save=Button(book_frame,command=self.book_reset,text="Reset",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=115,y=35)

        but_save=Button(book_frame,command=self.book_pay,text="Pay",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=200,y=35)

        but_save=Button(book_frame,command=self.book_bill,text="Bill",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=265,y=35)

        
        but_save=Button(book_frame,command=self.book_check,text="Check",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=320,y=35)

        but_save=Button(book_frame,command=self.book_see,text="See all",bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=410,y=35)


        #entry field
        ent_book=Entry(book_frame,textvariable=self.book_sup,font=("new times roman",11,"bold"),state="readonly",bd=0)
        ent_book.place(x=10,y=100,height=80,width=475)


        #buttons for room details
        but_save=Button(room_frame,text="Save",command=self.room_save,bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=10,y=35)

        but_save=Button(room_frame,text="Update",command=self.room_update,bd=1,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=130,y=35)

        but_save=Button(room_frame,text="Delete",bd=1,command=self.room_delete,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=260,y=35)

        but_save=Button(room_frame,text="Reset",bd=1,command=self.room_reset,font=("new times roman",14,"bold"),fg="black",bg="white",cursor="hand2")
        but_save.place(x=385,y=35)


        #entry field
        ent_room=Entry(room_frame,textvariable=self.room_sup,font=("new times roman",11,"bold"),state="readonly",bd=0)
        ent_room.place(x=10,y=100,height=80,width=450)


        #Software related support frame
        soft_frame=LabelFrame(self.root,bd=2,text="Software Related Support",font=("new times roman",16,"bold"),fg="purple")
        soft_frame.place(x=10,y=500,height=95,width=1510)

        label_soft=Label(soft_frame,bd=0,text="Contact Us",font=("new times roman",13,"bold"),fg="red")
        label_soft.place(x=10,y=10)


        label_soft=Label(soft_frame,bd=0,text="Gmail:  team_57@gmail.com",font=("new times roman",12,"bold"),fg="black")
        label_soft.place(x=150,y=30)


        label_soft=Label(soft_frame,bd=0,text="Helpline NO:  06660-10993",font=("new times roman",12,"bold"),fg="black")
        label_soft.place(x=500,y=30)

        
        label_soft=Label(soft_frame,bd=0,text="Offline Support Address",font=("new times roman",13,"bold"),fg="red")
        label_soft.place(x=820,y=10)

        
        label_soft=Label(soft_frame,bd=0,text="Shop name:Manual_To_Tech_Team_57",font=("new times roman",13,"bold"),fg="green")
        label_soft.place(x=757,y=30)

        #buttons for address
        
        but_save=Button(soft_frame,text="Bihar",command=self.bihar_info,bd=1,font=("new times roman",10,"bold"),fg="black",bg="white",cursor="hand2",width=10)
        but_save.place(x=1100,y=6)

        but_save=Button(soft_frame,text="Jharkhand",command=self.jharkhand_info,bd=1,font=("new times roman",10,"bold"),fg="black",bg="white",cursor="hand2",width=10)
        but_save.place(x=1200,y=6)

        but_save=Button(soft_frame,text="Oddisa",bd=1,command=self.oddisa_info,font=("new times roman",10,"bold"),fg="black",bg="white",cursor="hand2",width=10)
        but_save.place(x=1300,y=6)

        but_save=Button(soft_frame,text="Goa",bd=1,command=self.goa_info,font=("new times roman",10,"bold"),fg="black",bg="white",cursor="hand2",width=10)
        but_save.place(x=1400,y=6)

        #entry field for address
        ent_room=Entry(soft_frame,textvariable=self.ent_address,font=("new times roman",10,"bold"),state="readonly",bd=0)
        ent_room.place(x=1110,y=40,height=20,width=390)



        




        

    #function making for save,update,reset,check,seeall
    def cust_save(self):
        self.cust_sup.set("")
        self.cust_sup.set("This Button is used to succesfully record Guest details")

    def cust_update(self):
        self.cust_sup.set("")
        self.cust_sup.set("Select the guest detail from the table that you wanted to 'Update'")
    def cust_delete(self):
        self.cust_sup.set("")
        self.cust_sup.set("Select the guest detail  that you wanted to 'Delete'")
    def cust_reset(self):
        self.cust_sup.set("")
        self.cust_sup.set("This button will empty all entry field of customer details")
    
    def cust_check(self):
        self.cust_sup.set("")
        self.cust_sup.set("Click to verify Guest details")
    def cust_see(self):
        self.cust_sup.set("")
        self.cust_sup.set("View the complete list of Guest details")



    #function making  proceed,reset,pay,bill,check,see for booking
    def book_proceed(self):
        self.book_sup.set("")
        self.book_sup.set("Successfully calculate the price of facility opted by guest")

    def book_pay(self):
        self.book_sup.set("")
        self.book_sup.set("Pay to reserve room for the guest instantly")
    def book_bill(self):
        self.book_sup.set("")
        self.book_sup.set("Generate a printable version of the guest's bill")
    def book_reset(self):
        self.book_sup.set("")
        self.book_sup.set("This button will empty all entry field of booking details")
    def book_check(self):
        self.book_sup.set("")
        self.book_sup.set("Click to verify room or booking details")
    def book_see(self):
        self.book_sup.set("")
        self.book_sup.set("View the complete list of booking details")




    #function making  save,update,delete,reset for room
    def room_save(self):
        self.room_sup.set("")
        self.room_sup.set("This Button is used to succesfully record new room Detail")

    def room_update(self):
        self.room_sup.set("")
        self.room_sup.set("You can update existing room details of your Hotel")
    def room_delete(self):
        self.room_sup.set("")
        self.room_sup.set("Select the room detail from the table that you wanted to 'Delete'")
    def room_reset(self):
        self.room_sup.set("")
        self.room_sup.set("This button will empty all entry field of room details")


    #function making for dashboard buttons
    def guest_info(self):
        self.ent_dash.set("")
        self.ent_dash.set("Helps to manage guest related details")

    def booking_info(self):
        self.ent_dash.set("")
        self.ent_dash.set("It helps you to allocate room to the guest")
    def room_info(self):
        self.ent_dash.set("")
        self.ent_dash.set("Here you can manage room related operation")
    def logout_info(self):
        self.ent_dash.set("")
        self.ent_dash.set("This button helps Successfully logout from Dashboard")


    #function making for address buttons
    def bihar_info(self):
        self.ent_address.set("")
        self.ent_address.set("District:Nawada,behind ITI,Kali temple road,Kendua")

    def jharkhand_info(self):
        self.ent_address.set("")
        self.ent_address.set("District:Bokaro,jamshedpur,near softech solution,Golmuri")
    def oddisa_info(self):
        self.ent_address.set("")
        self.ent_address.set("District:Raniguri,after rustana house,govind road,Hisua")
    def goa_info(self):
        self.ent_address.set("")
        self.ent_address.set("District:Himani,near railway station,Kanpa")

       
        


if __name__=="__main__":
    window=Tk()
    software=help_button(window)
    window.mainloop()
