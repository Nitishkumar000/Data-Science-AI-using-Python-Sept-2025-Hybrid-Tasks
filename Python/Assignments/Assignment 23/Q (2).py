import tkinter as tk

# simple fixed rates
rates = {
    "INR": 83,
    "USD": 1,
    "EUR": 90
}

def convert():
    amount = float(entry_amount.get())
    from_cur = from_currency.get()
    to_cur = to_currency.get()

    result = amount * rates[to_cur] / rates[from_cur]
    lbl_result.config(text=f"Converted Amount: {result:.2f}")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x250")

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

from_currency = tk.StringVar(value="INR")
to_currency = tk.StringVar(value="USD")

tk.Label(root, text="From Currency").pack()
tk.OptionMenu(root, from_currency, *rates.keys()).pack()

tk.Label(root, text="To Currency").pack()
tk.OptionMenu(root, to_currency, *rates.keys()).pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)

lbl_result = tk.Label(root, text="Converted Amount:")
lbl_result.pack()

root.mainloop()
