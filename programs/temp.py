import tkinter as tk
from tkinter import ttk, messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

def on_combobox_select(event):
    selected_value.set(combo.get())

def on_checkbutton_toggle():
    messagebox.showinfo("CheckButton", f"CheckButton state: {var1.get()}")

def on_radiobutton_select():
    messagebox.showinfo("RadioButton", f"Selected radio button: {radio_var.get()}")

# Create the main window
root = tk.Tk()
root.title("Tkinter Widgets Example")

# Label widget
label = tk.Label(root, text="This is a Label widget")
label.pack()

# Button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Entry widget
entry = tk.Entry(root)
entry.pack()

# Combo box widget
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()
selected_value = tk.StringVar()
combo.bind("<<ComboboxSelected>>", on_combobox_select)

# Check button widget
var1 = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me", variable=var1, command=on_checkbutton_toggle)
check_button.pack()

# Radio button widget
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option A", variable=radio_var, value="A", command=on_radiobutton_select)
radio2 = tk.Radiobutton(root, text="Option B", variable=radio_var, value="B", command=on_radiobutton_select)
radio1.pack()
radio2.pack()

# Canvas widget
canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
canvas.create_line(0, 0, 200, 100, fill="red", width=2)
canvas.create_rectangle(50, 25, 150, 75, fill="yellow")
canvas.pack()

# Frame widget
frame = tk.Frame(root, bg="lightgrey", borderwidth=2, relief="sunken")
frame.pack(pady=10)
frame_label = tk.Label(frame, text="This is a Frame widget")
frame_label.pack()

# Message box widget (shown on button click)
message_button = tk.Button(root, text="Show Message Box", command=lambda: messagebox.showinfo("Message Box", "This is a message box."))
message_button.pack()

# Menu widget
menu = tk.Menu(root)
root.config(menu=menu)

# Menu button
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: messagebox.showinfo("Menu", "Open selected"))
file_menu.add_command(label="Save", command=lambda: messagebox.showinfo("Menu", "Save selected"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

m2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Baka", menu=m2)
file_menu.add_command(label="Idiot", command=lambda: messagebox.showinfo("Sussy Baka", "Beluga"))

# Start the main event loop
root.mainloop()