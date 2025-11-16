import tkinter as tk
from tkinter import messagebox
import random
import string

def kuldeepPasswordMekar():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "  enter a valid number for length!")
        return

    length = int(length)

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "   Bro sahi se kar le!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    outputentry.delete(0, tk.END)
    outputentry.insert(0, password)

def  copyHereBro():
    password = outputentry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copy  ho gaya!")
    else:
        messagebox.showerror("Error", "No password to copy!")

# over viwe
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.config(bg="#222")

# Heading
title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="#222", fg="white")
title.pack(pady=10)

# size
tk.Label(root, text="Enter Password Length:", bg="#222", fg="white").pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Options
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters (A-Z)", variable=letters_var, bg="#222", fg="white", selectcolor="#444").pack()
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var, bg="#222", fg="white", selectcolor="#444").pack()
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var, bg="#222", fg="white", selectcolor="#444").pack()

# Generator karne ke liye Button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=kuldeepPasswordMekar, bg="#00A86B", fg="white")
generate_btn.pack(pady=10)

# Output finlly
tk.Label(root, text="Generated Password:", bg="#222", fg="white").pack()
outputentry = tk.Entry(root, width=30, font=("Arial", 12))
outputentry.pack(pady=5)

# Copy karne ke liye Button
copybutton = tk.Button(root, text="Copy Password", font=("Arial", 12), command= copyHereBro, bg="#1E90FF", fg="white")
copybutton.pack(pady=10)

root.mainloop()
