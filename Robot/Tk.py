import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age based on DOB
def calculate_age():
    try:
        dob = entry_dob.get()
        dob_date = datetime.strptime(dob, "%Y-%m-%d")  # Expected format: YYYY-MM-DD
        today = datetime.today()
        
        # Calculate age
        age = today.year - dob_date.year
        if today.month < dob_date.month or (today.month == dob_date.month and today.day < dob_date.day):
            age -= 1
        
        label_result.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in the format YYYY-MM-DD.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place the widgets
label_instruction = tk.Label(root, text="Enter your Date of Birth (YYYY-MM-DD):")
label_instruction.pack(pady=10)

entry_dob = tk.Entry(root)
entry_dob.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="Your age will be displayed here.")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
