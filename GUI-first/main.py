import tkinter as tk

# Set window and label variable
window = tk.Tk()
greeting = tk.Label(text="Hello, World")
name = tk.Label(text="Jelle")

# Prints the greeting to the window
greeting.pack()
name.pack()

# This keeps the window open in a loop
window.mainloop()