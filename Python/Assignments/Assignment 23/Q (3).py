import tkinter as tk

def calculate(op):
    a = float(entry1.get())
    b = float(entry2.get())

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b

    lbl_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="+", width=5, command=lambda: calculate("+")).pack()
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).pack()
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).pack()
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).pack()

lbl_result = tk.Label(root, text="Result:")
lbl_result.pack(pady=10)

root.mainloop()
