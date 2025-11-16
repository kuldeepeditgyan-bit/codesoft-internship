import tkinter as tk

root = tk.Tk()
root.title("kuldeep ka Calculator")
root.geometry("320x420")
root.config(bg="#0d0d0d")

display = tk.Entry(root, font=("Consolas", 20), bg="#1a1a1a", fg="#00ff00", bd=5, relief=tk.FLAT, justify="right")
display.pack(fill="both", padx=10, pady=15)

def press(val):
    display.insert(tk.END, val)

def clear():
    display.delete(0, tk.END)

def equal():
    try:
        ans = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, ans)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

mystly = {
    "font": ("Consolas", 18),
    "bg": "#1a1a1a",
    "fg": "#00ff00",
    "width": 4,
    "height": 1,
    "relief": tk.FLAT
}

frame = tk.Frame(root, bg="#0d0d0d")
frame.pack()

button = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in button:
    btn_row = tk.Frame(frame, bg="#0d0d0d")
    btn_row.pack()
    for btn in row:
        if btn == "C":
            tk.Button(btn_row, text=btn, command=clear, **mystly).pack(side="left", padx=5, pady=5)
        elif btn == "=":
            tk.Button(btn_row, text=btn, command=equal, **mystly).pack(side="left", padx=5, pady=5)
        else:
            tk.Button(btn_row, text=btn, command=lambda x=btn: press(x), **mystly).pack(side="left", padx=5, pady=5)

root.mainloop()
