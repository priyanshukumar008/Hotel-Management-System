from tkinter import *
from tkinter import messagebox as mb
from PIL import Image , ImageTk
from tkinter import ttk
import mysql.connector
import random


class cust_detail:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+183")
        self.root.title("Guest Detail")

        #variable creation
        
        self.book_id=StringVar()
        self.y=random.randint(10000,99999)
        self.book_id.set(str(self.y))
        self.guest_name=StringVar()
        self.guest_gender=StringVar()
        self.guest_proof=StringVar()
        self.guest_id=StringVar()
        self.guest_phone=StringVar()
        self.guest_email=StringVar()
        self.guest_national=StringVar()
        self.guest_address=StringVar()

        #(self.book_id,self.guest_name,self.guest_gender,self.guest_proof,self.guest_id,self.guest_phone,self.guest_email,self.guest_national,self.guest_address)
        

        
        #label for title
        label=Label(self.root,text="Guest Detail",font=("new times roman",30,"bold"),bd=3,fg="white",bg="black")
        label.place(x=0,y=0,width=1550)

        #frame creation
        frame=LabelFrame(self.root,bd=2,text="Guest Details",font=("new times roman",16,"bold"),fg="purple")
        frame.place(x=10,y=55,height=225,width=1509)

        #textbox and label for customer detail
        label_cust_ref=Label(frame,text="Booking Ref:",font=("new times roman",15,"italic"))
        label_cust_ref.grid(row=0,column=0,pady=15)
        
        cust_det=Entry(frame,textvariable=self.book_id,font=("new times roman",15,"italic"),state="readonly")
        cust_det.grid(row=0,column=1,padx=100)


        label_cust_name=Label(frame,text="Customer Name:",font=("new times roman",15,"italic"))
        label_cust_name.grid(row=0,column=2,padx=10)
        
        cust_name=Entry(frame,textvariable=self.guest_name,font=("new times roman",15,"italic"))
        cust_name.grid(row=0,column=3,padx=90)



        label_cust_Gen=Label(frame,text="Gender:",font=("new times roman",15,"italic"))
        label_cust_Gen.grid(row=0,column=4,padx=10)
        
        cust_gen=ttk.Combobox(frame,textvariable=self.guest_gender,font=("new times roman",15,"italic"),state="readonly")
        cust_gen["values"]=("Male","Female","Transgender","Other")
        cust_gen.current(0)
        cust_gen.grid(row=0,column=5,padx=10)

        label_cust_id=Label(frame,text="Id Proof:",font=("new times roman",15,"italic"))
        label_cust_id.grid(row=1,column=0)
        
        cust_id=ttk.Combobox(frame,textvariable=self.guest_proof,font=("new times roman",14,"italic"),state="readonly")
        cust_id["values"]=("Aadhar Card","Pan Card","other")
        cust_id.current(0)
        cust_id.grid(row=1,column=1)


        label_cust_id_num=Label(frame,text="Id Number:",font=("new times roman",15,"italic"))
        label_cust_id_num.grid(row=1,column=2)

        cust_id_num=Entry(frame,textvariable=self.guest_id,font=("new times roman",15,"italic"))
        cust_id_num.grid(row=1,column=3)



        label_cust_phone=Label(frame,text="Phone:",font=("new times roman",15,"italic"))
        label_cust_phone.grid(row=1,column=4)
        
        cust_phone=Entry(frame,textvariable=self.guest_phone,font=("new times roman",15,"italic"))
        cust_phone.grid(row=1,column=5,padx=6)



        label_cust_email=Label(frame,text="Email:",font=("new times roman",15,"italic"))
        label_cust_email.grid(row=2,column=0)
        
        cust_email=Entry(frame,textvariable=self.guest_email,font=("new times roman",15,"italic"))
        cust_email.grid(row=2,column=1,padx=0)


        label_cust_nat=Label(frame,text="Nationality",font=("new times roman",15,"italic"))
        label_cust_nat.grid(row=2,column=2)
        
        cust_nat=ttk.Combobox(frame,textvariable=self.guest_national,font=("new times roman",15,"italic"),state="readonly")
        cust_nat["values"]=("Indian","Non-Indian")
        cust_nat.current(0)
        cust_nat.grid(row=2,column=3,padx=10,pady=15)


        label_cust_add=Label(frame,text="Address:",font=("new times roman",15,"italic"))
        label_cust_add.grid(row=2,column=4,padx=3)
        
        cust_add=Entry(frame,textvariable=self.guest_address,font=("new times roman",15,"italic"))
        cust_add.grid(row=2,column=5,padx=10)



        #frame for a button
        frame_d=Frame(frame)
        frame_d.place(x=6,y=150,height=39,width=1490)

        #button for save,update,delete,reset
        but_save=Button(frame_d,command=self.insert_record,text="Save",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_save.grid(row=0,column=0,padx=180)

        but_update=Button(frame_d,command=self.update_guest_detail,text="Update",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_update.grid(row=0,column=1,padx=280)

        #but_delete=Button(frame_d,command=self.delete_guest_detail,text="Delete",bd=1,font=("new times roman",14,"bold"),bg="white",fg="purple",cursor="hand2")
        #but_delete.grid(row=0,column=2,padx=140)

        but_reset=Button(frame_d,text="Reset",command=self.reset_guest_detail,bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_reset.grid(row=0,column=3,padx=160)


        #table frame
        table_frame=LabelFrame(self.root,bd=2,text="View and Search Room Detail",font=("new times roman",16,"bold"),relief=RIDGE,fg="purple")
        table_frame.place(x=10,y=300,height=290,width=1509)

        #table detail show
        
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=16,y=14,height=234,width=1000)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Cust_ref","name","gender","Id Proof","Id Number","Phone","email","nation","add"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Cust_ref",text="Booking_id")
        self.Cust_Details_Table.heading("name",text="Guest Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("Id Proof",text="Id Proof")
        self.Cust_Details_Table.heading("Id Number",text="Id Number")
        self.Cust_Details_Table.heading("Phone",text="Phone")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nation",text="Nationality")
        self.Cust_Details_Table.heading("add",text="Address")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("Cust_ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("Id Proof",width=100)
        self.Cust_Details_Table.column("Id Number",width=100)
        self.Cust_Details_Table.column("Phone",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nation",width=100)
        self.Cust_Details_Table.column("add",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_guest_data)

        self.show_guest_data()

        #frame for search Engine
        search_frame=LabelFrame(table_frame,text="Browse by",font=("new times roman",17,"bold"),fg="purple",bd=2,relief=RIDGE)
        search_frame.place(x=1070,y=1,height=249,width=400)

        #combobox for searching

        self.check_guest=StringVar()
        self.see_all=StringVar()
        option_prov=ttk.Combobox(search_frame,textvariable=self.check_guest,font=("new times roman",14,"italic"),state="readonly",width=15)
        option_prov["values"]=("Phone","Booking_id")
        option_prov.current(0)
        option_prov.place(x=15,y=59)

        #text box
        
        search_value=Entry(search_frame,textvariable=self.see_all,font=("new times roman",14,"italic"),width=15)
        search_value.place(x=210,y=59)


        #Button for checking guest detail and see all data

        button_check=Button(search_frame,text="Check",command=self.check_display,font=("new times roman",14,"bold"),cursor="hand2",width=7,fg="purple",bg="white")
        button_check.place(x=60,y=130)

        see_button=Button(search_frame,text="See all",command=self.show_guest_data,font=("new times roman",14,"bold"),cursor="hand2",width=7,fg="purple",bg="white")
        see_button.place(x=240,y=130)



        
    def insert_record(self):
        if self.guest_name.get()=="" or self.guest_address.get()=="" or self.guest_phone=="" or self.guest_proof=="":
            mb.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute("insert into guest values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.book_id.get(),
                    self.guest_name.get(),
                    self.guest_gender.get(),
                    self.guest_proof.get(),
                    self.guest_id.get(),
                    self.guest_phone.get(),
                    self.guest_email.get(),
                    self.guest_national.get(),
                    self.guest_address.get()
                    ))
                mysql_connect.commit()
                self.show_guest_data()
                mysql_connect.close()
            
                                                                                                     
                mb.showinfo("success","Guest detail inserted Sucessfully",parent=self.root)
                self.show_guest_data()
            except Exception as es:
                mb.showwarning("Warning",f"Some thing went wrong:{str(es)}")
    def show_guest_data(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute("select *from guest")
        rows=mysql_control.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            mysql_connect.commit()
            mysql_connect.close()


    def get_guest_data(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.book_id.set(row[0])
        self.guest_name.set(row[1])
        self.guest_gender.set(row[2])
        self.guest_proof.set(row[3])
        self.guest_id.set(row[4])
        self.guest_phone.set(row[5])
        self.guest_email.set(row[6])
        self.guest_national.set(row[7])
        self.guest_address.set(row[8])

        
    def update_guest_detail(self):
        if self.guest_name.get()=="" or self.guest_proof.get()=="" or self.guest_email.get()=="" or self.guest_address.get()=="":
            mb.showerror("Error","All field required",parent=self.root)
        else:
                
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            mysql_control.execute("update guest set Guest_name=%s,Gender=%s,Id_proof=%s,Id_number=%s,Phone=%s,Email=%s,nationality=%s,address=%s where Booking_id=%s",(
                    self.guest_name.get(),
                    self.guest_gender.get(),
                    self.guest_proof.get(),   
                    self.guest_id.get(),
                    self.guest_phone.get(),
                    self.guest_email.get(),
                    self.guest_national.get(),
                    self.guest_address.get(),
                    self.book_id.get()
                    ))
            mysql_connect.commit()
            mysql_connect.close()
            mb.showinfo("Update","Guest Detail Updated Sucessfully",parent=self.root)
            self.show_guest_data()
             
                    


            
        
    def reset_guest_detail(self):
                
        self.y=random.randint(10000,99999)
        self.book_id.set(str(self.y))
        self.guest_name.set("")
        self.guest_id.set("")
        self.guest_phone.set("")
        self.guest_email.set("")
        self.guest_address.set("")

    def check_display(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select * from guest where {} LIKE %s".format(str(self.check_guest.get()))
        mysql_control.execute(query,('%'+str(self.see_all.get())+'%',))
            

        rows=mysql_control.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            mysql_connect.commit()
        mysql_connect.close()
    
    
        
if __name__=="__main__":
    root=Tk()    #it is tool kit and it is used provide window where you can use widgets 
    app=cust_detail(root)
    root.mainloop()


























    def check_display(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select * from room where {} LIKE %s".format(str(self.guest_check.get()))
        mysql_control.execute(query,('%'+str(self.see_all.get())+'%',))
            

        rows=mysql_control.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            mysql_connect.commit()
            mysql_connect.close()

        
            

def delete_guest_detail(self):
        ques=mb.askyesno("Delete Warning","Do you want to delete this customer",parent=self.root)
        print(ques)
        if ques>0:
            try:
                
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                query="delete from room where  Booking_id=%s"
                value=(self.book_id.get(),)
                mysql_control.execute(query,(self.book_id.get(),))
            except Exception as e:
                print("Error",e)
        else:
            if not delete_guest_detail:
                return
        mysql_connect.commit()
        mysql_connect.close()
        self.show_guest_data()
