import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# MySQL connection details
HOST = "192.168.126.204"
USER = "user"
PASSWORD = "Guru@5104"
DATABASE = "dbms"

def connect_db():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def add_customer_window():
    add_cust_win = tk.Toplevel(user_app)
    add_cust_win.title("Add Customer")
    add_cust_win.configure(bg="#2E2E2E")

    ttk.Label(add_cust_win, text="Name:").grid(row=0, column=0, padx=10, pady=10)
    cust_name_entry = ttk.Entry(add_cust_win)
    cust_name_entry.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(add_cust_win, text="Phone Number:").grid(row=1, column=0, padx=10, pady=10)
    phno_entry = ttk.Entry(add_cust_win)
    phno_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(add_cust_win, text="Email:").grid(row=2, column=0, padx=10, pady=10)
    email_entry = ttk.Entry(add_cust_win)
    email_entry.grid(row=2, column=1, padx=10, pady=10)
    
    ttk.Label(add_cust_win, text="Address:").grid(row=3, column=0, padx=10, pady=10)
    address_entry = ttk.Entry(add_cust_win)
    address_entry.grid(row=3, column=1, padx=10, pady=10)
    
    def add_customer():
        cust_name = cust_name_entry.get()
        phno = phno_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (cust_name, phno, email, address) VALUES (%s, %s, %s, %s)", (cust_name, phno, email, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully")
        add_cust_win.destroy()

    ttk.Button(add_cust_win, text="Add Customer", command=add_customer).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def add_sales_window():
    add_sales_win = tk.Toplevel(user_app)
    add_sales_win.title("Add Sales Record")
    add_sales_win.configure(bg="#2E2E2E")

    ttk.Label(add_sales_win, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
    sales_customer_id_entry = ttk.Entry(add_sales_win)
    sales_customer_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(add_sales_win, text="Part:").grid(row=1, column=0, padx=10, pady=10)
    part_entry = ttk.Entry(add_sales_win)
    part_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def add_sales():
        customer_id = sales_customer_id_entry.get()
        part = part_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (customer_id, part) VALUES (%s, %s)", (customer_id, part))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Sales record added successfully")
        add_sales_win.destroy()

    ttk.Button(add_sales_win, text="Add Sales Record", command=add_sales).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def add_service_window():
    add_service_win = tk.Toplevel(user_app)
    add_service_win.title("Add Service Record")
    add_service_win.configure(bg="#2E2E2E")

    ttk.Label(add_service_win, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
    service_customer_id_entry = ttk.Entry(add_service_win)
    service_customer_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(add_service_win, text="Service:").grid(row=1, column=0, padx=10, pady=10)
    service_entry = ttk.Entry(add_service_win)
    service_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(add_service_win, text="Status:").grid(row=2, column=0, padx=10, pady=10)
    status_entry = ttk.Entry(add_service_win)
    status_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def add_service():
        customer_id = service_customer_id_entry.get()
        service = service_entry.get()
        status = status_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO service (customer_id, service, status) VALUES (%s, %s, %s)", (customer_id, service, status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Service record added successfully")
        add_service_win.destroy()

    ttk.Button(add_service_win, text="Add Service Record", command=add_service).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def add_rating_window():
    add_rating_win = tk.Toplevel(user_app)
    add_rating_win.title("Add Rating and Comment")
    add_rating_win.configure(bg="#2E2E2E")

    ttk.Label(add_rating_win, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
    rating_customer_id_entry = ttk.Entry(add_rating_win)
    rating_customer_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(add_rating_win, text="Rating:").grid(row=1, column=0, padx=10, pady=10)
    rating_entry = ttk.Entry(add_rating_win)
    rating_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(add_rating_win, text="Comment:").grid(row=2, column=0, padx=10, pady=10)
    comment_entry = ttk.Entry(add_rating_win)
    comment_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def add_rating():
        customer_id = rating_customer_id_entry.get()
        rating = rating_entry.get()
        comment = comment_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rating_comment (customer_id, rating, comment) VALUES (%s, %s, %s)", (customer_id, rating, comment))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Rating and comment added successfully")
        add_rating_win.destroy()

    ttk.Button(add_rating_win, text="Add Rating and Comment", command=add_rating).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def add_issue_window():
    add_issue_win = tk.Toplevel(user_app)
    add_issue_win.title("Add Issue")
    add_issue_win.configure(bg="#2E2E2E")

    ttk.Label(add_issue_win, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10)
    issue_customer_id_entry = ttk.Entry(add_issue_win)
    issue_customer_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(add_issue_win, text="Issue Type:").grid(row=1, column=0, padx=10, pady=10)
    issue_type_entry = ttk.Entry(add_issue_win)
    issue_type_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(add_issue_win, text="Issue Description:").grid(row=2, column=0, padx=10, pady=10)
    issue_description_entry = ttk.Entry(add_issue_win)
    issue_description_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def add_issue():
        customer_id = issue_customer_id_entry.get()
        issue_type = issue_type_entry.get()
        issue_description = issue_description_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO issues (customer_id, issue_type, issue_description) VALUES (%s, %s, %s)", (customer_id, issue_type, issue_description))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Issue added successfully")
        add_issue_win.destroy()

    ttk.Button(add_issue_win, text="Add Issue", command=add_issue).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Function to apply dark theme to the buttons
def apply_dark_theme():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", foreground="white", background="#1E1E1E", font=('Helvetica', 12))
    style.configure("TLabel", foreground="white", background="#2E2E2E", font=('Helvetica', 12))
    style.configure("TEntry", foreground="white", background="#333333", fieldbackground="#333333", font=('Helvetica', 12))
    style.map('TButton', background=[('active', '#333333')])

# GUI setup
user_app = tk.Tk()
user_app.title("User Panel")
user_app.configure(bg="#2E2E2E")

# Maximize the window
user_app.state('zoomed')

apply_dark_theme()

# Align all elements to the center
container = tk.Frame(user_app, bg="#2E2E2E")
container.place(relx=0.5, rely=0.5, anchor='center')

ttk.Button(container, text="New Customer", command=add_customer_window).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(container, text="Buy", command=add_sales_window).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(container, text="Service", command=add_service_window).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(container, text="Rate and Comment", command=add_rating_window).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(container, text="Raise Issue", command=add_issue_window).grid(row=9, column=0, columnspan=2, padx=10, pady=10)

user_app.mainloop()
