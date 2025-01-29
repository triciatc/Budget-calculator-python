import tkinter as tk
from tkinter import messagebox

def calculate_budget():
    try:
        total_budget = float(entry_total_budget.get())
        monthly_expenses = float(entry_total_expenses.get())
        result_budget = total_budget/monthly_expenses

        messagebox.showinfo("Final result", f"Your money will last for {result_budget:.2f} months.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Budget Calculator")

tk.Label(root, text="Enter your total budget (£):").grid(row=0, column=0, padx=10, pady=10)
entry_total_budget = tk.Entry(root)
entry_total_budget.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your total monthly expenses (£):").grid(row=1, column=0, padx=10, pady=10)
entry_total_expenses = tk.Entry(root)
entry_total_expenses.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_budget)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 


root.mainloop()