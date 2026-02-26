import tkinter as tk
from tkinter import messagebox

# predefined credentials
USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome! Login successful.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
