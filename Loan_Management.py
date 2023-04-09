# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 00:59:31 2023
@author:  © RAJAT_KUNDU 
"""

import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
 
 
class LoanManager:
    def __init__(self, root):
        # Initialize the class with the root window passed as an argument
        self.root = root
        # Set the title and size of the root window
        self.root.title("Loan Management System  © hack_limitless")
        self.root.geometry("1350x720+0+0")
        # Create a label with the title text and style it
        title = Label(self.root, text="Loan Management System", font=(
            "Comic Sans MS", 20, ), bd=8,  bg='black', fg='yellow')
        title.pack(side=TOP, fill=X)
        # Create StringVar variables to store the loan details
        self.LoanId = StringVar()
        self.name = StringVar()
        self.mob = StringVar()
        self.aadhar = StringVar()
        self.add = StringVar()
        self.pin = StringVar()
        self.amount = StringVar()
        self.year = StringVar()
        self.rate = StringVar()
        self.mpay = StringVar()
        self.tpay = StringVar()
 
        # Create a frame to hold the loan details
        Detail_F = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        Detail_F.place(x=10, y=90, width=520, height=620)
 
        # Create a label and entry field for the loan ID
        lbl_id = Label(Detail_F, text="Loan Id", font=("Comic Sans MS", 12, ))
        lbl_id.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        txt_id = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                       bd=3,  textvariable=self.LoanId)
        txt_id.grid(row=0, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the name
        lbl_name = Label(Detail_F, text="Full Name",
                         font=("Comic Sans MS", 12, ))
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                         bd=3,  textvariable=self.name)
        txt_name.grid(row=1, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the mobile number
        lbl_mob = Label(Detail_F, text="Mobile No.",
                        font=("Comic Sans MS", 12, ))
        lbl_mob.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_mob = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                        bd=3,  textvariable=self.mob)
        txt_mob.grid(row=2, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the Aadhar number
        lbl_aa = Label(Detail_F, text="Aadhar No.",
                       font=("Comic Sans MS", 12, ))
        lbl_aa.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_aa = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                       bd=3,  textvariable=self.aadhar)
        txt_aa.grid(row=3, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the address
        lbl_add = Label(Detail_F, text="Address", font=("Comic Sans MS", 12, ))
        lbl_add.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_add = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                        bd=3,  textvariable=self.add)
        txt_add.grid(row=4, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the pincode
        lbl_pin = Label(Detail_F, text="PinCode", font=("Comic Sans MS", 12, ))
        lbl_pin.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_pin = Entry(Detail_F, font=("Comic Sans MS", 10, ),
                        bd=3,  textvariable=self.pin)
        txt_pin.grid(row=5, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the loan amount
        lbl_amount = Label(Detail_F, text="Amount of Loan",
                           font=("Comic Sans MS", 12, ))
        lbl_amount.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_amount = Entry(Detail_F, font=(
            "Comic Sans MS", 10, ), bd=3,  textvariable=self.amount)
        txt_amount.grid(row=6, column=1, pady=10, sticky="w")
 
        # Create a label and entry field for the number of years
        lbl_time = Label(Detail_F, text="Number of years",
                         font=("Comic Sans MS", 12, ))
        lbl_time.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_time = Entry(Detail_F, font=("Comic Sans MS", 10,
                                         ), bd=3,  textvariable=self.year)
        txt_time.grid(row=7, column=1, pady=10, sticky="w")
        # Create a label and entry field for the interest rate
        lbl_rate = Label(Detail_F, text="Interest Rate/Year",
                         font=("Comic Sans MS", 12, ))
        lbl_rate.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        txt_rate = Entry(Detail_F, font=("Comic Sans MS", 10,
                                         ), bd=3,  textvariable=self.rate)
        txt_rate.grid(row=8, column=1, pady=10, sticky="w")
        # Create a label and entry field for the monthly payment
        lbl_Mp = Label(Detail_F, text="Monthly Interest Payment",
                       font=("Comic Sans MS", 12, ))
        lbl_Mp.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        txt_Mp = Label(Detail_F, font=("Comic Sans MS", 10, ),
                       bd=3,  state=DISABLED, textvariable=self.mpay)
        txt_Mp.grid(row=9, column=1, pady=10, sticky="w")
        # Create a label and entry field for the total payment
        lbl_tp = Label(Detail_F, text="Total Payment",
                       font=("Comic Sans MS", 12, ))
        lbl_tp.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        txt_tp = Label(Detail_F, font=("Comic Sans MS", 10, ),
                       bd=3,  state=DISABLED, textvariable=self.tpay)
        txt_tp.grid(row=10, column=1, pady=10, sticky="w")
        recordFrame = Frame(self.root, bd=5, relief=RIDGE)
        recordFrame.place(x=535, y=100, width=810, height=530)
 
        yscroll = Scrollbar(recordFrame, orient=VERTICAL)
        # Create a treeview to display the records
        self.employee_table = ttk.Treeview(recordFrame, columns=(
            "empId", "name", "years", "rate", "Mpayment", "Tpayment", "mobile"), yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading("empId", text="Customer Id")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("years", text="Number of Years")
        self.employee_table.heading("rate", text="Interest Rate/Year")
        self.employee_table.heading("Mpayment", text="Monthly Interest Payment")
        self.employee_table.heading("Tpayment", text="Total Payment")
        self.employee_table.heading("mobile", text="Mobile No.")
 
        self.employee_table['show'] = 'headings'
 
        self.employee_table.column("empId", width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("years", width=100)
        self.employee_table.column("rate", width=100)
        self.employee_table.column("Mpayment", width=110)
        self.employee_table.column("Tpayment", width=100)
        self.employee_table.column("mobile", width=100)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        btnFrame = Frame(self.root, bd=5, relief=RIDGE)
        btnFrame.place(x=700, y=630, width=480, height=60)
 
        # Create a button to calculate the Details
        btn1 = Button(btnFrame, text='Add record', font='arial 12 bold',
                      bg='black', fg='yellow', width=9, command=self.addrecord)
        btn1.grid(row=0, column=0, padx=10, pady=10)
        # Create a button to update the Details
        btn2 = Button(btnFrame, text='Update', font='arial 12 bold',
                      bg='black', fg='yellow', width=9, command=self.update)
        btn2.grid(row=0, column=1, padx=8, pady=10)
        # Create a button to delete the entr
        btn3 = Button(btnFrame, text='Delete', font='arial 12 bold',
                      bg='black', fg='yellow', width=9, command=self.delete)
        btn3.grid(row=0, column=2, padx=8, pady=10)
        # Create a button to reset the fields
        btn4 = Button(btnFrame, text='Reset', font='arial 12 bold',
                      bg='black', fg='yellow', width=9, command=self.reset)
        btn4.grid(row=0, column=3, padx=8, pady=10)
 
    def total(self):
        # Get the loan amount, interest rate, and number of years as integers
        p = int(self.amount.get())
        r = float(self.rate.get())
        n = int(self.year.get())
 
        # Calculate the total interest to be paid
        t = (p*r*n)/(100)
 
        # Calculate the monthly payment amount
        m = t/(n*12)
 
        # Set the monthly payment and total payment amounts in the corresponding StringVar objects
        self.mpay.set(str(round(m, 2)))
        self.tpay.set(str(t+p))
 
    def addrecord(self):
        if self.LoanId.get() == '' or self.name.get() == '' or self.mob.get() == '' or self.aadhar.get() == '' or self.add.get() == '' or self.pin.get() == '':
            messagebox.showerror('Error', 'Please enter details ?')
        else:
            self.total()
            con = sqlite3.connect('loanDetails.db')
            cur = con.cursor()
            cur.execute("Select * from customer")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == self.LoanId.get():
                    messagebox.showerror(
                        'Error', 'Duplicates not allowed')
                    return
            cur.execute("insert into customer values(?,?,?,?,?,?,?,?,?,?,?)", (
                self.LoanId.get(),
                self.name.get(),
                self.mob.get(),
                self.aadhar.get(),
                self.add.get(),
                self.pin.get(),
                self.amount.get(),
                self.year.get(),
                self.rate.get(),
                self.mpay.get(),
                self.tpay.get(),
            ))
            con.commit()
            self.fetch_data()
            con.close()
 
    def fetch_data(self):
        con = sqlite3.connect('loanDetails.db')
        cur = con.cursor()
        cur.execute("select Loan_Id , Name , Year , Rate , Monthly_Payment , Total_Payment , MobileNumber , AadharNumber , Address , Pincode , Amount from customer")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
        con.commit()
        con.close()
 
    def update(self):
        if self.LoanId.get() == '':
            messagebox.showerror('Error', 'Select a record to update !')
        else:
            self.total()
            con = sqlite3.connect('loanDetails.db')
            cur = con.cursor()
            cur.execute("update customer set Name = ?, MobileNumber = ?, AadharNumber = ?, Address = ?, Pincode = ?, Amount = ?, Year = ?, Rate = ?, Total_Payment = ?, Monthly_Payment = ? where Loan_Id = ?", (
                self.name.get(),
                self.mob.get(),
                self.aadhar.get(),
                self.add.get(),
                self.pin.get(),
                self.amount.get(),
                self.year.get(),
                self.rate.get(),
                self.tpay.get(),
                self.mpay.get(),
                self.LoanId.get()
            ))
            messagebox.showinfo(
                'Info', f'Record {self.LoanId.get()} Updated Successfully')
            con.commit()
            con.close()
            self.fetch_data()
            self.reset()
 
    def delete(self):
        if self.LoanId.get() == '':
            messagebox.showerror(
                'Error', 'Enter customer ID to delete the records')
        else:
            con = sqlite3.connect('loanDetails.db')
            cur = con.cursor()
            cur.execute("delete from customer where Loan_Id = ?",
                        (self.LoanId.get(),))
            con.commit()
            con.close()
            self.fetch_data()
            self.reset()
 
    def reset(self):
        self.LoanId.set('')
        self.name.set('')
        self.mob.set('')
        self.aadhar.set('')
        self.add.set('')
        self.pin.set('')
        self.amount.set('')
        self.year.set('')
        self.rate.set('')
        self.mpay.set('')
        self.tpay.set('')
 
    def get_cursor(self, ev):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        row = content['values']
        self.LoanId.set(row[0])
        self.name.set(row[1])
        self.year.set(row[2])
        self.rate.set(row[3])
        self.mpay.set(row[4])
        self.tpay.set(row[5])
        self.mob.set(row[6])
        self.aadhar.set(row[7])
        self.add.set(row[8])
        self.pin.set(row[9])
        self.amount.set(row[10])
 
 
class Login():
    def __init__(self, root):
        # Initialize the class with the root window passed as an argument
        self.root = root
        # Set the title of the root window
        self.root.title("Loan Management System © hack_limitless")
        # Create StringVar variables to store the username and password
        self.username = StringVar()
        self.password = StringVar()
 
        # Create a label and entry field for the username
        Label(self.root, text="Username:").grid(
            row=0, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.username).grid(
            row=0, column=1, padx=10, pady=10)
        # Create a label and entry field for the password
        Label(self.root, text="Password:").grid(
            row=1, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.password,
              show="*").grid(row=1, column=1, padx=10, pady=10)
        # Create a login button that calls the login method when clicked
        Button(self.root, text="Login", command=self.login).grid(
            row=2, column=1, padx=10, pady=10)
 
    def login(self):
        # Check if the entered username and password are correct
        if self.username.get() == "admin" and self.password.get() == "admin":
            # If the login is successful, destroy the current window and open a new window
            root.destroy()
            nroot = Tk()
            LoanManager(nroot)
        else:
            # If the login is unsuccessful, show an error message
            messagebox.showerror("Error", "Invalid username or password")
 
 
# Connect to the 'loanDetails.db' database
con = sqlite3.connect('loanDetails.db')
# Create a cursor to perform operations on the database
cur = con.cursor()
# Execute a SQL query to create a table named 'customer' if it doesn't already exist
# The table has 10 columns: Loan_Id, Name, MobileNumber, AadharNumber, Address, Pincode, Amount, Year, Rate, and Monthly_Payment, Total_Payment
# The Loan_Id column is set as the primary key
cur.execute('create table if not exists customer(Loan_Id varchar(20) primary key,Name varchar(20),MobileNumber varchar(20),AadharNumber varchar(20),Address varchar(20),Pincode varchar(20),Amount varchar(20),Year varchar(20),Rate varchar(20),Monthly_Payment varchar(20),Total_Payment varchar(20))')
 
# Create a Tkinter root window
root = Tk()
# Create a Login object and pass the root window as an argument
obj = Login(root)
# if u want to skip the login proess then uncomment the below line and comment the above line
# obj = LoanManager(root)
# Start the main loop of the Tkinter program
root.mainloop()
