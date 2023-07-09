import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from datetime import datetime

root = tk.Tk()
root.geometry("1350x700+0+0")

def tab1():
    def tab2():
        global label2
        global data_frame2
        global detail_frame2
        global main_frame2
        global search_frame2
        global button2

        label1.destroy()
        button1.destroy()
        detail_frame.destroy()
        main_frame.destroy()
        search_frame.destroy()
        data_frame.destroy()


        label2 = Label(root, text="Boarding House Management System", font=("Arial", 30, "bold"), border=12,
                       relief=tk.GROOVE)
        label2.pack(side=tk.TOP, fill=tk.X)

        detail_frame2 = tk.LabelFrame(root, text="Room Details", font=("Arial", 20), bd=12, relief=tk.GROOVE)
        detail_frame2.place(x=30, y=90, width=390, height=575)

        data_frame2 = tk.Frame(root, bd=12, relief=tk.GROOVE)
        data_frame2.place(x=420, y=90, width=890, height=575)

        # ===== Variables =====#
        room_id = tk.StringVar()
        capacity = tk.StringVar()
        rent = tk.StringVar()


        cCode_lb = tk.Label(detail_frame2, text="Room ID", font=("Arial", 15))
        cCode_lb.grid(row=0, column=0, padx=2, pady=2)
        cCode_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=room_id)
        cCode_inp.grid(row=0, column=1, padx=2, pady=2)

        cName_lb = tk.Label(detail_frame2, text="Capacity", font=("Arial", 15))
        cName_lb.grid(row=1, column=0, padx=2, pady=2)
        cName_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=capacity)
        cName_inp.grid(row=1, column=1, padx=2, pady=2)
        
        rent_lb = tk.Label(detail_frame2, text="Rent", font=("Arial", 15))
        rent_lb.grid(row=2, column=0, padx=2, pady=2)
        rent_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=rent)
        rent_inp.grid(row=2, column=1, padx=2, pady=2)


        def fetch_student_database():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("SELECT * FROM `rooms`")
            rows = curr.fetchall()
            if len(rows) != 0:
                course_table.delete(*course_table.get_children())
                for row in rows:
                    course_table.insert('', tk.END, values=row)
                conn.commit()
            conn.close()

        def add_room():
            try:
                if room_id.get() == "" or capacity.get() == "" or rent.get() == "":
                    messagebox.showerror("Error!", "Please fill all the fields!")
                else:
                    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                    curr = conn.cursor()
                    curr.execute("INSERT INTO rooms VALUES (%s,%s,%s)",
                                (room_id.get(), capacity.get(), rent.get()))
                    conn.commit()
                    conn.close()

                    fetch_student_database()
            except:
                messagebox.showerror("Error!", "Room already exists!")

        def get_cursors(event):

            cursor_row2 = course_table.focus()
            content = course_table.item(cursor_row2)
            row = content['values']
            room_id.set(row[0])
            capacity.set(row[1])
            rent.set(row[2])

        def clear_room():
            room_id.set("")
            capacity.set("")
            rent.set("")

        def delete_room():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("delete from rooms where `room_id`=%s", room_id.get())
            curr.execute("delete from tenants where `room_id`=%s", room_id.get())
            
            conn.commit()
            conn.close()
            clear_room()         
            update_room()   
            refresh_frame()
            fetch_student_database()


        def update_room():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                item = course_table.focus()    
                values = course_table.item(item)['values']
                cc = values[0]                
                curr.execute("update rooms set `room_id`=%s, `capacity`=%s, `rent`=%s where `room_id`=%s",
                            (room_id.get(), capacity.get(), rent.get(), cc))
                conn.commit()
                conn.close()
                fetch_student_database()
                clear_room()
            except:
                messagebox.showerror("Error!", "Room already exists!")

        def search_room():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                curr.execute("select * from rooms where `room_id`=%s", room_id.get())
                row = curr.fetchone()

                room_id.set(row[0])
                capacity.set(row[1])
                rent.set(row[2])

                conn.commit()

            except:
                tkinter.messagebox.showinfo("data entry form", "No Course Found")
                clear_room()
                conn.close()

        btn_frame2 = tk.Frame(detail_frame2, bd=10, relief=tk.GROOVE)
        btn_frame2.place(x=10, y=400, width=345, height=120)

        add_btn2 = tk.Button(btn_frame2, text="Add", bd=7, font=("Arial", 13), width=15, command=add_room)
        add_btn2.grid(row=0, column=0, padx=2, pady=2)

        update_btn2 = tk.Button(btn_frame2, text="Update", bd=7, font=("Arial", 13), width=15, command=update_room)
        update_btn2.grid(row=0, column=1, padx=2, pady=2)

        delete_btn2 = tk.Button(btn_frame2, text="Delete", bd=7, font=("Arial", 13), width=15, command=delete_room)
        delete_btn2.grid(row=1, column=0, padx=2, pady=2)

        clear_btn2 = tk.Button(btn_frame2, text="Clear", bd=7, font=("Arial", 13), width=15, command=clear_room)
        clear_btn2.grid(row=1, column=1, padx=2, pady=2)

        search_frame2 = tk.Frame(data_frame2, relief=tk.GROOVE)
        search_frame2.pack(anchor=tk.SE)

        search_btn2 = tk.Button(search_frame2, text="Search", font=("Arial", 13), bd=9, width=14,
                                command=search_room)
        search_btn2.grid(row=0, column=2, padx=12, pady=2)

        main_frame2 = tk.Frame(data_frame2, bd=11, relief=tk.GROOVE)
        main_frame2.pack(fill=tk.BOTH, expand=True)

        y_scroll2 = tk.Scrollbar(main_frame2, orient=tk.VERTICAL)
        x_scroll2 = tk.Scrollbar(main_frame2, orient=tk.HORIZONTAL)

        course_table = ttk.Treeview(main_frame2, columns=("Room ID", "Capacity", "Rent"),
                                    yscrollcommand=y_scroll2.set, xscrollcommand=x_scroll2.set)

        y_scroll2.config(command=course_table.yview)
        x_scroll2.config(command=course_table.xview)

        y_scroll2.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll2.pack(side=tk.BOTTOM, fill=tk.X)

        course_table.heading("Room ID", text="Room ID")
        course_table.heading("Capacity", text="Capacity")
        course_table.heading("Rent", text="Rent")

        course_table['show'] = 'headings'

        course_table.column("Room ID", width=100)
        course_table.column("Capacity", width=100)
        course_table.column("Rent", width=100)

        course_table.pack(fill=tk.BOTH, expand=True)

        fetch_student_database()

        course_table.bind("<ButtonRelease-1>", get_cursors)

        def back():
            label2.destroy()
            button2.destroy()
            detail_frame2.destroy()
            main_frame2.destroy()
            search_frame2.destroy()
            data_frame2.destroy()
            tab1()
        
        def refresh_frame():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            cursor = conn.cursor()

            # Clear existing data
            course_table.delete(*course_table.get_children())

            # Fetch data from the database
            cursor.execute('SELECT * FROM rooms')        
            rows = cursor.fetchall()

            # Insert fetched data into the treeview
            for row in rows:
                course_table.insert('', tk.END, values=row)  


        button2 = Button(root, text='TENANT', font=('Times_New_Roman', 15), command=back)
        # button2.pack(side=BOTTOM)
        button2.place(x=450, y=110)

        button2_1 = Button(root, text='PAYMENT', font=('Times_New_Roman', 15), command=tab3)
        # button2.pack(side=BOTTOM)
        button2_1.place(x=550, y=110)

        button2_2 = Button(root, text='ENERGY', font=('Times_New_Roman', 15), command=tab3)
        # button2.pack(side=BOTTOM)
        button2_2.place(x=670, y=110)        

    def tab3():
        global label3
        global data_frame3
        global detail_frame3
        global main_frame3
        global search_frame3
        global button3        

        label1.destroy()
        button1.destroy()
        detail_frame.destroy()
        main_frame.destroy()
        search_frame.destroy()
        data_frame.destroy()

        # label2.destroy()
        # button2.destroy()
        # detail_frame2.destroy()
        # main_frame2.destroy()
        # search_frame2.destroy()
        # data_frame2.destroy()

        label3 = Label(root, text="Boarding House Management System", font=("Arial", 30, "bold"), border=12,
                    relief=tk.GROOVE)
        label3.pack(side=tk.TOP, fill=tk.X)

        detail_frame3 = tk.LabelFrame(root, text="Payment Information", font=("Arial", 20), bd=12, relief=tk.GROOVE)
        detail_frame3.place(x=30, y=90, width=390, height=575)

        data_frame3 = tk.Frame(root, bd=12, relief=tk.GROOVE)
        data_frame3.place(x=420, y=90, width=890, height=575)

        # ===== Variables =====#
        payment_id = tk.StringVar()
        amount_paid = tk.StringVar()
        paid_date = tk.StringVar()
        room_id3 = tk.StringVar()
        tenant_id3 = tk.StringVar()


        today = datetime.now()
        current_date = datetime.now()
        formatted_date = current_date.strftime("%B %d, %Y")


        # cCode_lb = tk.Label(detail_frame3, text="Payment ID", font=("Arial", 15))
        # cCode_lb.grid(row=0, column=0, padx=2, pady=2)
        # cCode_inp = tk.Entry(detail_frame3, bd=7, font=("Arial", 15), textvariable=payment_id)
        # cCode_inp.grid(row=0, column=1, padx=2, pady=2)

        cName_lb = tk.Label(detail_frame3, text="Room ID", font=("Arial", 15))
        cName_lb.grid(row=1, column=0, padx=2, pady=2)
        # cName_inp = tk.Entry(detail_frame3, bd=7, font=("Arial", 15), textvariable=room_id3)
        # cName_inp.grid(row=1, column=1, padx=2, pady=2)
        cName_inp = ttk.Combobox(detail_frame3, font=("Arial", 15),textvariable=room_id3)
        cName_inp["values"] = room_ids
        cName_inp.place(x=125, y=1, width=230, height=32)

        
        rent_lb = tk.Label(detail_frame3, text="Tenant ID", font=("Arial", 15))
        rent_lb.grid(row=2, column=0, padx=2, pady=2)
        # rent_inp = tk.Entry(detail_frame3, bd=7, font=("Arial", 15), textvariable=tenant_id3)
        # rent_inp.grid(row=2, column=1, padx=2, pady=2)
        rent_inp = ttk.Combobox(detail_frame3, font=("Arial", 15),textvariable=tenant_id3)
        rent_inp["values"] = tenant_ids
        rent_inp.place(x=125, y=35, width=230, height=32)


        energy_consumption_lb = tk.Label(detail_frame3, text="Amount Paid", font=("Arial", 15))
        energy_consumption_lb.grid(row=3, column=0, padx=2, pady=2)
        energy_consumption_inp = tk.Entry(detail_frame3, bd=7, font=("Arial", 15), textvariable=amount_paid)
        energy_consumption_inp.grid(row=3, column=1, padx=2, pady=2)
        
        eBill_lb = tk.Label(detail_frame3, text="Paid Date", font=("Arial", 14))
        eBill_lb.grid(row=4, column=0, padx=2, pady=2)
        eBill_inp = tk.Entry(detail_frame3, bd=7, font=("Arial", 15), textvariable=paid_date)
        eBill_inp.grid(row=4, column=1, padx=2, pady=2)

        paid_date.set(formatted_date)

        def fetch_payment_database():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("SELECT * FROM `payments`")
            rows = curr.fetchall()
            if len(rows) != 0:
                payment_table.delete(*payment_table.get_children())
                for row in rows:
                    payment_table.insert('', tk.END, values=row)
                conn.commit()
            conn.close()

        def add_payment():
            try:
                if room_id3.get() == "" or tenant_id3.get() == "" or amount_paid.get() == "" or paid_date.get() == "":
                    messagebox.showerror("Error!", "Please fill all the fields!")
                else:
                    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                    curr = conn.cursor()
                    curr.execute("INSERT INTO payments(tenant_id, room_id, payment_date, payment_amount) VALUES (%s,%s,%s,%s)",
                                (tenant_id3.get(),room_id3.get(), paid_date.get(),amount_paid.get()))
                    conn.commit()
                    conn.close()

                    fetch_payment_database()
            except:
                messagebox.showerror("Error!", "Payment already exists!")

        def get_cursors3(event):

            cursor_row3 = payment_table.focus()
            content = payment_table.item(cursor_row3)
            row = content['values']
            payment_id.set(row[0])
            room_id3.set(row[1])
            tenant_id3.set(row[2])
            amount_paid.set(row[4])
            paid_date.set(row[3])

        def clear_payment():
            payment_id.set("")
            room_id3.set("")
            tenant_id3.set("")
            amount_paid.set("")
            paid_date.set("")

        def delete_payment():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            item = payment_table.focus()    
            values = payment_table.item(item)['values']
            cc = values[0]             
            curr.execute("delete from payments where `payment_id`=%s", cc)
            
            conn.commit()
            conn.close()
            clear_payment()         
            update_payment()   
            fetch_payment_database()


        def update_payment():
            # try:
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            item = payment_table.focus()    
            values = payment_table.item(item)['values']
            cc = values[0]                 
            curr.execute("update payments set `room_id`=%s, `tenant_id`=%s, `payment_date`=%s, `payment_amount`=%s where `payment_id`=%s",
                        (room_id3.get(), tenant_id3.get(), paid_date.get(),amount_paid.get(), cc))
            conn.commit()
            conn.close()
            fetch_payment_database()
            clear_payment()
        # except:
            #     messagebox.showerror("Error!", "Room already exists!")

        def search_payment():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                item = payment_table.focus()    
                values = payment_table.item(item)['values']
                cc = values[0] 
                curr.execute("select * from payments where `payment_id`=%s", cc)
                row = curr.fetchone()

                # payment_id.set(row[0])
                room_id3.set(row[1])
                tenant_id3.set(row[2])
                amount_paid.set(row[3])
                paid_date.set(row[4])

                conn.commit()

            except:
                tkinter.messagebox.showinfo("data entry form", "No Course Found")
                clear_payment()
                conn.close()
        
        
        btn_frame3 = tk.Frame(detail_frame3, bd=10, relief=tk.GROOVE)
        btn_frame3.place(x=10, y=400, width=345, height=120)

        add_btn3 = tk.Button(btn_frame3, text="Add", bd=7, font=("Arial", 13), width=15, command= add_payment)
        add_btn3.grid(row=0, column=0, padx=2, pady=2)

        update_btn3 = tk.Button(btn_frame3, text="Update", bd=7, font=("Arial", 13), width=15, command = update_payment)
        update_btn3.grid(row=0, column=1, padx=2, pady=2)

        delete_btn3 = tk.Button(btn_frame3, text="Delete", bd=7, font=("Arial", 13), width=15, command = delete_payment)
        delete_btn3.grid(row=1, column=0, padx=2, pady=2)

        clear_btn3 = tk.Button(btn_frame3, text="Clear", bd=7, font=("Arial", 13), width=15, command= clear_payment)
        clear_btn3.grid(row=1, column=1, padx=2, pady=2)

        search_frame3 = tk.Frame(data_frame3, relief=tk.GROOVE)
        search_frame3.pack(anchor=tk.SE)

        search_btn3 = tk.Button(search_frame3, text="Search", font=("Arial", 13), bd=9, width=14)
        search_btn3.grid(row=0, column=2, padx=12, pady=2)

        main_frame3 = tk.Frame(data_frame3, bd=11, relief=tk.GROOVE)
        main_frame3.pack(fill=tk.BOTH, expand=True)

        y_scroll3 = tk.Scrollbar(main_frame3, orient=tk.VERTICAL)
        x_scroll3 = tk.Scrollbar(main_frame3, orient=tk.HORIZONTAL)

        payment_table = ttk.Treeview(main_frame3, columns=("Payment ID", "Room ID", "Tenant ID", "Paid Date", "Amount Paid"),
                                    yscrollcommand=y_scroll3.set, xscrollcommand=x_scroll3.set)

        y_scroll3.config(command=payment_table.yview)
        x_scroll3.config(command=payment_table.xview)

        y_scroll3.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll3.pack(side=tk.BOTTOM, fill=tk.X)

        payment_table.heading("Payment ID", text="Payment ID")
        payment_table.heading("Room ID", text="Room ID")
        payment_table.heading("Tenant ID", text="Tenant ID")
        payment_table.heading("Paid Date", text="Paid Date")        
        payment_table.heading("Amount Paid", text="Amount Paid")


        payment_table['show'] = 'headings'

        payment_table.column("Payment ID", width=100)
        payment_table.column("Room ID", width=100)
        payment_table.column("Tenant ID", width=100)
        payment_table.column("Paid Date", width=100)        
        payment_table.column("Amount Paid", width=100)


        payment_table.pack(fill=tk.BOTH, expand=True)

        fetch_payment_database()

        payment_table.bind("<ButtonRelease-1>", get_cursors3)

        def back3():
            label3.destroy()
            button3.destroy()
            detail_frame3.destroy()
            main_frame3.destroy()
            search_frame3.destroy()
            data_frame3.destroy()
     
            tab1()


        button3 = Button(root, text='TENANT', font=('Times_New_Roman', 15), command=back3)
        # button2.pack(side=BOTTOM)
        button3.place(x=450, y=110)

        button3_1 = Button(root, text='ROOM', font=('Times_New_Roman', 15), command=tab2)
        # button2.pack(side=BOTTOM)
        button3_1.place(x=550, y=110)

        button3_2 = Button(root, text='ENERGY', font=('Times_New_Roman', 15), command=tab4)
        # button2.pack(side=BOTTOM)
        button3_2.place(x=640, y=110)        

    def tab4():
        global label4
        global data_frame4
        global detail_frame4
        global main_frame4
        global search_frame4
        global button4        

        label1.destroy()
        button1.destroy()
        detail_frame.destroy()
        main_frame.destroy()
        search_frame.destroy()
        data_frame.destroy()

        # label2.destroy()
        # button2.destroy()
        # detail_frame2.destroy()
        # main_frame2.destroy()
        # search_frame2.destroy()
        # data_frame2.destroy()

        label4 = Label(root, text="Boarding House Management System", font=("Arial", 30, "bold"), border=12,
                    relief=tk.GROOVE)
        label4.pack(side=tk.TOP, fill=tk.X)

        detail_frame4 = tk.LabelFrame(root, text="Energy Consumption", font=("Arial", 20), bd=12, relief=tk.GROOVE)
        detail_frame4.place(x=30, y=90, width=390, height=575)

        data_frame4 = tk.Frame(root, bd=12, relief=tk.GROOVE)
        data_frame4.place(x=420, y=90, width=890, height=575)

        # ===== Variables =====#
        consumption_id = tk.StringVar()
        energy_consumption = tk.StringVar()
        consumption_date = tk.StringVar()
        room_id4 = tk.StringVar()
        tenant_id4 = tk.StringVar()


        # cCode_lb = tk.Label(detail_frame4, text="Consumption \n ID", font=("Arial", 15))
        # cCode_lb.grid(row=0, column=0, padx=2, pady=2)
        # cCode_inp = tk.Entry(detail_frame4, bd=7, font=("Arial", 15), textvariable=consumption_id)
        # cCode_inp.grid(row=0, column=1, padx=2, pady=2)

        cName_lb = tk.Label(detail_frame4, text="Room ID", font=("Arial", 15))
        cName_lb.grid(row=1, column=0, padx=2, pady=2)
        cName_inp = ttk.Combobox(detail_frame4, font=("Arial", 15),textvariable=room_id4)
        cName_inp["values"] = room_ids
        cName_inp.place(x=133, y=1, width=230, height=32)
        
        rent_lb = tk.Label(detail_frame4, text="Tenant ID", font=("Arial", 15))
        rent_lb.grid(row=2, column=0, padx=2, pady=2)
        rent_inp = ttk.Combobox(detail_frame4, font=("Arial", 15),textvariable=tenant_id4)
        rent_inp["values"] = tenant_ids
        rent_inp.place(x=133, y=37, width=230, height=32)

        energy_consumption_lb = tk.Label(detail_frame4, text="Energy \n Consumption", font=("Arial", 15))
        energy_consumption_lb.grid(row=3, column=0, padx=2, pady=2)
        energy_consumption_inp = tk.Entry(detail_frame4, bd=7, font=("Arial", 15), textvariable=energy_consumption)
        energy_consumption_inp.grid(row=3, column=1, padx=1.5, pady=1.5)
        
        eBill_lb = tk.Label(detail_frame4, text="Consumption \n Date", font=("Arial", 14))
        eBill_lb.grid(row=4, column=0, padx=2, pady=2)
        eBill_inp = tk.Entry(detail_frame4, bd=7, font=("Arial", 15), textvariable=consumption_date)
        eBill_inp.grid(row=4, column=1, padx=2, pady=2)

        def fetch_energy_database():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("SELECT * FROM `energy_consumption`")
            rows = curr.fetchall()
            if len(rows) != 0:
                energy_table.delete(*energy_table.get_children())
                for row in rows:
                    energy_table.insert('', tk.END, values=row)
                conn.commit()
            conn.close()

        def add_energy():
            try:
                if room_id4.get() == "" or tenant_id4.get() == "" or energy_consumption.get() == "" or consumption_date.get() == "":
                    messagebox.showerror("Error!", "Please fill all the fields!")
                else:
                    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                    curr = conn.cursor()
                    curr.execute("INSERT INTO energy_consumption(room_id,tenant_id, consumption_date, energy_consumption) VALUES (%s,%s,%s,%s)",
                                (room_id4.get(),tenant_id4.get(), consumption_date.get(),energy_consumption.get()))
                    conn.commit()
                    conn.close()

                    fetch_energy_database()
            except:
                messagebox.showerror("Error!", "Payment already exists!")

        def get_cursors4(event):

            cursor_row4 = energy_table.focus()
            content = energy_table.item(cursor_row4)
            row = content['values']
            consumption_id.set(row[0])
            room_id4.set(row[1])
            tenant_id4.set(row[2])
            energy_consumption.set(row[4])
            consumption_date.set(row[3])

        def clear_energy():
            room_id4.set('')
            tenant_id4.set('')
            energy_consumption.set('')
            consumption_date.set('')

        def delete_energy():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            item = energy_table.focus()    
            values = energy_table.item(item)['values']
            cc = values[0]             
            curr.execute("delete from energy_consumption where `consumption_id`=%s", cc)
            
            conn.commit()            
            clear_energy()         
            # update_energy()   
            fetch_energy_database()
            conn.close()

        def update_energy():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                item = energy_table.focus()    
                values = energy_table.item(item)['values']
                cc = values[0]                
                curr.execute("update energy_consumption set `room_id`=%s, `tenant_id`=%s, `consumption_date`=%s, `energy_consumption`=%s where `consumption_id`=%s",
                            (room_id4.get(), tenant_id4.get(), consumption_date.get(), energy_consumption.get(), cc))
                conn.commit()
                conn.close()
                fetch_energy_database()
                clear_energy()
            except:
                messagebox.showerror("Error!", "Room already exists!")

        def search_energy():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                item = energy_table.focus()    
                values = energy_table.item(item)['values']
                cc = values[0] 
                curr.execute("select * from payments where `payment_id`=%s", cc)
                row = curr.fetchone()

                consumption_id.set(row[0])
                room_id4.set(row[1])
                tenant_id4.set(row[2])
                energy_consumption.set(row[4])
                consumption_date.set(row[3])

                conn.commit()

            except:
                tkinter.messagebox.showinfo("data entry form", "No Course Found")
                clear_energy()
                conn.close()        

        
        btn_frame4 = tk.Frame(detail_frame4, bd=10, relief=tk.GROOVE)
        btn_frame4.place(x=10, y=400, width=345, height=120)

        add_btn4 = tk.Button(btn_frame4, text="Add", bd=7, font=("Arial", 13), width=15, command=add_energy)
        add_btn4.grid(row=0, column=0, padx=2, pady=2)

        update_btn4 = tk.Button(btn_frame4, text="Update", bd=7, font=("Arial", 13), width=15, command=update_energy)
        update_btn4.grid(row=0, column=1, padx=2, pady=2)

        delete_btn4 = tk.Button(btn_frame4, text="Delete", bd=7, font=("Arial", 13), width=15, command=delete_energy)
        delete_btn4.grid(row=1, column=0, padx=2, pady=2)

        clear_btn4 = tk.Button(btn_frame4, text="Clear", bd=7, font=("Arial", 13), width=15, command=clear_energy)
        clear_btn4.grid(row=1, column=1, padx=2, pady=2)

        search_frame4 = tk.Frame(data_frame4, relief=tk.GROOVE)
        search_frame4.pack(anchor=tk.SE)

        search_btn4 = tk.Button(search_frame4, text="Search", font=("Arial", 13), bd=9, width=14)
        search_btn4.grid(row=0, column=2, padx=12, pady=2)

        main_frame4 = tk.Frame(data_frame4, bd=11, relief=tk.GROOVE)
        main_frame4.pack(fill=tk.BOTH, expand=True)

        y_scroll4 = tk.Scrollbar(main_frame4, orient=tk.VERTICAL)
        x_scroll4 = tk.Scrollbar(main_frame4, orient=tk.HORIZONTAL)

        energy_table = ttk.Treeview(main_frame4, columns=("Consumption ID", "Room ID", "Tenant ID", "Consumption Date", "Energy Consumption"),
                                    yscrollcommand=y_scroll4.set, xscrollcommand=x_scroll4.set)

        y_scroll4.config(command=energy_table.yview)
        x_scroll4.config(command=energy_table.xview)

        y_scroll4.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll4.pack(side=tk.BOTTOM, fill=tk.X)

        energy_table.heading("Consumption ID", text="Consumption ID")
        energy_table.heading("Room ID", text="Room ID")
        energy_table.heading("Tenant ID", text="Tenant ID")
        energy_table.heading("Energy Consumption", text="Energy Consumption")
        energy_table.heading("Consumption Date", text="Consumption Date")

        energy_table['show'] = 'headings'

        energy_table.column("Consumption ID", width=100)
        energy_table.column("Room ID", width=100)
        energy_table.column("Tenant ID", width=100)
        energy_table.column("Energy Consumption", width=100)
        energy_table.column("Consumption Date", width=100)

        energy_table.pack(fill=tk.BOTH, expand=True)

        fetch_energy_database()

        energy_table.bind("<ButtonRelease-1>", get_cursors4)

        def back4():
            label4.destroy()
            button4.destroy()
            detail_frame4.destroy()
            main_frame4.destroy()
            search_frame4.destroy()
            data_frame4.destroy()
     
            tab1()


        button4 = Button(root, text='TENANT', font=('Times_New_Roman', 15), command=back4)
        # button2.pack(side=BOTTOM)
        button4.place(x=450, y=110)

        button4_1 = Button(root, text='ROOM', font=('Times_New_Roman', 15), command=tab2)
        # button2.pack(side=BOTTOM)
        button4_1.place(x=550, y=110)    

        button4_2 = Button(root, text='PAYMENT', font=('Times_New_Roman', 15), command=tab3)
        # button2.pack(side=BOTTOM)
        button4_2.place(x=640, y=110)              


    label1 = tk.Label(root, text="Boarding House Management System", font=("Arial", 30, "bold"), border=12,
                      relief=tk.GROOVE)
    label1.pack(side=tk.TOP, fill=tk.X)

    detail_frame = tk.LabelFrame(root, text="Tenant Details", font=("Arial", 20), bd=12, relief=tk.GROOVE)
    detail_frame.place(x=30, y=90, width=390, height=575)

    data_frame = tk.Frame(root, bd=12, relief=tk.GROOVE)
    data_frame.place(x=420, y=90, width=890, height=575)

    # ===== Variables =====#

    #tenant_id = tk.StringVar()
    room_id = tk.StringVar()
    name = tk.StringVar()
    contact = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()


    # ===== Entry =====#
    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
    curr = conn.cursor()
    curr.execute("SELECT tenant_id FROM tenants")
    tenant_ids = [row[0] for row in curr.fetchall()]
    conn.close()     

    # idno_lb = tk.Label(detail_frame, text="Tenant ID No.", font=("Arial", 15))
    # idno_lb.grid(row=0, column=0, padx=2, pady=2)

    # idno_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=tenant_id)
    # idno_inp.grid(row=0, column=1, padx=2, pady=2)

    idno2_lb = tk.Label(detail_frame, text="Room ID No.", font=("Arial", 15))
    idno2_lb.grid(row=1, column=0, padx=2, pady=2)

    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
    curr = conn.cursor()
    curr.execute("SELECT room_id FROM rooms")
    room_ids = [row[0] for row in curr.fetchall()]
    conn.close()    
    # idno2_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=room_id)
    idno2_inp = ttk.Combobox(detail_frame, font=("Arial", 15),textvariable=room_id)
    idno2_inp["values"] = room_ids
    # idno2_inp.grid(row=1, column=1, padx=2, pady=2)
    idno2_inp.place(x=127, y=1, width=230, height=33)

    name_lb = tk.Label(detail_frame, text="Name", font=("Arial", 15))
    name_lb.grid(row=2, column=0, padx=2, pady=2)

    name_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=name)
    name_inp.grid(row=2, column=1, padx=2, pady=2)


    year_lb = tk.Label(detail_frame, text="Age", font=("Arial", 15))
    year_lb.grid(row=3, column=0, padx=2, pady=2)

    year_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=age)
    year_inp.grid(row=3, column=1, padx=2, pady=2)

    gender_lb = tk.Label(detail_frame, text="Gender", font=("Arial", 15))
    gender_lb.grid(row=4, column=0, padx=2, pady=2)

    gender_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=gender)
    gender_inp.grid(row=4, column=1, padx=2, pady=2)

    contact_lb = tk.Label(detail_frame, text="Contact", font=("Arial", 15))
    contact_lb.grid(row=5, column=0, padx=2, pady=2)

    contact_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=contact)
    contact_inp.grid(row=5, column=1, padx=2, pady=2)


    # ================#

    # ===== Functions =====#

    def fetch_data():
        conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
        curr = conn.cursor()
        curr.execute("SELECT * FROM tenants")
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            conn.commit()
        conn.close()

    def add_tenant():
        # try:
        if room_id.get() == "" or name.get() == "" or contact.get() == "" or age.get() == "" or gender.get() == "":
            messagebox.showerror("Error!", "Please fill al the fields!")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("INSERT INTO tenants(room_id, tenant_name, gender, age, contact) VALUES (%s,%s,%s,%s,%s)",
                        (room_id.get(), name.get(), gender.get(), age.get(), contact.get()))
            conn.commit()
            conn.close()

            fetch_data()
        # except:
        #     messagebox.showerror("Error!", "Tenant already exists!")

    def get_cursor(event):
        ''' This function will fetch data of the selected row'''

        cursor_row = student_table.focus()
        content = student_table.item(cursor_row)
        row = content['values']
        room_id.set(row[0])
        #tenant_id.set(row[1])
        name.set(row[2])
        gender.set(row[3])        
        age.set(row[4])
        contact.set(row[5])

    def clear_tenants():
        #tenant_id.set("")
        room_id.set("")
        name.set("")
        age.set("")
        gender.set("")
        contact.set("")

    def delete_tenants():
        conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
        curr = conn.cursor()
        item = student_table.focus()    
        values = student_table.item(item)['values']
        cc = values[1]

        curr.execute("delete from tenants where `tenant_id`=%s", cc)
        #curr.execute("update rooms set `capacity` = `capacity` - 1 where `room_id` = %s", rm_id)
        
        conn.commit()
        conn.close()
        fetch_data()
        refresh_stud_frame()
        clear_tenants()

    def update_tenants():
        
        conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
        curr = conn.cursor()
        item = student_table.focus()    
        values = student_table.item(item)['values']
        cc = values[1]

        curr.execute("update tenants set `room_id` = %s, `tenant_name`=%s,`gender`=%s, `age`=%s, `contact`=%s where `tenant_id`=%s",
                    (room_id.get(), name.get(), gender.get(), age.get(), contact.get(), cc))
        conn.commit()
        conn.close()
        fetch_data()
        refresh_stud_frame()
        clear_tenants()

    def search_tenants():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            item = student_table.focus()    
            values = student_table.item(item)['values']
            cc = values[1]            
            curr.execute("select * from tenants where `tenant_id`=%s", cc)
            row = curr.fetchone()

            room_id.set(row[0])
            #tenant_id.set(row[1])
            name.set(row[2])
            age.set(row[3])
            gender.set(row[4])
            contact.set(row[5])

            conn.commit()

        except:
            tkinter.messagebox.showinfo("data entry form", "No student found")
            clear_tenants()
            conn.close()
        
    def refresh_stud_frame():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            cursor1 = conn.cursor()
            student_table.delete(*student_table.get_children())

            # Fetch data from the database
            cursor1.execute('SELECT * FROM tenants')        
            rows = cursor1.fetchall()

            # Insert fetched data into the treeview
            for row in rows:
                student_table.insert('', tk.END, values=row)  

    # ================#

    # ===== Buttons =====#

    btn_frame = tk.Frame(detail_frame, bd=10, relief=tk.GROOVE)
    btn_frame.place(x=10, y=400, width=345, height=120)

    add_btn = tk.Button(btn_frame, text="Add", bd=7, font=("Arial", 13), width=15, command=add_tenant)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, text="Update", bd=7, font=("Arial", 13), width=15, command=update_tenants)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, text="Delete", bd=7, font=("Arial", 13), width=15, command=delete_tenants)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, text="Clear", bd=7, font=("Arial", 13), width=15, command=clear_tenants)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

    # ================#

    # ===== Search =====#

    search_frame = tk.Frame(data_frame, relief=tk.GROOVE)
    search_frame.pack(anchor=tk.SE)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, command=search_tenants)
    search_btn.grid(row=0, column=2, padx=12, pady=2)

    # ================#

    # ===== Database frame =====#

    main_frame = tk.Frame(data_frame, bd=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

    student_table = ttk.Treeview(main_frame, columns=("Room ID","Tenant ID", "Name", "Gender", "Age", "Contact"),
                                 yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    student_table.heading("Room ID", text="Room ID")  
    student_table.heading("Tenant ID", text="Tenant ID")
    student_table.heading("Name", text="Name")
    student_table.heading("Gender", text="Gender")
    student_table.heading("Age", text="Age")
    student_table.heading("Contact", text="Contact")


    student_table['show'] = 'headings'

    student_table.column("Room ID", width=100)
    student_table.column("Tenant ID", width=100)
    student_table.column("Name", width=100)
    student_table.column("Gender", width=100)
    student_table.column("Age", width=100)
    student_table.column("Contact", width=100)

        
    student_table.pack(fill=tk.BOTH, expand=True)

    fetch_data()

    student_table.bind("<ButtonRelease-1>", get_cursor)

    button1 = Button(root, text='ROOMS', font=('Times_New_Roman', 15), command=tab2)
    button1.place(x=450, y=110)

    button1_1 = Button(root, text='PAYMENT', font=('Times_New_Roman', 15), command=tab3)
    button1_1.place(x=550, y=110)

    button1_2 = Button(root, text='ENERGY', font=('Times_New_Roman', 15), command=tab4)
    button1_2.place(x=670, y=110)    


tab1()

root.mainloop()

