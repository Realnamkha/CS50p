import tkinter as tk
from tkinter import ttk

def on_category_select(event):
    selected_category = category_var.get()
    print("Selected Category:", selected_category)

# Create the main window
root = tk.Tk()
root.title("Category Selection")

# Create a StringVar to hold the selected category
category_var = tk.StringVar()

# Create a Label widget
label = tk.Label(root, text="Select a category:")

# Create a Combobox (dropdown menu) widget
category_combobox = ttk.Combobox(root, textvariable=category_var)
category_combobox['values'] = ("Food", "Stationary", "Travel", "Entertainment", "Others")

# Set the default value for the Combobox
category_combobox.set("Food")

# Bind the event handler to the category Combobox
category_combobox.bind("<<ComboboxSelected>>", on_category_select)

# Pack the widgets into the window
label.pack(pady=10)
category_combobox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
