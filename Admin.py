import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from sqlalchemy import create_engine

# MySQL connection details (replace with your actual credentials)
HOST = "localhost"
USER = "root"
PASSWORD = "Guru@2004"
DATABASE = "dbms"

def connect_db():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def open_add_customer_window():
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
        add_customer_win.destroy()

    add_customer_win = tk.Toplevel(admin_app)
    add_customer_win.title("Add Customer")
    center_window(add_customer_win, 400, 300)
    add_customer_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(add_customer_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Name:").grid(row=0, column=0, pady=5, padx=5)
    cust_name_entry = ttk.Entry(frame)
    cust_name_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(frame, text="Phone Number:").grid(row=1, column=0, pady=5, padx=5)
    phno_entry = ttk.Entry(frame)
    phno_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Label(frame, text="Email:").grid(row=2, column=0, pady=5, padx=5)
    email_entry = ttk.Entry(frame)
    email_entry.grid(row=2, column=1, pady=5, padx=5)

    ttk.Label(frame, text="Address:").grid(row=3, column=0, pady=5, padx=5)
    address_entry = ttk.Entry(frame)
    address_entry.grid(row=3, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Add Customer", command=add_customer).grid(row=4, column=0, columnspan=2, pady=10)

def open_delete_customer_window():
    def delete_customer():
        customer_id = delete_customer_id_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer deleted successfully")
        delete_customer_win.destroy()

    delete_customer_win = tk.Toplevel(admin_app)
    delete_customer_win.title("Delete Customer")
    center_window(delete_customer_win, 400, 200)
    delete_customer_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(delete_customer_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Customer ID:").grid(row=0, column=0, pady=5, padx=5)
    delete_customer_id_entry = ttk.Entry(frame)
    delete_customer_id_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Delete Customer", command=delete_customer).grid(row=1, column=0, columnspan=2, pady=10)

def open_search_customer_window():
    def search_customer():
        search_value = search_entry.get()
        search_by = search_option.get()

        conn = connect_db()
        cursor = conn.cursor()
        if search_by == "Phone Number":
            cursor.execute("SELECT * FROM customers WHERE phno = %s", (search_value,))
        else:
            cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (search_value,))
        result = cursor.fetchall()
        conn.close()

        search_result_table.delete(*search_result_table.get_children())
        for row in result:
            search_result_table.insert('', 'end', values=row)

    search_customer_win = tk.Toplevel(admin_app)
    search_customer_win.title("Search Customer")
    center_window(search_customer_win, 600, 400)
    search_customer_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(search_customer_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Search By:").grid(row=0, column=0, pady=5, padx=5)
    search_option = ttk.Combobox(frame, values=["Phone Number", "Customer ID"])
    search_option.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(frame, text="Value:").grid(row=1, column=0, pady=5, padx=5)
    search_entry = ttk.Entry(frame)
    search_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Search Customer", command=search_customer).grid(row=2, column=0, columnspan=2, pady=10)

    columns = ('customer_id', 'cust_name', 'phno', 'email', 'address')
    search_result_table = ttk.Treeview(frame, columns=columns, show='headings')
    for col in columns:
        search_result_table.heading(col, text=col)
        search_result_table.column(col, width=100)
    search_result_table.grid(row=3, column=0, columnspan=2, pady=10)

def open_update_status_window():
    def update_status(status):
        service_number = update_status_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE service SET status = %s WHERE service_number = %s", (status, service_number,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Service status updated to '{status}'")
        update_status_win.destroy()

    update_status_win = tk.Toplevel(admin_app)
    update_status_win.title("Update Service Status")
    center_window(update_status_win, 400, 200)
    update_status_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(update_status_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Service Number:").grid(row=0, column=0, pady=5, padx=5)
    update_status_entry = ttk.Entry(frame)
    update_status_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Set to Pending", command=lambda: update_status('pending')).grid(row=1, column=0, pady=10, padx=5)
    ttk.Button(frame, text="Set to Complete", command=lambda: update_status('complete')).grid(row=1, column=1, pady=10, padx=5)

def open_display_summary_window():
    def display_summary():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer_overview")
        result = cursor.fetchall()
        conn.close()

        summary_table.delete(*summary_table.get_children())
        for row in result:
            summary_table.insert('', 'end', values=row)

    display_summary_win = tk.Toplevel(admin_app)
    display_summary_win.title("Summary")
    center_window(display_summary_win, 800, 600)
    display_summary_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(display_summary_win)
    frame.pack(expand=True)

    columns = ('cust_name', 'Sales', 'service', 'rating')
    summary_table = ttk.Treeview(frame, columns=columns, show='headings')
    for col in columns:
        summary_table.heading(col, text=col)
        summary_table.column(col, width=200)
    summary_table.grid(row=0, column=0, sticky='nsew', pady=10)

    ttk.Button(frame, text="Refresh", command=display_summary).grid(row=1, column=0, pady=10)

def generate_report():
    conn = connect_db()
    query = "SELECT * FROM customer_overview"
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv("customer_overview_report.csv", index=False)
    messagebox.showinfo("Success", "Report generated and saved as 'customer_overview_report.csv'")

def open_send_email_window():
    def send_email():
        recipient_email = email_entry.get()
        subject = "Customer Overview Report"
        body = "Please find the attached report."

        msg = MIMEMultipart()
        msg['From'] = 'guruprasaaths.22cse@kongu.edu'
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open("customer_overview_report.csv", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= customer_overview_report.csv")
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        try:
            server.login('guruprasaaths.22cse@kongu.edu', 'Rathy@2005')  # Replace with your email and app-specific password
            text = msg.as_string()
            server.sendmail('guruprasaaths.22cse@kongu.edu', recipient_email, text)
            messagebox.showinfo("Success", "Email sent successfully")
        except smtplib.SMTPAuthenticationError as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
        finally:
            server.quit()

    send_email_win = tk.Toplevel(admin_app)
    send_email_win.title("Send Email Report")
    center_window(send_email_win, 400, 200)
    send_email_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(send_email_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Recipient Email:").grid(row=0, column=0, pady=5, padx=5)
    email_entry = ttk.Entry(frame)
    email_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Send Email", command=send_email).grid(row=1, column=0, columnspan=2, pady=10)

def open_delete_sales_window():
    def delete_sales():
        column = delete_sales_column_entry.get()
        condition = delete_sales_condition_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM sales WHERE {column} = %s", (condition,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Sales record deleted successfully")
        delete_sales_win.destroy()

    delete_sales_win = tk.Toplevel(admin_app)
    delete_sales_win.title("Delete Sales Record")
    center_window(delete_sales_win, 400, 200)
    delete_sales_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(delete_sales_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Column:").grid(row=0, column=0, pady=5, padx=5)
    delete_sales_column_entry = ttk.Entry(frame)
    delete_sales_column_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Label(frame, text="Condition:").grid(row=1, column=0, pady=5, padx=5)
    delete_sales_condition_entry = ttk.Entry(frame)
    delete_sales_condition_entry.grid(row=1, column=1, pady=5, padx=5)

    ttk.Button(frame, text="Delete Sales Record", command=delete_sales).grid(row=2, column=0, columnspan=2, pady=10)

def open_view_issue_window():
    def view_issue():
        customer_id = view_issue_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM issues WHERE customer_id = %s", (customer_id,))
        result = cursor.fetchall()
        conn.close()

        issue_text.delete('1.0', tk.END)
        for row in result:
            issue_text.insert(tk.END, f"{row}\n")

    view_issue_win = tk.Toplevel(admin_app)
    view_issue_win.title("View Issue")
    center_window(view_issue_win, 400, 400)
    view_issue_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(view_issue_win)
    frame.pack(expand=True)

    ttk.Label(frame, text="Customer ID:").grid(row=0, column=0, pady=5, padx=5)
    view_issue_entry = ttk.Entry(frame)
    view_issue_entry.grid(row=0, column=1, pady=5, padx=5)

    ttk.Button(frame, text="View Issue", command=view_issue).grid(row=1, column=0, columnspan=2, pady=10)

    issue_text = tk.Text(frame, height=10, width=50)
    issue_text.grid(row=2, column=0, columnspan=2, pady=10)

def open_view_logs_window():
    def view_logs():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM log_table")
        result = cursor.fetchall()
        conn.close()

        # Clear existing rows in the table
        log_table.delete(*log_table.get_children())
        
        # Insert new rows
        for row in result:
            log_table.insert('', 'end', values=row)

    view_logs_win = tk.Toplevel(admin_app)
    view_logs_win.title("View Logs")
    center_window(view_logs_win, 600, 400)
    view_logs_win.configure(bg="#2E2E2E")

    frame = ttk.Frame(view_logs_win)
    frame.pack(expand=True, fill='both')

    # Define columns based on your log table structure
    columns = ('log_id', 'action', 'cust_id','time')  # Adjust columns as needed
    log_table = ttk.Treeview(frame, columns=columns, show='headings')
    for col in columns:
        log_table.heading(col, text=col)
        log_table.column(col, width=150)
    log_table.pack(expand=True, fill='both', pady=10)

    ttk.Button(frame, text="Refresh", command=view_logs).pack(pady=10)

    # Call view_logs initially to populate the log_table widget
    view_logs()



# Function to center a window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

# Main Admin Application Window
admin_app = tk.Tk()
admin_app.title("Admin Panel")
admin_app.state('zoomed')  # Open maximized
admin_app.configure(bg="#2E2E2E")

# Applying dark theme to the buttons
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground="white", background="#1E1E1E", font=('Helvetica', 12))
style.map('TButton', background=[('active', '#333333')])

# Creating a frame to contain the buttons
button_frame = ttk.Frame(admin_app)
button_frame.pack(expand=True)

buttons = [
    ("Add Customer", open_add_customer_window),
    ("Delete Customer", open_delete_customer_window),
    ("Search Customer", open_search_customer_window),
    ("Update Service Status", open_update_status_window),
    ("Display Summary", open_display_summary_window),
    ("Generate Report", generate_report),
    ("Send Email Report", open_send_email_window),
    ("Delete Sales Record", open_delete_sales_window),
    ("View Issue", open_view_issue_window),
    ("View Logs", open_view_logs_window)
]

for i, (text, command) in enumerate(buttons):
    ttk.Button(button_frame, text=text, command=command).grid(row=i, column=0, padx=20, pady=10)

admin_app.mainloop()
