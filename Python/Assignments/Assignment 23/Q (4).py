import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "q": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Pune", "Chennai"],
        "answer": "Delhi"
    },
    {
        "q": "Which language is used for web apps?",
        "options": ["Python", "Java", "HTML", "All"],
        "answer": "All"
    }
]

index = 0

def check_answer():
    global index
    if selected.get() == questions[index]["answer"]:
        messagebox.showinfo("Correct", "Correct Answer!")
    else:
        messagebox.showerror("Wrong", "Wrong Answer")

    index += 1
    if index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz", "Quiz Completed")
        root.destroy()

def load_question():
    selected.set(None)
    lbl_question.config(text=questions[index]["q"])

    for i in range(4):
        options[i].config(text=questions[index]["options"][i],
                          value=questions[index]["options"][i])

root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

lbl_question = tk.Label(root, text="", wraplength=350)
lbl_question.pack(pady=10)

selected = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected, value="")
    rb.pack(anchor="w")
    options.append(rb)

tk.Button(root, text="Next", command=check_answer).pack(pady=10)

load_question()
root.mainloop()
