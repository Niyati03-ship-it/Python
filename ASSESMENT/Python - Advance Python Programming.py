
import tkinter as tk
from tkinter import messagebox
import pymysql
import re
from datetime import datetime, timedelta

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        autocommit=True
    )
    cur = conn.cursor()
except:
    messagebox.showerror("Error", "MySQL Connection Failed")
    exit()

cur.execute("CREATE DATABASE IF NOT EXISTS libradesk")
cur.execute("USE libradesk")

cur.execute("""
CREATE TABLE IF NOT EXISTS members(
    mid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS books(
    isbn VARCHAR(20) PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(50),
    available INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS borrow(
    isbn VARCHAR(20),
    mid INT,
    issue_date DATE,
    return_date DATE
)
""")

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        cur.execute(
            "INSERT INTO members(name, phone) VALUES (%s,%s)",
            (self.name, self.phone)
        )

class Book:
    def __init__(self, isbn, title, author, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre

    def save(self):
        cur.execute(
            "INSERT INTO books VALUES (%s,%s,%s,%s,%s)",
            (self.isbn, self.title, self.author, self.genre, 1)
        )

class BorrowSystem:
    def borrow_book(self, isbn, mid):
        cur.execute("SELECT available FROM books WHERE isbn=%s", (isbn,))
        data = cur.fetchone()

        if not data or data[0] == 0:
            raise Exception("Book not available")

        issue = datetime.now().date()
        due = issue + timedelta(days=7)

        cur.execute(
            "INSERT INTO borrow VALUES (%s,%s,%s,%s)",
            (isbn, mid, issue, due)
        )
        cur.execute(
            "UPDATE books SET available=0 WHERE isbn=%s",
            (isbn,)
        )

    def return_book(self, isbn):
        cur.execute(
            "SELECT return_date FROM borrow WHERE isbn=%s",
            (isbn,)
        )
        data = cur.fetchone()

        if not data:
            raise Exception("Invalid ISBN")

        due = data[0]
        today = datetime.now().date()

        fine = max(0, (today - due).days * 10)
        gst = fine * 0.18
        total = fine + gst

        with open("invoice.txt", "w") as f:
            f.write("LibraDesk Invoice\n")
            f.write(f"ISBN: {isbn}\n")
            f.write(f"Fine: {fine}\n")
            f.write(f"GST: {gst}\n")
            f.write(f"Total: {total}\n")

        cur.execute("DELETE FROM borrow WHERE isbn=%s", (isbn,))
        cur.execute(
            "UPDATE books SET available=1 WHERE isbn=%s",
            (isbn,)
        )

        return total

system = BorrowSystem()

app = tk.Tk()
app.title("LibraDesk")
app.geometry("520x620")

def add_member():
    try:
        Member(m_name.get(), m_phone.get()).save()
        messagebox.showinfo("Success", "Member Added")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_book():
    try:
        Book(
            b_isbn.get(),
            b_title.get(),
            b_author.get(),
            b_genre.get()
        ).save()
        messagebox.showinfo("Success", "Book Added")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def borrow_book():
    try:
        system.borrow_book(br_isbn.get(), int(br_mid.get()))
        messagebox.showinfo("Success", "Book Borrowed")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def return_book():
    try:
        amount = system.return_book(rt_isbn.get())
        messagebox.showinfo("Returned", f"Fine: {amount}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_book():
    try:
        result.delete(0, tk.END)
        key = search_entry.get()
        cur.execute("SELECT * FROM books")
        for row in cur.fetchall():
            if re.search(key, row[1], re.IGNORECASE):
                result.insert(tk.END, row)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def label(text):
    tk.Label(app, text=text, font=("Arial", 10, "bold")).pack()

label("Member Name")
m_name = tk.Entry(app)
m_name.pack()

label("Phone Number")
m_phone = tk.Entry(app)
m_phone.pack()

tk.Button(app, text="Add Member", command=add_member).pack(pady=5)

label("Book ISBN")
b_isbn = tk.Entry(app)
b_isbn.pack()

label("Book Title")
b_title = tk.Entry(app)
b_title.pack()

label("Author Name")
b_author = tk.Entry(app)
b_author.pack()

label("Genre")
b_genre = tk.Entry(app)
b_genre.pack()

tk.Button(app, text="Add Book", command=add_book).pack(pady=5)

label("Borrow - Book ISBN")
br_isbn = tk.Entry(app)
br_isbn.pack()

label("Member ID")
br_mid = tk.Entry(app)
br_mid.pack()

tk.Button(app, text="Borrow Book", command=borrow_book).pack(pady=5)

label("Return - Book ISBN")
rt_isbn = tk.Entry(app)
rt_isbn.pack()

tk.Button(app, text="Return Book", command=return_book).pack(pady=5)

label("Search Book Title")
search_entry = tk.Entry(app)
search_entry.pack()

tk.Button(app, text="Search", command=search_book).pack(pady=5)

result = tk.Listbox(app, width=65)
result.pack(pady=10)
app.mainloop()