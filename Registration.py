import tkinter as tk
from tkinter import messagebox
import re

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    phone = entry_phone.get()
    password = entry_password.get()
    confirmpassword = entry_confirmpassword.get()

    if len(phone)<10:
        messagebox.showwarning("Warning","Phone number must be 10 digits")

    if confirmpassword!=password:
        messagebox.showwarning("Warning","Passwords do not match")
        return

    # Simple validation
    if not username or not password or not email or not phone or not confirmpassword:
        messagebox.showwarning("Warning", "All fields are required!")
        return
    
    # Regex for validating email ending with .com
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com)$'
    if not re.match(email_regex, email):
        messagebox.showwarning("Warning", "Invalid email format. Please enter a valid .com email address.")
        return

    # Here you can add code to handle the registration logic (e.g., saving to a file or database)
    # For now, we'll just show a success message
    messagebox.showinfo("Success", "Registration Successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Page")

# Create and place the widgets
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=10)
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=3, column=0, padx=10, pady=10)
entry_password = tk.Entry(root,show="*")
entry_password.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Confirm Password:").grid(row=4, column=0, padx=10, pady=10)
entry_confirmpassword = tk.Entry(root,show="*")
entry_confirmpassword.grid(row=4, column=1, padx=10, pady=10)

btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=5, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()