import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pymysql

root = tk.Tk()
root.geometry("1350x700+0+0")


def tab1():
    def tab2():
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
        eBill = tk.StringVar()


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
        
        eBill_lb = tk.Label(detail_frame2, text="Electric Bill", font=("Arial", 14))
        eBill_lb.grid(row=3, column=0, padx=2, pady=2)
        eBill_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=eBill)
        eBill_inp.grid(row=3, column=1, padx=2, pady=2)

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
                if room_id.get() == "" or capacity.get() == "" or rent.get() == "" or eBill.get() == "":
                    messagebox.showerror("Error!", "Please fill al the fields!")
                else:
                    conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                    curr = conn.cursor()
                    curr.execute("INSERT INTO rooms VALUES (%s,%s,%s,%s)",
                                (room_id.get(), capacity.get(), rent.get(), eBill.get()))
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
            eBill.set(row[3])

        def clear_room():
            room_id.set("")
            capacity.set("")
            rent.set("")
            eBill.set("")

        def delete_room():
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("delete from rooms where `room_id`=%s", room_id.get())
            conn.commit()
            conn.close()
            fetch_student_database()
            clear_room()

        def update_room():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                curr.execute("update rooms set `capacity`=%s, `rent`=%s, `elec_bill`=%s where `room_id`=%s",
                            (capacity.get(), rent.get(), eBill.get(), room_id.get()))
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
                eBill.set(row[3])

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

        course_table = ttk.Treeview(main_frame2, columns=("Room ID", "Capacity", "Rent", "Electric Bill"),
                                    yscrollcommand=y_scroll2.set, xscrollcommand=x_scroll2.set)

        y_scroll2.config(command=course_table.yview)
        x_scroll2.config(command=course_table.xview)

        y_scroll2.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll2.pack(side=tk.BOTTOM, fill=tk.X)

        course_table.heading("Room ID", text="Room ID")
        course_table.heading("Capacity", text="Capacity")
        course_table.heading("Rent", text="Rent")
        course_table.heading("Electric Bill", text="Electric Bill")

        course_table['show'] = 'headings'

        course_table.column("Room ID", width=100)
        course_table.column("Capacity", width=100)
        course_table.column("Rent", width=100)
        course_table.column("Electric Bill", width=100)

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

        button2 = Button(root, text='TENANT', font=('Times_New_Roman', 15), command=back)
        button2.pack(side=BOTTOM)

    label1 = tk.Label(root, text="Boarding House Management System", font=("Arial", 30, "bold"), border=12,
                      relief=tk.GROOVE)
    label1.pack(side=tk.TOP, fill=tk.X)

    detail_frame = tk.LabelFrame(root, text="Tenant Details", font=("Arial", 20), bd=12, relief=tk.GROOVE)
    detail_frame.place(x=30, y=90, width=390, height=575)

    data_frame = tk.Frame(root, bd=12, relief=tk.GROOVE)
    data_frame.place(x=420, y=90, width=890, height=575)

    # ===== Variables =====#

    tenant_id = tk.StringVar()
    room_id = tk.StringVar()
    name = tk.StringVar()
    contact = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    amt_paid = tk.StringVar()

    # ===== Entry =====#

    idno_lb = tk.Label(detail_frame, text="Tenant ID No.", font=("Arial", 15))
    idno_lb.grid(row=0, column=0, padx=2, pady=2)

    idno_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=tenant_id)
    idno_inp.grid(row=0, column=1, padx=2, pady=2)

    idno2_lb = tk.Label(detail_frame, text="Room ID No.", font=("Arial", 15))
    idno2_lb.grid(row=1, column=0, padx=2, pady=2)

    idno2_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=room_id)
    idno2_inp.grid(row=1, column=1, padx=2, pady=2)

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

    amt_paid_lb = tk.Label(detail_frame, text="Amount Paid", font=("Arial", 15))
    amt_paid_lb.grid(row=6, column=0, padx=2, pady=2)
    amt_paid_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=amt_paid)
    amt_paid_inp.grid(row=6, column=1, padx=2, pady=2)

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
        try:
            if tenant_id.get() == "" or room_id.get() == "" or name.get() == "" or contact.get() == "" or age.get() == "" or gender.get() == "":
                messagebox.showerror("Error!", "Please fill al the fields!")
            else:
                conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
                curr = conn.cursor()
                curr.execute("INSERT INTO tenants VALUES (%s,%s,%s,%s,%s,%s)",
                            (tenant_id.get(), room_id.get(), name.get(), gender.get(), age.get(), contact.get(), amt_paid.get))
                conn.commit()
                conn.close()

                fetch_data()
        except:
            messagebox.showerror("Error!", "Tenant already exists!")

    def get_cursor(event):
        ''' This function will fetch data of the selected row'''

        cursor_row = student_table.focus()
        content = student_table.item(cursor_row)
        row = content['values']
        tenant_id.set(row[0])
        room_id.set(row[1])
        name.set(row[2])
        age.set(row[3])
        gender.set(row[4])
        contact.set(row[5])
        amt_paid.set(row[6])

    def clear_tenants():
        tenant_id.set("")
        room_id.set("")
        name.set("")
        age.set("")
        gender.set("")
        contact.set("")
        amt_paid.set("")

    def delete_tenants():
        conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
        curr = conn.cursor()
        curr.execute("delete from tenants where `tenant_id`=%s", tenant_id.get())
        conn.commit()
        conn.close()
        fetch_data()
        clear_tenants()

    def update_tenants():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("update tenants set `tenant_id` = %s, `room_id` = %s, `tenant_ame`=%s,`gender`=%s, `age`=%s, `contact`=%s where `tenant_id`=%s",
                        (tenant_id.get(), room_id.get(), name.get(), gender.get(), age.get(), contact.get(), amt_paid.get(), tenant_id.get()))
            conn.commit()
            conn.close()
            fetch_data()
            clear_tenants()
        except:
            messagebox.showerror("Error!", "Tenant already exists!")

    def search_tenants():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="Dytuanhanz15", database="bhms")
            curr = conn.cursor()
            curr.execute("select * from tenants where `tenant_id`=%s", tenant_id.get())
            row = curr.fetchone()

            tenant_id.set(row[0])
            room_id.set(row[1])
            name.set(row[2])
            age.set(row[3])
            gender.set(row[4])
            contact.set(row[5])
            amt_paid.set(row[6])

            conn.commit()

        except:
            tkinter.messagebox.showinfo("data entry form", "No student found")
            clear_tenants()
            conn.close()

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

    student_table = ttk.Treeview(main_frame, columns=("Tenant ID", "Room ID", "Name", "Gender", "Age", "Contact", "Amount Paid"),
                                 yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    student_table.heading("Tenant ID", text="Tenant ID")
    student_table.heading("Room ID", text="Room ID")  
    student_table.heading("Name", text="Name")
    student_table.heading("Gender", text="Gender")
    student_table.heading("Age", text="Age")
    student_table.heading("Contact", text="Contact")
    student_table.heading("Amount Paid", text="Amount Paid")


    student_table['show'] = 'headings'

    student_table.column("Tenant ID", width=100)
    student_table.column("Room ID", width=100)
    student_table.column("Name", width=100)
    student_table.column("Gender", width=100)
    student_table.column("Age", width=100)
    student_table.column("Contact", width=100)
    student_table.column("Amount Paid", width=100)
        
    student_table.pack(fill=tk.BOTH, expand=True)

    fetch_data()

    student_table.bind("<ButtonRelease-1>", get_cursor)

    button1 = Button(root, text='ROOMS', font=('Times_New_Roman', 15), command=tab2)
    button1.pack(side=BOTTOM)


tab1()

root.mainloop()

