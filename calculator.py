import tkinter as tk
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create window
root = tk.Tk()
root.title("Calculator")

# Entry box
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Add buttons to window
for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", width=5, height=2)
        button.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)
    frame.pack()

# Start the app
root.mainloop()
