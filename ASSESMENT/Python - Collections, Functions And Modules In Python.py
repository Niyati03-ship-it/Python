import tkinter as tk
from tkinter import messagebox

orders = []
GST = 5

def add_order():
    name = e_name.get()
    device = e_device.get()
    issue = e_issue.get()
    due = e_due.get()

    if name == "" or device == "" or issue == "" or due == "":
        messagebox.showerror("Error", "All fields required")
        return

    order = {
        "name": name,
        "device": device,
        "issue": issue,
        "due": due
    }

    orders.append(order)
    listbox.insert(tk.END, name + " - " + device)

    e_name.delete(0, tk.END)
    e_device.delete(0, tk.END)
    e_issue.delete(0, tk.END)
    e_due.delete(0, tk.END)

    messagebox.showinfo("Success", "Order Added")


def generate_bill():
    try:
        index = listbox.curselection()[0]
        order = orders[index]
    except:
        messagebox.showerror("Error", "Select order")
        return

    try:
        repair_fee = float(e_repair.get())
        parts_cost = float(e_parts.get())
        gst = float(e_gst.get())
        discount = float(e_discount.get())
    except:
        messagebox.showerror("Error", "Enter valid numbers")
        return

    subtotal = repair_fee + parts_cost
    tax = subtotal * gst / 100
    total = subtotal + tax - discount

    bill = f"""
Customer : {order['name']}
Device   : {order['device']}
Issue    : {order['issue']}

Repair Fee : {repair_fee}
Parts Cost : {parts_cost}
GST%  : {tax:.2f}
Discount  : {discount}

Total     : {total:.2f}
"""

    messagebox.showinfo("Invoice", bill)


root = tk.Tk()
root.title("FixTrack")
root.geometry("400x550")

tk.Label(root, text="FixTrack Repair System", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Customer Name").pack()
e_name = tk.Entry(root)
e_name.pack()

tk.Label(root, text="Device Type").pack()
e_device = tk.Entry(root)
e_device.pack()

tk.Label(root, text="Issue").pack()
e_issue = tk.Entry(root)
e_issue.pack()

tk.Label(root, text="Due Date").pack()
e_due = tk.Entry(root)
e_due.pack()

tk.Button(root, text="Add Repair Order", command=add_order).pack(pady=8)

tk.Label(root, text="Orders").pack()
listbox = tk.Listbox(root, width=35)
listbox.pack(pady=5)

tk.Label(root, text="Repair Fee").pack()
e_repair = tk.Entry(root)
e_repair.pack()

tk.Label(root, text="Parts Cost").pack()
e_parts = tk.Entry(root)
e_parts.pack()

tk.Label(root, text="GST (%)").pack()
e_gst = tk.Entry(root)
e_gst.insert(0, str(GST))
e_gst.pack()

tk.Label(root, text="Discount").pack()
e_discount = tk.Entry(root)
e_discount.pack()

tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=15)

root.mainloop()
