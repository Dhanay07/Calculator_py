import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

root = tk.Tk()
root.title("Basic Calculator")

result = tk.StringVar()

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0)

btn_add = tk.Button(root, text="+", command=lambda: calculate('+'))
btn_add.grid(row=2, column=0)
btn_sub = tk.Button(root, text="-", command=lambda: calculate('-'))
btn_sub.grid(row=2, column=1)
btn_mul = tk.Button(root, text="*", command=lambda: calculate('*'))
btn_mul.grid(row=2, column=2)
btn_div = tk.Button(root, text="/", command=lambda: calculate('/'))
btn_div.grid(row=2, column=3)

btn_reset = tk.Button(root, text="Reset", command=reset)
btn_reset.grid(row=3, column=1, columnspan=2)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0)
entry_result = tk.Entry(root, textvariable=result, state='readonly')
entry_result.grid(row=4, column=1)

root.mainloop()
