# Import required libraries for GUI and message dialogs
import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x300")  # Set window dimensions

# Create and pack the main title label
calculator_label = tk.Label(window, text="Calculator", font=("TkDefaultFont", 18))
calculator_label.pack()

# Create input field for mathematical expressions
entry = tk.Entry(window, fg="grey")
entry.pack()

def calculate():
    # Get the expression from entry field
    expression = entry.get()
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        # Display result in the result label
        resultLabel.config(text=result)

    except Exception as e:
        # Handle errors and show error message dialog
        print(e)
        messagebox.showerror("Error Occured", "Please check the expression provided")

# Create and pack the submit button
button = tk.Button(window, text="Submit", command=calculate)
button.pack(pady=5)

# Create and pack the label to display results
resultLabel = tk.Label(window, text="")
resultLabel.pack(pady=5)

# Start the main event loop
window.mainloop()
