import string
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

def generate_password():
    length = int(password_length_entry.get())
    characterList = ""
    
    if digits_var.get():
        characterList += string.digits
    if letters_var.get():
        characterList += string.ascii_letters
    if special_chars_var.get():
        characterList += string.punctuation
        
    if not characterList:
        messagebox.showwarning("Warning", "Please select at least one character set.")
        return
    
    password = [random.choice(characterList) for _ in range(length)]
    password_str = ''.join(password)
    
    password_result_label.config(text="Generated Password: " + password_str)

# Create the main GUI window
root = tk.Tk()
root.title("Password Generator")

# Password Length
password_length_label = tk.Label(root, text="Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(root)
password_length_entry.pack()

# Character Sets
digits_var = tk.IntVar()
letters_var = tk.IntVar()
special_chars_var = tk.IntVar()

digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.pack()
letters_check = tk.Checkbutton(root, text="Letters", variable=letters_var)
letters_check.pack()
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Result Label
password_result_label = tk.Label(root, text="")
password_result_label.pack()

# Run the GUI event loop
root.mainloop()
