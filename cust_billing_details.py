from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog
from PIL import Image , ImageTk
from tkinter import ttk
import mysql.connector


from datetime import datetime
import webbrowser
import urllib.parse
import tempfile
import os

class booking_status:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+183")
        self.root.title("Guest Room Booking")
        self.dummy_frame=""
        
        
        current_date=datetime.now().strftime("%d-%m-%Y")

        #variable creation
        self.book_id=StringVar()
        self.check_in=StringVar()
        self.check_in.set(current_date)
        self.check_out=StringVar()
        self.room_type=StringVar()
        self.room_avl=StringVar()
        self.dish=StringVar()
        self.duration=StringVar()
        self.roomprice=StringVar()
        self.dishprice=StringVar()
        self.tax=StringVar()
        self.amt=StringVar()
        self.pay_time=StringVar()
        self.pay_status=StringVar()


        self.biframe=""

        self.phone_no=StringVar()

        self.hide_frame=""
        self.date_search=StringVar()
        self.income_set=StringVar()
        self.photo10=""

        #(self.con_no,self.check_in,self.check_out,self.room_type,self.room_avl,self.dish,self.duration,self.roomprice,self.dishprice,self.tax,self.amt,self.pay_time)

        #heading for room booking status
        title=Label(self.root,text="Room Booking Status",font=("times new roman",30,"bold"),bg="black",fg="white",bd=1,relief=RIDGE)
        title.place(x=0,y=0,width=1550,height=50)


        #frame creation for guest detail
        guest_frame=LabelFrame(self.root,fg="purple",text="Room Allotment",bd=2,relief=RIDGE,font=("times new roman",17,"bold"),padx=2)
        guest_frame.place(x=10,y=50,height=180,width=1100)


        #label creation and textbox  creation
        
        label_book_num=Label(guest_frame,text="Booking_id:",font=("new times roman",15,"italic"))
        label_book_num.place(x=10,y=10)
        inp_num=Entry(guest_frame,textvariable=self.book_id,font=("new times roman",15,"italic"),width=15)
        inp_num.place(x=130,y=10)

        #eye icon
        eye_img=Image.open("C:\\hotel management\\image\\eye.jpg")
        eye_resi=eye_img.resize((40,22),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(eye_resi)
        eye_button=Button(guest_frame,command=self.bind_button_eye,image=self.photo1,bd=0,cursor="hand2")
        eye_button.place(x=258,y=13)



        label_gue_checkin=Label(guest_frame,text="Check_in Date:",font=("new times roman",15,"italic"))
        label_gue_checkin.place(x=370,y=10)
        inp_checkin=Entry(guest_frame,textvariable=self.check_in,font=("new times roman",15,"italic"),width=15)
        inp_checkin.place(x=520,y=10)



        label_gue_checkout=Label(guest_frame,text="Check_out Date:",font=("new times roman",15,"italic"))
        label_gue_checkout.place(x=760,y=10)
        inp_checkout=Entry(guest_frame,textvariable=self.check_out,font=("new times roman",15,"italic"),width=15)
        inp_checkout.place(x=920,y=10)

                
        label_gue_rtype=Label(guest_frame,text="Room Type:",font=("new times roman",15,"italic"))
        label_gue_rtype.place(x=10,y=100)
        self.inp_rtype=ttk.Combobox(guest_frame,textvariable=self.room_type,font=("new times roman",15,"italic"),width=14,state="readonly")
        self.inp_rtype["values"]=("Luxary","Duplex","Single")
        self.inp_rtype.current(0)
        self.inp_rtype.place(x=130,y=100)




        label_gue_avlroom=Label(guest_frame,text="Room Available:",font=("new times roman",15,"italic"))
        label_gue_avlroom.place(x=365,y=100)
        self.inp_avlroom=ttk.Combobox(guest_frame,textvariable=self.room_avl,font=("new times roman",15,"italic"),width=9,state="readonly")
        self.inp_avlroom["values"]=()
        self.inp_avlroom.place(x=520,y=100)

        eye_img=Image.open("C:\\hotel management\\image\\eye.jpg")
        eye_resi=eye_img.resize((40,24),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(eye_resi)
        eye_button=Button(guest_frame,command=self.display_room_no,image=self.photo2,bd=0,cursor="hand2")
        eye_button.place(x=646,y=103,height=23)





        label_gue_dish=Label(guest_frame,text="Dish:",font=("new times roman",15,"italic"))
        label_gue_dish.place(x=810,y=100)
        self.inp_dish=ttk.Combobox(guest_frame,textvariable=self.dish,font=("new times roman",15,"italic"),width=13,state="readonly")
        self.inp_dish["values"]=("All","Dinner","Lunch","Breakfast")
        self.inp_dish.current(0)
        self.inp_dish.place(x=920,y=100)


        #proceed button
        pro_button=Button(self.root,bd=2,command=self.proceed_button,cursor="hand2",text="Proceed",font=("new times roman",14,"bold italic"),width=10,fg="purple",bg="white")
        pro_button.place(x=490,y=240)


        #frame creation to calculate on basis of taken facility
        cal_frame=Frame(self.root,bd=2,relief=RIDGE)
        cal_frame.place(x=10,y=290,height=35,width=1100)


        label_gue_days_cal=Label(cal_frame,text="Duration:",font=("new times roman",14,"italic"))
        label_gue_days_cal.place(x=10,y=1)
        inp_days_cal=Entry(cal_frame,textvariable=self.duration,font=("new times roman",15,"italic"),width=5,state="readonly",bd=0)
        inp_days_cal.place(x=100,y=1)


        label_gue_rent=Label(cal_frame,text="Room Rent:",font=("new times roman",14,"italic"))
        label_gue_rent.place(x=178,y=1)
        inp_rent=Entry(cal_frame,textvariable=self.roomprice,font=("new times roman",15,"italic"),width=8,state="readonly",bd=0)
        inp_rent.place(x=290,y=1)



        
        label_gue_dish=Label(cal_frame,text="Food:",font=("new times roman",14,"italic"))
        label_gue_dish.place(x=410,y=1)
        inp_dish=Entry(cal_frame,textvariable=self.dishprice,font=("new times roman",15,"italic"),width=8,state="readonly",bd=0)
        inp_dish.place(x=470,y=1)



        label_gue_tax=Label(cal_frame,text="Payable Tax:",font=("new times roman",15,"italic"))
        label_gue_tax.place(x=588,y=1)
        inp_tax_cal=Entry(cal_frame,textvariable=self.tax,font=("new times roman",15,"italic"),width=8,state="readonly",bd=0)
        inp_tax_cal.place(x=720,y=1)
        


        label_gue_total=Label(cal_frame,text="Payable Amount:",font=("new times roman",15,"italic"))
        label_gue_total.place(x=823,y=1)
        inp_total_cal=Entry(cal_frame,textvariable=self.amt,font=("new times roman",15,"italic"),width=9,state="readonly",bd=0)
        inp_total_cal.place(x=980,y=1)
        

        #add,reset button
        
        #add_button=Button(self.root,bd=2,command=self.add_button,cursor="hand2",text="Add",font=("new times roman",14,"italic"),width=10,fg="purple",bg="white")
        #add_button.place(x=190,y=350)

        
        self.reset_button=Button(self.root,command=self.reset_but,bd=2,cursor="hand2",text="Reset",font=("new times roman",14,"bold italic"),width=10,fg="purple",bg="white")
        self.reset_button.place(x=490,y=350)

                
        self.hidden_button=Button(self.root,command=self.hide_personal_info,bd=0,cursor="hand2",text="",font=("new times roman",14,"italic"),width=10)
        self.hidden_button.place(x=900,y=350)
        



        #table view frame
        table_frame=LabelFrame(self.root,fg="purple",text="Guest Room Booking Detail",bd=2,relief=RIDGE,font=("times new roman",17,"bold"),padx=2)
        table_frame.place(x=10,y=400,height=195,width=1100)

        details_table=Frame(table_frame,bd=0,relief=RIDGE)
        details_table.place(x=0,y=0,height=165,width=1090)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Booking_id","cont_no","check_in","check_out","room_type","room_book","dish","duration","room_rent","food_rent","payable_tax","payable_amt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)


        self.Cust_Details_Table.heading("Booking_id",text="Booking Id")
        self.Cust_Details_Table.heading("cont_no",text="Contact No")
        self.Cust_Details_Table.heading("check_in",text="Check In")
        self.Cust_Details_Table.heading("check_out",text="Check Out")
        self.Cust_Details_Table.heading("room_type",text="Room Type")
        self.Cust_Details_Table.heading("room_book",text="Room No")
        self.Cust_Details_Table.heading("dish",text="Dish")
        self.Cust_Details_Table.heading("duration",text="Duration")
        self.Cust_Details_Table.heading("room_rent",text="Room Rent")
        self.Cust_Details_Table.heading("food_rent",text="Food Rent")
        self.Cust_Details_Table.heading("payable_tax",text="Payable Tax")
        self.Cust_Details_Table.heading("payable_amt",text="Paid Amount")
        
        

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Booking_id",width=97)
        self.Cust_Details_Table.column("cont_no",width=97)
        self.Cust_Details_Table.column("check_in",width=97)
        self.Cust_Details_Table.column("check_out",width=97)
        self.Cust_Details_Table.column("room_type",width=97)
        self.Cust_Details_Table.column("room_book",width=97)
        self.Cust_Details_Table.column("dish",width=97)
        self.Cust_Details_Table.column("duration",width=97)
        self.Cust_Details_Table.column("room_rent",width=97)
        self.Cust_Details_Table.column("food_rent",width=97)
        self.Cust_Details_Table.column("payable_tax",width=97)
        self.Cust_Details_Table.column("payable_amt",width=97)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_guest_data)

        self.show_guest_data()
        #pay frame
        pay_frame=Frame(self.root,bd=2,relief=RIDGE)
        pay_frame.place(x=1120,y=230,height=170,width=400)

        pay_head_label=Label(pay_frame,bd=2,text="Payment",font=("new times roman",16,"italic"),fg="purple")
        pay_head_label.place(x=0,y=0)

        total_amt_label=Label(pay_frame,bd=0,text="Total Amount to be Paid:  ",font=("new times roman",14,"italic"),fg="black")
        total_amt_label.place(x=20,y=50)

        entry_amt_box=Entry(pay_frame,textvariable=self.pay_time,bd=0,font=("new times roman",16,"italic"),width=10,fg="black",state="readonly")
        entry_amt_box.place(x=250,y=50)
        

        

        self.combo_dummy_pay=ttk.Combobox(pay_frame,textvariable=self.pay_status,font=("new times roman",14,"italic"),width=7,state="disabled")
        self.combo_dummy_pay["values"]=("Unpaid","Paid")
        self.combo_dummy_pay.current(0)
        self.combo_dummy_pay.place(x=145,y=85)
        
        
        pay_button=Button(pay_frame,bd=2,command=self.pay_button,cursor="hand2",text="Pay",font=("new times roman",10,"bold italic"),width=10,fg="purple",bg="white")
        pay_button.place(x=70,y=130)

        
        bill_button=Button(pay_frame,bd=2,command=self.bill_frame,cursor="hand2",text="Bill",font=("new times roman",10,"bold italic"),width=10,fg="purple",bg="white")
        bill_button.place(x=240,y=130)





        
        #table browse frame
        browse_frame=LabelFrame(self.root,fg="purple",text="Browse By",bd=2,relief=RIDGE,font=("times new roman",17,"bold"))
        browse_frame.place(x=1120,y=400,height=195,width=400)

        self.guest_check=StringVar()
        self.see_all=StringVar()

        combo_opt=ttk.Combobox(browse_frame,textvariable=self.guest_check,font=("times new roman",17,"italic"),width=10,state="readonly")
        combo_opt["values"]=("Booking_id","Room_no","Check_In","Room_Type")
        combo_opt.current(0)
        combo_opt.place(x=20,y=20)

        gue_search=Entry(browse_frame,textvariable=self.see_all,font=("times new roman",17,"italic"),width=11)
        gue_search.place(x=250,y=20)


        #check button inside browse frame
        check_button=Button(browse_frame,text="Check",command=self.check_display,cursor="hand2",font=("times new roman",15,"bold italic"),width=8,fg="purple",bg="white")
        check_button.place(x=90,y=90)

        see_button=Button(browse_frame,command=self.show_guest_data,cursor="hand2",text="See All",font=("times new roman",15,"bold italic"),width=8,fg="purple",bg="white")
        see_button.place(x=230,y=90)



        self.show_guest_data()


    def proceed_button(self):
        if self.book_id.get() == "" or self.check_in.get() == "" or self.check_out.get() == "" or self.room_type.get() == "" or self.room_avl.get() == "" or self.dish.get() == "":
            mb.showerror("Error", "All Fields are Required", parent=self.root)
            return

        try:
            # Check if the Booking ID already exists
            mysql_connect = mysql.connector.connect(
                host="localhost", user="root", password="Mysql@12345", database="hotelmangement")
            mysql_control = mysql_connect.cursor()
            mysql_control.execute(
                "SELECT Booking_id FROM room WHERE Booking_id=%s", (self.book_id.get(),))
            row = mysql_control.fetchone()
            mysql_connect.commit()
            mysql_connect.close()

            if row is not None:
                mb.showwarning("Warning", "Room is already booked for this Booking ID", parent=self.root)
                return

            # Calculate Duration
            try:
                start = datetime.strptime(self.check_in.get(), "%d-%m-%Y")
                end = datetime.strptime(self.check_out.get(), "%d-%m-%Y")
                no_days = (end - start).days
                if no_days <= 0:
                    mb.showerror("Error", "Check-out date must be after Check-in date", parent=self.root)
                    return
                self.duration.set(str(no_days))
            except Exception as e:
                mb.showerror("Date Error", f"Date must be in 'dd-mm-yyyy' format\n{str(e)}", parent=self.root)
                return

            # Calculate Room Rent
            rate = {"Luxary": 1100, "Single": 300, "Duplex": 600}
            room_rent = rate.get(self.room_type.get(), 0)
            total_room = room_rent * no_days
            self.roomprice.set(str(total_room))

            # Calculate Dish Cost
            dish_rate = 300 if self.dish.get() == "All" else 100
            total_dish = dish_rate * no_days
            self.dishprice.set(str(total_dish))

            # Tax and Total
            tax = 0.05 * (total_room + total_dish)
            total = total_room + total_dish + tax
            self.tax.set(str(round(tax, 2)))
            self.amt.set(str(round(total, 2)))
            self.pay_time.set(str(round(total, 2)))

        except Exception as e:
            mb.showerror("System Error", f"An unexpected error occurred:\n{str(e)}", parent=self.root)


    

    def pay_button(self):
        if self.pay_time.get()=="":
            mb.showerror("Error","First complete room allotment Procedure",parent=self.root)
        else:
            if self.pay_status.get()!="Paid":
                #print(self.pay_status.get())
                var1=mb.askyesno("Payment","Guest wanted to pay the dues?",parent=self.root)
                #print("askyesno",var1,type(var1),type(str(var1)))
                if str(var1)!="False":
                    var=mb.askyesno("Payment","Has the guest already completed the payment",parent=self.root)
                    if str(var)!="False":
                        self.combo_dummy_pay.current(1)
                        mb.showinfo("Success","Payment done sucessfully",parent=self.root)
                        self.add_button()
                    else:
                        mb.showinfo("Payment","first ask guest to complete the payment",parent=self.root)
                else:
                    mb.showinfo("Payment","first ask guest to complete the payment",parent=self.root)
            else:
                    mb.showinfo("Success","Payment already Done",parent=self.root)
                
    def add_button(self):
            try:

                
                
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Phone from guest where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                mysql_connect.commit()
                mysql_connect.close()


                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                    self.book_id.get(),
                    row[0],
                    self.check_in.get(),
                    self.check_out.get(),
                    self.room_type.get(),
                    self.room_avl.get(),
                    self.dish.get(),
                    self.duration.get(),
                    self.roomprice.get(),
                    self.dishprice.get(),
                    self.tax.get(),
                    self.amt.get()
                    ))

                mysql_connect.commit()
                mysql_connect.close()
            
                                                                                                     
                mb.showinfo("success","Room Booked Sucessfully",parent=self.root)
                self.show_guest_data()
            except Exception as es:
                mb.showwarning("Warning",f"Some thing went wrong:{str(es)}")

    
    def show_guest_data(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute("select * from room")
        rows=mysql_control.fetchall()
        #print(len(rows))
        #print(rows)
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,value=i)
            mysql_connect.commit()
            mysql_connect.close()


    def reset_but(self):
        self.book_id.set("")
        self.room_avl.set("")
        current_date=datetime.now().strftime("%d-%m-%Y")
        self.check_in.set(current_date)
        self.check_out.set("")
        self.inp_rtype.current(0)
        self.inp_dish.current(0)
        self.combo_dummy_pay.current(0)
        self.duration.set("")
        self.roomprice.set("")
        self.dishprice.set("")
        self.tax.set("")
        self.amt.set("")
        self.pay_time.set("")
        if self.dummy_frame!="":
            self.dummy_frame.destroy()

    def display_data_in_right_above_frame(self):
        if self.book_id.get()=="":
            return 1
        else:
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            mysql_control.execute(("select Guest_name from guest where Booking_id=%s"),(self.book_id.get(),))
            row=mysql_control.fetchone()
            mysql_connect.commit()
            mysql_connect.close()
            if row==None:
                return 0
            else:
                #guest fetching detail frame
                #998876756
                self.dummy_frame=Frame(self.root,bd=2,relief=RIDGE)
                self.dummy_frame.place(x=1120,y=60,height=170,width=400)

                name_label=Label(self.dummy_frame,text="Name:",font=("new times roman",14,"italic"))
                name_label.place(x=10,y=0)
                show_name=Label(self.dummy_frame,text=row[0],font=("new times roman",14,"italic"))
                show_name.place(x=140,y=0)


                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Booking_id from guest where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                mysql_connect.commit()
                mysql_connect.close()

                
                bid_label=Label(self.dummy_frame,text="Booking Id:",font=("new times roman",14,"italic"))
                bid_label.place(x=10,y=32)
                bid_name=Label(self.dummy_frame,text=row[0],font=("new times roman",14,"italic"))
                bid_name.place(x=140,y=32)

                
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Phone from guest where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                mysql_connect.commit()
                mysql_connect.close()


                
                
                phone_label=Label(self.dummy_frame,text="Phone No:",font=("new times roman",14,"italic"))
                phone_label.place(x=10,y=67)
                phone_name=Label(self.dummy_frame,text=row[0],font=("new times roman",14,"italic"))
                phone_name.place(x=140,y=67)


                
                
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Email from guest where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                mysql_connect.commit()
                mysql_connect.close()

   
                
                email_label=Label(self.dummy_frame,text="Email:",font=("new times roman",14,"italic"))
                email_label.place(x=10,y=102)
                email_data=Label(self.dummy_frame,text=row[0],font=("new times roman",14,"italic"))
                email_data.place(x=140,y=102)
            
                
                
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Address from guest where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                mysql_connect.commit()
                mysql_connect.close()


                
                
                address_label=Label(self.dummy_frame,text="Address:",font=("new times roman",14,"italic"))
                address_label.place(x=10,y=135)
                address_data=Label(self.dummy_frame,text=row[0],font=("new times roman",14,"italic"))
                address_data.place(x=140,y=135)
            

            
    
    def bind_button_eye(self):
            res=self.display_data_in_right_above_frame()
            if res==0:
                mb.showerror("Error","Guest is not registered",parent=self.root)
                mb.showinfo("Register","First register guest detail",parent=self.root)
            elif res==1:
                mb.showerror("Error","Please enter Guest Booking id",parent=self.root)
                
            else:
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute(("select Booking_id from room where Booking_id=%s"),(self.book_id.get(),))
                row=mysql_control.fetchone()
                #print(row)
                mysql_connect.commit()
                mysql_connect.close()
                if row==None:
                    mb.showinfo("Status","Room is not Booked",parent=self.root)
                else:
                    mb.showinfo("Status","Room is already booked",parent=self.root) 
    def get_guest_data(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.book_id.set(row[0])
        self.check_in.set(row[2])
        self.check_out.set(row[3])
        self.inp_rtype.set(row[4])
        self.room_avl.set(row[5])
        self.inp_dish.set(row[6])
        self.duration.set(row[7])
        self.roomprice.set(row[8])
        self.dishprice.set(row[9])
        self.tax.set(row[10])
        self.amt.set(row[11])
        #self.pay_time.set("0.0")
        self.pay_time.set(self.amt.get())
        self.combo_dummy_pay.current(1)
        self.display_data_in_right_above_frame()
            
    def check_display(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select * from room where {}  LIKE %s".format(str(self.guest_check.get()))
        mysql_control.execute(query,('%'+str(self.see_all.get())+'%',))
        

        rows=mysql_control.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            mysql_connect.commit()
            mysql_connect.close()

    #*****************Bill related***********************
    def bill_frame(self):
        if self.book_id.get()=="" or self.check_in.get()=="" or self.check_out.get()=="" or self.room_type.get()=="" or self.room_avl.get()=="" or self.dish.get()=="":
            mb.showerror("Error","First complete room allotment Procedure",parent=self.root)

        elif self.pay_status.get()=="Unpaid":
            mb.showerror("Error","First ask Guest for a payment",parent=self.root)
        else:
            ''' 
            self.book_id.get(),
            row[0],
            self.check_in.get(),
            self.check_out.get(),
            self.room_type.get(),
            self.room_avl.get(),
            self.dish.get(),
            self.duration.get(),
            self.roomprice.get(),
            self.dishprice.get(),
            self.tax.get(),
            self.amt.get()
           ''' 


        
            self.biframe=Frame(self.root,bd=5,relief=RIDGE)
            self.biframe.place(x=0,y=0,width=338,height=420)


            exit_button=Button(self.biframe,command=self.bill_frame_close,text="Close",cursor="hand2",font=("new times roman",10,"italic"),bg="white",fg="black",width=8)
            exit_button.place(x=90,y=375)
            
            printb_button=Button(self.biframe,command=self.print_bill,text="Print Bill",cursor="hand2",font=("new times roman",10,"italic"),bg="white",fg="black",width=8)
            printb_button.place(x=180,y=375)

            phone_tb=Entry(self.biframe,width=15,textvariable=self.phone_no)
            phone_tb.place(x=62,y=334,height=25)
            print_button=Button(self.biframe,command=self.send_invoice,cursor="hand2",text="Send Bill",font=("new times roman",10,"italic"),bg="white",fg="black",width=8)
            print_button.place(x=185,y=330)

            label_h_name=Label(self.biframe,text="HOTEL VIP",font=("new times roman",15,"bold"),fg="black")
            label_h_name.place(x=110,y=0)



            label_h_bookid=Label(self.biframe,text="Booking Id:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_bookid.place(x=10,y=30)
            label_h_bookid=Label(self.biframe,text=self.book_id.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_bookid.place(x=87,y=30)

            

            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            mysql_control.execute(("select Guest_name from guest where Booking_id=%s"),(self.book_id.get(),))
            row=mysql_control.fetchone()
            mysql_connect.commit()
            mysql_connect.close()
            label_h_gname=Label(self.biframe,text="Guest Name:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname.place(x=10,y=49)
            label_h_gname=Label(self.biframe,text=row[0],font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname.place(x=91,y=49)


            
            label_h_bdate=Label(self.biframe,text="Date:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_bdate.place(x=190,y=30)
            label_h_bdate_dis=Label(self.biframe,text=self.check_in.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_bdate_dis.place(x=237,y=30)


            
                
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            mysql_control.execute(("select Phone from guest where Booking_id=%s"),(self.book_id.get(),))
            row1=mysql_control.fetchone()
            mysql_connect.commit()
            mysql_connect.close()
            label_h_gname=Label(self.biframe,text="Phone:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname.place(x=190,y=49)
            label_h_gname_dis=Label(self.biframe,text=row1[0],font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname_dis.place(x=242,y=49)


            label_h_gname=Label(self.biframe,text="CheckIn:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname.place(x=10,y=68)
            label_h_gname_dis=Label(self.biframe,text=self.check_in.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname_dis.place(x=68,y=68)


            
            label_h_gname=Label(self.biframe,text="CheckOut:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_gname.place(x=190,y=68)
            label_h_gname_dis=Label(self.biframe,text=self.check_out.get(),font=("new times roman",9,"bold italic"),fg="black")
            label_h_gname_dis.place(x=260,y=68)

            
            label_h_ser=Label(self.biframe,text="Service",font=("new times roman",10,"bold italic"),fg="black")
            label_h_ser.place(x=10,y=100)



            
            label_h_faci=Label(self.biframe,text="Facility\n Opt",font=("new times roman",10,"bold italic"),fg="black")
            label_h_faci.place(x=75,y=100)

            
            label_h_price=Label(self.biframe,text="Price",font=("new times roman",10,"bold italic"),fg="black")
            label_h_price.place(x=141,y=100)
            cal=int(self.roomprice.get())//int(self.duration.get())
            label_h_price=Label(self.biframe,text=cal,font=("new times roman",10,"bold italic"),fg="black")
            label_h_price.place(x=141,y=140)
            cal=int(self.dishprice.get())//int(self.duration.get())
            label_h_price=Label(self.biframe,text=cal,font=("new times roman",10,"bold italic"),fg="black")
            label_h_price.place(x=141,y=190)

            label_h_dur=Label(self.biframe,text="Duration",font=("new times roman",10,"bold italic"),fg="black")
            label_h_dur.place(x=183,y=100)
            label_h_dur=Label(self.biframe,text=self.duration.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_dur.place(x=204,y=140)
            label_h_dur=Label(self.biframe,text=self.duration.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_dur.place(x=204,y=190)

            
            label_h_tot=Label(self.biframe,text="Total",font=("new times roman",10,"bold italic"),fg="black")
            label_h_tot.place(x=260,y=100)
            label_h_tot=Label(self.biframe,text=self.roomprice.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_tot.place(x=256,y=140)
            label_h_tot=Label(self.biframe,text=self.dishprice.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_tot.place(x=256,y=190)

            
            label_h_rtype=Label(self.biframe,text="Room \nType",font=("new times roman",10,"bold italic"),fg="black")
            label_h_rtype.place(x=10,y=140)
            label_h_faci=Label(self.biframe,text=self.room_type.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_faci.place(x=75,y=140)



            
            label_h_dtype=Label(self.biframe,text="Dish",font=("new times roman",10,"bold italic"),fg="black")
            label_h_dtype.place(x=10,y=190)
            label_h_faci=Label(self.biframe,text=self.dish.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_faci.place(x=75,y=190)


            
            
            label_h_rtax=Label(self.biframe,text="Tax:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_rtax.place(x=194,y=210)
            label_h_rtax=Label(self.biframe,text=self.tax.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_rtax.place(x=256,y=210)



            
            label_h_tpaid=Label(self.biframe,text="Paid Amount:",font=("new times roman",10,"bold italic"),fg="black")
            label_h_tpaid.place(x=10,y=235)
            label_h_tpaid=Label(self.biframe,text=self.amt.get(),font=("new times roman",10,"bold italic"),fg="black")
            label_h_tpaid.place(x=100,y=235)
            
            
            label_h_tpaid=Label(self.biframe,text="Helpline No:   06605-90786",font=("new times roman",10,"bold italic"),fg="black")
            label_h_tpaid.place(x=10,y=255)


            
            
            label_h_mess=Label(self.biframe,text="Your Comfort Is Our Priority",font=("new times roman",10,"bold italic"),fg="black")
            label_h_mess.place(x=70,y=280)

            
            
            label_h_mess1=Label(self.biframe,text="Visit us again soon! ",font=("new times roman",10,"bold italic"),fg="black")
            label_h_mess1.place(x=98,y=300)

            self.phone_no.set(row1[0])





        
    def bill_frame_close(self):
        self.biframe.destroy()
        

    def send_invoice(self):
        
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute(("select Guest_name from guest where Booking_id=%s"),(self.book_id.get(),))
        row=mysql_control.fetchone()
        mysql_connect.commit()
        mysql_connect.close()

        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute(("select Phone from guest where Booking_id=%s"),(self.book_id.get(),))
        row1=mysql_control.fetchone()
        mysql_connect.commit()
        mysql_connect.close()
        


        message=f"""                  HOTEL VIP

Booking id:{self.book_id.get()}

Date      :{self.check_in.get()}

Guest Name:{row[0]}
Phone no  :{row1[0]}
Check In  :{self.check_in.get()}
Check Out :{self.check_out.get()}
        
Room Type :{self.room_type.get()}
Dish      :{self.dish.get()}
        
Room Rent :{self.roomprice.get()}
Dish Price:{self.dishprice.get()}
Tax       :{self.tax.get()}
Total Amt :{self.amt.get()}

    Your Comfort Is Our Priority
        Visit us again soon!
        """
        phone=str(self.phone_no.get())
        if not phone.startswith("+"):
            phone = "+91"+phone

        # Encode message and open WhatsApp Web
        encoded_message = urllib.parse.quote(message)
        wa_link = f"https://wa.me/{phone.replace('+', '')}?text={encoded_message}"
        webbrowser.open(wa_link)
        
    def print_bill(self):
        
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute(("select Guest_name from guest where Booking_id=%s"),(self.book_id.get(),))
        row=mysql_control.fetchone()
        mysql_connect.commit()
        mysql_connect.close()

        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute(("select Phone from guest where Booking_id=%s"),(self.book_id.get(),))
        row1=mysql_control.fetchone()
        mysql_connect.commit()
        mysql_connect.close()
        


        bill_content=f"""                  HOTEL VIP

Booking id:{self.book_id.get()}

Date      :{self.check_in.get()}

Guest Name:{row[0]}
Phone no  :{row1[0]}
Check In  :{self.check_in.get()}
Check Out :{self.check_out.get()}
        
Room Type :{self.room_type.get()}
Dish      :{self.dish.get()}
        
Room Rent :{self.roomprice.get()}
Dish Price:{self.dishprice.get()}
Tax       :{self.tax.get()}
Total Amt :{self.amt.get()}

    Your Comfort Is Our Priority
        Visit us again soon!
        """


        # Create a temporary file for the bill
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
            f.write(bill_content.encode('utf-8'))
            temp_file = f.name

        # Send to printer (Windows-specific)
        try:
            os.startfile(temp_file, "print")
            mb.showinfo("Printing", "Bill sent to printer.",parent=self.root)
        except Exception as e:
            mb.showerror("Error", f"Could not print bill:\n{e}",parent=self.root)
    def display_room_no(self):
        room_type=self.room_type.get()
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select Room_No from rooms where Room_Type=%s"
        value=(room_type,)
        mysql_control.execute(query,value)
        room_no=mysql_control.fetchall()

        
        tu=()
        for i in room_no:
            tu=tu+(i[0],)
        mysql_connect.commit()
        mysql_connect.close()
        
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select Room_No from room where CURDATE()<str_to_date(Check_Out,'%Y-%m-%d') and Room_Type=%s"
        value=(room_type,)
        mysql_control.execute(query,value)
        room_no1=mysql_control.fetchall()
        mysql_connect.commit()
        mysql_connect.close()
        tu1=()
        
        for i in room_no1:
            tu1=tu1+(i[0],)

            
        tu2=()
        for i in tu:
            if i not in tu1:
                tu2=tu2+(i,)
        self.inp_avlroom["values"]=tu2
        if tu2!=():
            self.inp_avlroom.current(0)
        else:
            self.inp_avlroom["values"]=("Full(N/A)",)
            self.inp_avlroom.current(0)
        print(room_no)
        print(room_no1)
        print(tu2)

    def hide_personal_info(self):
        user_input=simpledialog.askstring("Welcome","Enter your Password",parent=self.root)
        if user_input=="Mysql@12345":
            mb.showinfo("Welcome","It contains some hidden info",parent=self.root)

            self.hide_frame=Frame(self.root,bd=2,relief=RIDGE)
            self.hide_frame.place(x=630,y=328,height=82,width=479)

                    
            label_revenue=Label(self.hide_frame,text="Income",font=("new times roman",16,"italic bold"),fg="purple")
            label_revenue.place(x=0,y=0)

            
            label_date=Label(self.hide_frame,text="Date:",font=("new times roman",13,"italic bold"))
            label_date.place(x=10,y=40)
            inp_date=Entry(self.hide_frame,textvariable=self.date_search,font=("new times roman",13,"italic"),width=10)
            inp_date.place(x=80,y=40)

            eye_img=Image.open("C:\\hotel management\\image\\eye.jpg")
            eye_resi=eye_img.resize((40,22),Image.Resampling.LANCZOS)
            self.photo10=ImageTk.PhotoImage(eye_resi)
            eye_button=Button(self.hide_frame,command=self.show_inc,image=self.photo10,bd=0,cursor="hand2")
            eye_button.place(x=180,y=40)


            label_rev_tot=Label(self.hide_frame,text="Total Income:",font=("new times roman",13,"italic bold"))
            label_rev_tot.place(x=240,y=40)
            inp_inc=Entry(self.hide_frame,textvariable=self.income_set,font=("new times roman",13,"italic"),width=10)
            inp_inc.place(x=370,y=40)

            
            eye_img=Image.open("C:\\hotel management\\image\\cross.jpg")
            eye_resi=eye_img.resize((40,22),Image.Resampling.LANCZOS)
            self.photo11=ImageTk.PhotoImage(eye_resi)
            eye_button=Button(self.hide_frame,command=self.remove_hidden,image=self.photo11,bd=0,cursor="hand2")
            eye_button.place(x=420,y=4)
            

            
        else:
            mb.showinfo("Restriction","Try again next time",parent=self.root)
    def show_inc(self):
        if self.date_search.get()=="":
            mb.showerror("Error","All fields Required",parent=self.root)
        else:
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            query="select Paid_Amount from room where Check_In=%s"
            value=(self.date_search.get(),)
            mysql_control.execute(query,value)
            s=0
            amo=mysql_control.fetchall()
            for i in amo:
                s=s+int(float(i[0]))
            self.income_set.set(str(s))
                
            mysql_connect.commit()
            mysql_connect.close()
    def remove_hidden(self):
        self.hide_frame.destroy()
        

            
        
if __name__=="__main__":
    win=Tk()
    app=booking_status(win)
    win.mainloop()
