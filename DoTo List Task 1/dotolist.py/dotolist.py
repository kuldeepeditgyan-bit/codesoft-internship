import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

FILE = "tasks.json"

# yaha se task list file me load hogi
def loadTasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# yaha se task list file me save hogi
def saveTask():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# new task add karne ka function
def addNewTask():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    
    tasks.append({"task": task, "status": "Pending"})
    UpdateTable()
    entry.delete(0, tk.END)
    saveTask()

# ye wala function task delete karega
def taskDelete():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete!")
        return
    
    index = int(selected[0])
    tasks.pop(index)
    UpdateTable()
    saveTask()

# mark karne ke liye use hota hai
def MarkIsDone():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select a task to mark done!")
        return
    
    index = int(selected[0])
    tasks[index]["status"] = "Completed"
    UpdateTable()
    saveTask()

# table update karega
def UpdateTable():
    for row in tree.get_children():
        tree.delete(row)

    for i, t in enumerate(tasks):
        tree.insert("", tk.END, iid=i, values=(t["task"], t["status"]))

# GUI window start
app = tk.Tk()
app.title("Advanced To-Do List App - Kuldeep Version")
app.geometry("600x400")
app.config(bg="#222")

title = tk.Label(app, text="My To-Do List", font=("Arial", 18, "bold"), bg="#222", fg="white")
title.pack(pady=10)

frame = tk.Frame(app, bg="#222")
frame.pack(pady=10)

entry = tk.Entry(frame, width=40, font=("Arial", 12))
entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(frame, text="Add Task", font=("Arial", 12), command=addNewTask, bg="#00d26a", fg="white")
add_btn.grid(row=0, column=1)

cols = ("Task", "Status")
tree = ttk.Treeview(app, columns=cols, show="headings", height=10)
tree.heading("Task", text="Task")
tree.heading("Status", text="Status")
tree.pack(pady=20)

btn_frame = tk.Frame(app, bg="#222")
btn_frame.pack()

mark_btn = tk.Button(btn_frame, text="Mark Completed", command=MarkIsDone, font=("Arial", 12), bg="#ff8608", fg="white")
mark_btn.grid(row=0, column=0, padx=10)

del_btn = tk.Button(btn_frame, text="Delete Task", command=taskDelete, font=("Arial", 12), bg="#f10000", fg="white")
del_btn.grid(row=0, column=1, padx=10)

tasks = loadTasks()
UpdateTable()

app.mainloop()
