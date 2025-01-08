import tkinter as tk

window = tk.Tk()
window.title("GUI program")
window.geometry("400x300")

entry = tk.Entry(window)
entry.pack(pady=5)

frame = tk.Frame()
frame.pack()

def process():
  empty_label.config(text=entry.get())

def reset_process():
  empty_label.config(text="")

submit = tk.Button(frame, text="Submit", command=process)
submit.grid(row=0, column=0)

reset = tk.Button(frame, text="Reset", command=reset_process)
reset.grid(row=0, column=1)

empty_label = tk.Label(window, text="")
empty_label.pack(pady=10)

window.mainloop()