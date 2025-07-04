from tkinter import *
from tkinter import messagebox as mb
from PIL import Image , ImageTk
from tkinter import ttk
import mysql.connector


class room_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+235")
        self.root.title("Room_Management")


        #variables
        self.floor_no=StringVar()
        self.room_no=StringVar()
        self.room_type=StringVar()

        self.inp_rtype=""

        #frame creation
        man_room_frame=LabelFrame(self.root,fg="purple",text="Manage Hotel Room",bd=2,relief=RIDGE,font=("times new roman",17,"bold"),padx=2)
        man_room_frame.place(x=10,y=0,height=260,width=1500)

        
        
        label_room_flr=Label(man_room_frame,text="Floor",font=("new times roman",17,"italic bold"))
        label_room_flr.place(x=10,y=10)
        inp_flr=Entry(man_room_frame,textvariable=self.floor_no,font=("new times roman",15,"italic"),width=15)
        inp_flr.place(x=160,y=10)

        label_room_no=Label(man_room_frame,text="Room No",font=("new times roman",17,"italic bold"))
        label_room_no.place(x=10,y=70)
        inp_rno=Entry(man_room_frame,textvariable=self.room_no,font=("new times roman",15,"italic"),width=15)
        inp_rno.place(x=160,y=70)

        label_room_type=Label(man_room_frame,text="Room Type",font=("new times roman",17,"italic bold"))
        label_room_type.place(x=10,y=130)
        self.inp_rtype=ttk.Combobox(man_room_frame,textvariable=self.room_type,font=("new times roman",15,"italic"),width=15,state="readonly")
        self.inp_rtype["values"]=("Luxary","Single","Duplex")
        self.inp_rtype.current(0)
        self.inp_rtype.place(x=160,y=130)



        #button for add,update,reset,delete

        but_save=Button(man_room_frame,command=self.insert_record,text="Save",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_save.place(x=10,y=180)

        but_update=Button(man_room_frame,command=self.update_room_detail,text="Update",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_update.place(x=205,y=180)

        but_delete=Button(man_room_frame,command=self.delete_room_detail,text="Delete",bd=1,font=("new times roman",14,"bold"),bg="white",fg="purple",cursor="hand2")
        but_delete.place(x=420,y=180)

        but_reset=Button(man_room_frame,text="Reset",command=self.reset_but,bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
        but_reset.place(x=610,y=180)


        #table frame
        table_frame=LabelFrame(self.root,bd=2,text="Room Details",font=("new times roman",16,"bold"),relief=RIDGE,fg="purple")
        table_frame.place(x=10,y=270,height=275,width=1000)

        #table detail show
        
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=10,y=0,height=240,width=975)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("floor","room_no","room_type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("floor",text="Floor No")
        self.Cust_Details_Table.heading("room_no",text="Room No")
        self.Cust_Details_Table.heading("room_type",text="Room Type")

        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("floor",width=100)
        self.Cust_Details_Table.column("room_no",width=100)
        self.Cust_Details_Table.column("room_type",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_guest_data)

        self.show_guest_data()


        
        #browse frame

        
        #table browse frame
        browse_frame=LabelFrame(self.root,fg="purple",text="Browse By",bd=2,relief=RIDGE,font=("times new roman",17,"bold"))
        browse_frame.place(x=1040,y=270,height=275,width=470)

        self.guest_check=StringVar()
        self.see_all=StringVar()

        combo_opt=ttk.Combobox(browse_frame,textvariable=self.guest_check,font=("times new roman",17,"italic"),width=10,state="readonly")
        combo_opt["values"]=("Room_No","Room_Type")
        combo_opt.current(0)
        combo_opt.place(x=20,y=60)

        gue_search=Entry(browse_frame,textvariable=self.see_all,font=("times new roman",17,"italic"),width=11)
        gue_search.place(x=250,y=60)


        #check button inside browse frame
        check_button=Button(browse_frame,text="Check",command=self.check_display,cursor="hand2",font=("times new roman",15,"bold"),width=8,fg="purple",bg="white")
        check_button.place(x=90,y=160)

        see_button=Button(browse_frame,command=self.show_guest_data,cursor="hand2",text="See All",font=("times new roman",15,"bold"),width=8,fg="purple",bg="white")
        see_button.place(x=230,y=160)

    def insert_record(self):
        if self.floor_no.get()=="" or self.room_no.get()=="" or self.room_type.get()=="":
            mb.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
                mysql_control=mysql_connect.cursor()
                mysql_control.execute("insert into rooms values(%s,%s,%s)",(
                    self.floor_no.get(),
                    self.room_no.get(),
                    self.room_type.get()
                    ))
                mysql_connect.commit()
                mysql_connect.close()
            
                                                                                                     
                mb.showinfo("success","Room detail inserted Sucessfully",parent=self.root)
                self.show_guest_data()
            except Exception as es:
                mb.showwarning("Warning",f"Some thing went wrong:{str(es)}")
  
    def show_guest_data(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        mysql_control.execute("select * from rooms")
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
        self.floor_no.set(row[0])
        self.room_no.set(row[1])
        self.room_type.set(row[2])

    def update_room_detail(self):
        if self.floor_no.get()=="" or self.room_no.get()=="" or self.room_type.get()=="":
            mb.showerror("Error","All field required",parent=self.root)
        else:
                
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            mysql_control.execute("update rooms set floor=%s,room_type=%s where room_no=%s",(
                    self.floor_no.get(),
                    self.room_type.get(),
                    self.room_no.get(),
                    ))
            mysql_connect.commit()
            mysql_connect.close()
            mb.showinfo("Update","Room Detail Updated Sucessfully",parent=self.root)
            self.show_guest_data()
    def reset_but(self):
        self.floor_no.set("")
        self.room_no.set("")
        self.inp_rtype.current(0)

            
    def delete_room_detail(self):
        ques=mb.askyesno("Delete Warning","Do you want to delete this customer",parent=self.root)
        if ques>0:
            mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
            mysql_control=mysql_connect.cursor()
            query="DELETE from rooms where room_No=%s"
            mysql_control.execute(query,(self.room_no.get(),))
        else:
            if not delete_room_detail:
                return
        mysql_connect.commit()
        mysql_connect.close()
        self.show_guest_data()
            
    def check_display(self):
        mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
        mysql_control=mysql_connect.cursor()
        query="select * from rooms where {}  LIKE %s".format(str(self.guest_check.get()))
        mysql_control.execute(query,('%'+str(self.see_all.get())+'%',))
            

        rows=mysql_control.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            mysql_connect.commit()
            mysql_connect.close()
            




if __name__=="__main__":
    win=Tk()
    app=room_page(win)
    win.mainloop()



































# # # import tkinter as tk
# # # from tkinter import ttk, messagebox
# # # import mysql.connector

# # # class HotelRoomManager:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Hotel Room Manager")
# # #         self.root.geometry("1550x800+0+183")

# # #         # MySQL connection (replace credentials)
# # #         self.db = mysql.connector.connect(
# # #             host="localhost",
# # #             user="root",
# # #             password="Mysql@12345",
# # #             database="hotelmangement"
# # #         )
# # #         self.cursor = self.db.cursor()

# # #         # ---- Manage Room Frame ----
# # #         manage_frame = tk.LabelFrame(root, text="Manage Room", padx=10, pady=10)
# # #         manage_frame.pack(fill="x", padx=10, pady=5)

# # #         tk.Label(manage_frame, text="Floor No").grid(row=0, column=0, sticky="w", pady=2)
# # #         self.floor_entry = tk.Entry(manage_frame)
# # #         self.floor_entry.grid(row=0, column=1, pady=2)

# # #         tk.Label(manage_frame, text="Room No").grid(row=1, column=0, sticky="w", pady=2)
# # #         self.room_entry = tk.Entry(manage_frame)
# # #         self.room_entry.grid(row=1, column=1, pady=2)

# # #         tk.Label(manage_frame, text="Room Type").grid(row=2, column=0, sticky="w", pady=2)
# # #         self.type_combobox = ttk.Combobox(manage_frame, values=["Luxury", "Duplex", "Single"], state="readonly")
# # #         self.type_combobox.current(0)
# # #         self.type_combobox.grid(row=2, column=1, pady=2)

# # #         # ---- Room Details + Browse Frame ----
# # #         below_frame = tk.Frame(root)
# # #         below_frame.pack(fill="both", expand=True, padx=10)

# # #         # Room Details Table
# # #         table_frame = tk.LabelFrame(below_frame, text="Room Details", padx=10, pady=10)
# # #         table_frame.pack(side="left", fill="both", expand=True)

# # #         self.tree = ttk.Treeview(table_frame, columns=("floor_no", "room_no", "room_type"), show="headings")
# # #         self.tree.heading("floor_no", text="Floor No")
# # #         self.tree.heading("room_no", text="Room No")
# # #         self.tree.heading("room_type", text="Room Type")
# # #         self.tree.pack(fill="both", expand=True)

# # #         # Browse By Frame
# # #         browse_frame = tk.LabelFrame(below_frame, text="Browse By", padx=10, pady=10)
# # #         browse_frame.pack(side="right", fill="y")

# # #         tk.Label(browse_frame, text="Search By").grid(row=0, column=0, sticky="w")
# # #         self.search_by_cb = ttk.Combobox(browse_frame, values=["Room_No", "Booking_id", "Check_in", "Room_type"], state="readonly", width=15)
# # #         self.search_by_cb.current(0)
# # #         self.search_by_cb.grid(row=1, column=0, pady=5)

# # #         self.search_entry = tk.Entry(browse_frame, width=17)
# # #         self.search_entry.grid(row=1, column=1, pady=5, padx=5)

# # #         tk.Button(browse_frame, text="Check", width=10, command=self.check_data).grid(row=2, column=0, pady=10)
# # #         tk.Button(browse_frame, text="See All", width=10, command=self.refresh_table).grid(row=2, column=1)

# # #         self.refresh_table()

# # #     def refresh_table(self):
# # #         for row in self.tree.get_children():
# # #             self.tree.delete(row)
# # #         self.cursor.execute("SELECT floor_no, room_no, room_type FROM rooms")
# # #         for row in self.cursor.fetchall():
# # #             self.tree.insert("", tk.END, values=row)

# # #     def check_data(self):
# # #         criteria = self.search_by_cb.get()
# # #         keyword = self.search_entry.get()

# # #         # Map ComboBox values to actual column names
# # #         column_map = {
# # #             "Room_No": "room_no",
# # #             "Booking_id": "booking_id",
# # #             "Check_in": "check_in",
# # #             "Room_type": "room_type"
# # #         }

# # #         sql = f"SELECT floor_no, room_no, room_type FROM rooms WHERE {column_map[criteria]} LIKE %s"
# # #         self.cursor.execute(sql, (f"%{keyword}%",))
# # #         results = self.cursor.fetchall()

# # #         self.tree.delete(*self.tree.get_children())
# # #         for row in results:
# # #             self.tree.insert("", tk.END, values=row)

# # # # Launch the App
# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = HotelRoomManager(root)
# # #     root.mainloop()







# # import tkinter as tk
# # from tkinter import ttk, messagebox
# # import mysql.connector

# # class HotelRoomManager:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Hotel Room Manager")
# #         self.root.geometry("1550x800+0+183")
# #         self.selected_item = None

# #         # --- MySQL connection ---
# #         self.db = mysql.connector.connect(
# #             host="localhost",
# #             user="root",
# #             password="Mysql@12345",  # ← apna MySQL password yaha daalo
# #             database="hotelmangement"
# #         )
# #         self.cursor = self.db.cursor()

# #         # --- Manage Room Frame ---
# #         manage_frame = tk.LabelFrame(root, text="Manage Hotel Room", padx=10, pady=10)
# #         manage_frame.pack(fill="x", padx=10, pady=5)

# #         # Row-wise inputs
# #         tk.Label(manage_frame, text="Floor No").grid(row=0, column=0, sticky="w", pady=2)
# #         self.floor_entry = tk.Entry(manage_frame)
# #         self.floor_entry.grid(row=0, column=1, pady=2)

# #         tk.Label(manage_frame, text="Room No").grid(row=1, column=0, sticky="w", pady=2)
# #         self.room_entry = tk.Entry(manage_frame)
# #         self.room_entry.grid(row=1, column=1, pady=2)

# #         tk.Label(manage_frame, text="Room Type").grid(row=2, column=0, sticky="w", pady=2)
# #         self.type_combobox = ttk.Combobox(manage_frame, values=["Luxury", "Duplex", "Single"], state="readonly")
# #         self.type_combobox.current(0)
# #         self.type_combobox.grid(row=2, column=1, pady=2)

# #         # Buttons
# #         btn_frame = tk.Frame(manage_frame)
# #         btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

# #         tk.Button(btn_frame, text="Save", width=12, command=self.save_room).grid(row=0, column=0, padx=5)
# #         tk.Button(btn_frame, text="Update", width=12, command=self.update_room).grid(row=0, column=1, padx=5)
# #         tk.Button(btn_frame, text="Delete", width=12, command=self.delete_room).grid(row=0, column=2, padx=5)
# #         tk.Button(btn_frame, text="Reset", width=12, command=self.reset_form).grid(row=0, column=3, padx=5)

# #         # --- Lower Frame: Room Details + Browse By ---
# #         lower_frame = tk.Frame(root)
# #         lower_frame.pack(fill="both", expand=True, padx=10, pady=5)

# #         # Room Details Table
# #         table_frame = tk.LabelFrame(lower_frame, text="Room Details", padx=10, pady=10)
# #         table_frame.pack(side="left", fill="both", expand=True)

# #         self.tree = ttk.Treeview(table_frame, columns=("floor_no", "room_no", "room_type"), show="headings")
# #         self.tree.heading("floor_no", text="Floor No")
# #         self.tree.heading("room_no", text="Room No")
# #         self.tree.heading("room_type", text="Room Type")
# #         for col in ("floor_no", "room_no", "room_type"):
# #             self.tree.column(col, width=120)
# #         self.tree.pack(fill="both", expand=True)
# #         self.tree.bind("<<TreeviewSelect>>", self.on_select)

# #         # --- Browse By Frame ---
# #         browse_frame = tk.LabelFrame(lower_frame, text="Browse By", padx=10, pady=10)
# #         browse_frame.pack(side="right", fill="y", padx=10)

# #         tk.Label(browse_frame, text="Search By").grid(row=0, column=0, sticky="w")
# #         self.search_by_cb = ttk.Combobox(
# #             browse_frame, values=["Room_No", "Booking_id", "Check_in", "Room_type"], state="readonly", width=18)
# #         self.search_by_cb.current(0)
# #         self.search_by_cb.grid(row=1, column=0, pady=5)

# #         self.search_entry = tk.Entry(browse_frame, width=20)
# #         self.search_entry.grid(row=1, column=1, padx=5)

# #         tk.Button(browse_frame, text="Check", width=10, command=self.check_data).grid(row=2, column=0, pady=10)
# #         tk.Button(browse_frame, text="See All", width=10, command=self.refresh_table).grid(row=2, column=1)

# #         self.refresh_table()

# #     def save_room(self):
# #         floor = self.floor_entry.get()
# #         room = self.room_entry.get()
# #         rtype = self.type_combobox.get()
# #         if floor and room and rtype:
# #             query = "INSERT INTO rooms (floor_no, room_no, room_type) VALUES (%s, %s, %s)"
# #             self.cursor.execute(query, (floor, room, rtype))
# #             self.db.commit()
# #             self.refresh_table()
# #             self.reset_form()
# #         else:
# #             messagebox.showwarning("Warning", "Please fill all fields")

# #     def update_room(self):
# #         if self.selected_item:
# #             old = self.tree.item(self.selected_item)["values"]
# #             query = "UPDATE rooms SET floor_no=%s, room_no=%s, room_type=%s WHERE floor_no=%s AND room_no=%s AND room_type=%s"
# #             self.cursor.execute(query, (
# #                 self.floor_entry.get(),
# #                 self.room_entry.get(),
# #                 self.type_combobox.get(),
# #                 old[0], old[1], old[2]
# #             ))
# #             self.db.commit()
# #             self.refresh_table()
# #             self.reset_form()

# #     def delete_room(self):
# #         if self.selected_item:
# #             old = self.tree.item(self.selected_item)["values"]
# #             query = "DELETE FROM rooms WHERE floor_no=%s AND room_no=%s AND room_type=%s"
# #             self.cursor.execute(query, (old[0], old[1], old[2]))
# #             self.db.commit()
# #             self.refresh_table()
# #             self.reset_form()

# #     def reset_form(self):
# #         self.floor_entry.delete(0, tk.END)
# #         self.room_entry.delete(0, tk.END)
# #         self.type_combobox.current(0)
# #         self.selected_item = None

# #     def on_select(self, event):
# #         selected = self.tree.focus()
# #         if selected:
# #             self.selected_item = selected
# #             vals = self.tree.item(selected)["values"]
# #             self.floor_entry.delete(0, tk.END)
# #             self.floor_entry.insert(0, vals[0])
# #             self.room_entry.delete(0, tk.END)
# #             self.room_entry.insert(0, vals[1])
# #             self.type_combobox.set(vals[2])

# #     def refresh_table(self):
# #         self.tree.delete(*self.tree.get_children())
# #         self.cursor.execute("SELECT floor_no, room_no, room_type FROM rooms")
# #         for row in self.cursor.fetchall():
# #             self.tree.insert("", tk.END, values=row)

# #     def check_data(self):
# #         field_map = {
# #             "Room_No": "room_no",
# #             "Booking_id": "booking_id",
# #             "Check_in": "check_in",
# #             "Room_type": "room_type"
# #         }
# #         field = field_map[self.search_by_cb.get()]
# #         keyword = self.search_entry.get()
# #         query = f"SELECT floor_no, room_no, room_type FROM rooms WHERE {field} LIKE %s"
# #         self.cursor.execute(query, (f"%{keyword}%",))
# #         rows = self.cursor.fetchall()
# #         self.tree.delete(*self.tree.get_children())
# #         for row in rows:
# #             self.tree.insert("", tk.END, values=row)

# # # Main app loop
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = HotelRoomManager(root)
# #     root.mainloop()




# from tkinter import *
# from tkinter import messagebox as mb
# from PIL import Image , ImageTk
# from tkinter import ttk
# import mysql.connector


# class room_page:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1550x800+0+235")
#         self.root.title("Room_Management")


#         #variables
#         self.floor_no=StringVar()
#         self.room_no=StringVar()
#         self.room_type=StringVar()

#         self.inp_rtype=""

#         #frame creation
#         man_room_frame=LabelFrame(self.root,fg="purple",text="Manage Hotel Room",bd=2,relief=RIDGE,font=("times new roman",17,"bold"),padx=2)
#         man_room_frame.place(x=10,y=0,height=260,width=1500)

        
        
#         label_room_flr=Label(man_room_frame,text="Floor",font=("new times roman",17,"italic bold"))
#         label_room_flr.place(x=10,y=10)
#         inp_flr=Entry(man_room_frame,textvariable=self.floor_no,font=("new times roman",15,"italic"),width=15)
#         inp_flr.place(x=160,y=10)

#         label_room_no=Label(man_room_frame,text="Room No",font=("new times roman",17,"italic bold"))
#         label_room_no.place(x=10,y=70)
#         inp_rno=Entry(man_room_frame,textvariable=self.room_no,font=("new times roman",15,"italic"),width=15)
#         inp_rno.place(x=160,y=70)

#         label_room_type=Label(man_room_frame,text="Room Type",font=("new times roman",17,"italic bold"))
#         label_room_type.place(x=10,y=130)
#         self.inp_rtype=ttk.Combobox(man_room_frame,textvariable=self.room_type,font=("new times roman",15,"italic"),width=15,state="readonly")
#         self.inp_rtype["values"]=("Luxary","Single","Duplex")
#         self.inp_rtype.current(0)
#         self.inp_rtype.place(x=160,y=130)



#         #button for add,update,reset,delete

#         but_save=Button(man_room_frame,command=self.insert_record,text="Save",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
#         but_save.place(x=10,y=180)

#         but_update=Button(man_room_frame,command=self.update_room_detail,text="Update",bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
#         but_update.place(x=205,y=180)

#         but_delete=Button(man_room_frame,command=self.delete_room_detail,text="Delete",bd=1,font=("new times roman",14,"bold"),bg="white",fg="purple",cursor="hand2")
#         but_delete.place(x=420,y=180)

#         but_reset=Button(man_room_frame,text="Reset",command=self.reset_but,bd=1,font=("new times roman",14,"bold"),fg="purple",bg="white",cursor="hand2")
#         but_reset.place(x=610,y=180)


#         #table frame
#         table_frame=LabelFrame(self.root,bd=2,text="Room Details",font=("new times roman",16,"bold"),relief=RIDGE,fg="purple")
#         table_frame.place(x=10,y=270,height=275,width=1000)

#         #table detail show
        
#         details_table=Frame(table_frame,bd=2,relief=RIDGE)
#         details_table.place(x=10,y=0,height=240,width=975)

#         scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

#         self.Cust_Details_Table=ttk.Treeview(details_table,column=("floor","room_no","room_type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)

#         scroll_x.config(command=self.Cust_Details_Table.xview)
#         scroll_y.config(command=self.Cust_Details_Table.yview)

#         self.Cust_Details_Table.heading("floor",text="Floor No")
#         self.Cust_Details_Table.heading("room_no",text="Room No")
#         self.Cust_Details_Table.heading("room_type",text="Room Type")

#         self.Cust_Details_Table["show"]="headings"
        
#         self.Cust_Details_Table.column("floor",width=100)
#         self.Cust_Details_Table.column("room_no",width=100)
#         self.Cust_Details_Table.column("room_type",width=100)
        
#         self.Cust_Details_Table.pack(fill=BOTH,expand=1)

#         self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_guest_data)

#         self.show_guest_data()


        
#         #browse frame

        
#         #table browse frame
#         browse_frame=LabelFrame(self.root,fg="purple",text="Browse By",bd=2,relief=RIDGE,font=("times new roman",17,"bold"))
#         browse_frame.place(x=1040,y=270,height=275,width=470)

#         self.guest_check=StringVar()
#         self.see_all=StringVar()

#         combo_opt=ttk.Combobox(browse_frame,textvariable=self.guest_check,font=("times new roman",17,"italic"),width=10,state="readonly")
#         combo_opt["values"]=("Room_No","Room_Type")
#         combo_opt.current(0)
#         combo_opt.place(x=20,y=60)

#         gue_search=Entry(browse_frame,textvariable=self.see_all,font=("times new roman",17,"italic"),width=11)
#         gue_search.place(x=250,y=60)


#         #check button inside browse frame
#         check_button=Button(browse_frame,text="Check",command=self.check_display,cursor="hand2",font=("times new roman",15,"bold"),width=8,fg="purple",bg="white")
#         check_button.place(x=90,y=160)

#         see_button=Button(browse_frame,command=self.show_guest_data,cursor="hand2",text="See All",font=("times new roman",15,"bold"),width=8,fg="purple",bg="white")
#         see_button.place(x=230,y=160)

#     def insert_record(self):
#         if self.floor_no.get()=="" or self.room_no.get()=="" or self.room_type=="":
#             mb.showerror("Error","All Fields are Required",parent=self.root)
#         else:
#             try:
#                 mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
#                 mysql_control=mysql_connect.cursor()
#                 mysql_control.execute("insert into rooms values(%s,%s,%s)",(
#                     self.floor_no.get(),
#                     self.room_no.get(),
#                     self.room_type.get()
#                     ))
#                 mysql_connect.commit()
#                 mysql_connect.close()
            
                                                                                                     
#                 mb.showinfo("success","Guest detail inserted Sucessfully",parent=self.root)
#                 self.show_guest_data()
#             except Exception as es:
#                 mb.showwarning("Warning",f"Some thing went wrong:{str(es)}")
  
#     def show_guest_data(self):
#         mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
#         mysql_control=mysql_connect.cursor()
#         mysql_control.execute("select * from rooms")
#         rows=mysql_control.fetchall()
#         if len(rows)!=0:
#             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
#             for i in rows:
#                 self.Cust_Details_Table.insert("",END,values=i)
#             mysql_connect.commit()
#             mysql_connect.close()

#     def get_guest_data(self,event=""):
#         cursor_row=self.Cust_Details_Table.focus()
#         content=self.Cust_Details_Table.item(cursor_row)
#         row=content["values"]
#         self.floor_no.set(row[0])
#         self.room_no.set(row[1])
#         self.room_type.set(row[2])

#     def update_room_detail(self):
#         if self.floor_no.get()=="" or self.room_no.get()=="" or self.room_type.get()=="":
#             mb.showerror("Error","All field required",parent=self.root)
#         else:
                
#             mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
#             mysql_control=mysql_connect.cursor()
#             mysql_control.execute("update rooms set Floor=%s,Room_Type=%s where Room_No=%s",(
#                     self.floor_no.get(),
#                     self.room_type.get(),
#                     self.room_no.get(),
#                     ))
#             mysql_connect.commit()
#             mysql_connect.close()
#             mb.showinfo("Update","Room Detail Updated Sucessfully",parent=self.root)
#             self.show_guest_data()
#     def reset_but(self):
#         self.floor_no.set("")
#         self.room_no.set("")
#         self.inp_rtype.current(0)

            
#     def delete_room_detail(self):
#         ques=mb.askyesno("Delete Warning","Do you want to delete this customer",parent=self.root)
#         if ques>0:
#             mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
#             mysql_control=mysql_connect.cursor()
#             query="delete from rooms where Room_No=%s"
#             mysql_control.execute(query,(self.room_no.get(),))
#         else:
#             if not delete_room_detail:
#                 return
#         mysql_connect.commit()
#         mysql_connect.close()
#         self.show_guest_data()
            
#     def check_display(self):
#         mysql_connect=mysql.connector.connect(host="localhost",user="root",password="Mysql@12345",database="hotelmangement")
#         mysql_control=mysql_connect.cursor()
#         query="select * from rooms where {}  LIKE %s".format(str(self.guest_check.get()))
#         mysql_control.execute(query,('%'+str(self.see_all.get())+'%',))
            

#         rows=mysql_control.fetchall()
#         if len(rows)!=0:
#             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
#             for i in rows:
#                 self.Cust_Details_Table.insert("",END,values=i)
#             mysql_connect.commit()
#             mysql_connect.close()
            




# if __name__=="__main__":
#     win=Tk()
#     app=room_page(win)
#     win.mainloop()
