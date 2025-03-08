import tkinter as tk
from tkinter import font
import math

# Global memory variable
memory = 0

# Function to update the display
def update_display(value):
    current_text = display.get()
    if current_text == "Error":
        clear_display()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)
    history_label.config(text="")

# Function to calculate the result
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))  # Evaluate the expression
        history_label.config(text=f"{expression} =")
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to handle backspace
def backspace():
    current_text = display.get()
    if current_text == "Error":
        clear_display()
    display.delete(len(current_text) - 1, tk.END)

# Function to toggle dark mode
def toggle_dark_mode():
    if root.cget("bg") == "#f0f0f0":  # Light mode
        root.config(bg="#2e2e2e")
        display.config(bg="#444", fg="white")
        history_label.config(bg="#2e2e2e", fg="#888")
        footer_label.config(bg="#2e2e2e", fg="#888")
        for btn in buttons_list:
            btn.config(bg="#555", fg="white")
    else:  # Dark mode
        root.config(bg="#f0f0f0")
        display.config(bg="#f0f0f0", fg="black")
        history_label.config(bg="#f0f0f0", fg="#888")
        footer_label.config(bg="#f0f0f0", fg="#888")
        for btn in buttons_list:
            if btn.cget("text") in ['/', '*', '-', '+', '^', '√', '!', 'log', 'sin', 'cos', 'tan', '(', ')', '%', 'Mod', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh', 'tanh']:
                btn.config(bg="#ff9500", fg="white")
            elif btn.cget("text") == "=":
                btn.config(bg="#34c759", fg="white")
            elif btn.cget("text") == "C":
                btn.config(bg="#ff3b30", fg="white")
            elif btn.cget("text") == "⌫":
                btn.config(bg="#555", fg="white")
            elif btn.cget("text") == "☀️":
                btn.config(bg="#e0e0e0", fg="black")
            else:
                btn.config(bg="#e0e0e0", fg="black")

# Function to handle scientific operations
def scientific_operation(op):
    try:
        current_text = display.get()
        if op == "√":
            result = math.sqrt(float(current_text))
        elif op == "^":
            display.insert(tk.END, "**")
            return
        elif op == "!":
            result = math.factorial(int(current_text))
        elif op == "π":
            result = math.pi
        elif op == "e":
            result = math.e
        elif op == "log":
            result = math.log10(float(current_text))
        elif op == "sin":
            result = math.sin(math.radians(float(current_text)))
        elif op == "cos":
            result = math.cos(math.radians(float(current_text)))
        elif op == "tan":
            result = math.tan(math.radians(float(current_text)))
        elif op == "sin⁻¹":
            result = math.degrees(math.asin(float(current_text)))
        elif op == "cos⁻¹":
            result = math.degrees(math.acos(float(current_text)))
        elif op == "tan⁻¹":
            result = math.degrees(math.atan(float(current_text)))
        elif op == "sinh":
            result = math.sinh(float(current_text))
        elif op == "cosh":
            result = math.cosh(float(current_text))
        elif op == "tanh":
            result = math.tanh(float(current_text))
        elif op == "Mod":
            result = float(current_text) % 1
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Memory functions
def memory_add():
    global memory
    try:
        memory += float(display.get())
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def memory_subtract():
    global memory
    try:
        memory -= float(display.get())
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def memory_recall():
    display.delete(0, tk.END)
    display.insert(0, str(memory))

def memory_clear():
    global memory
    memory = 0

# Percentage function
def percentage():
    try:
        current_text = display.get()
        result = str(eval(current_text + "/100"))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Modern Scientific Calculator")
root.geometry("450x700")  # Set window size
root.resizable(True, True)  # Make the window resizable
root.config(bg="#f0f0f0")  # Light mode background

# Custom fonts
display_font = font.Font(family="Arial", size=20)
button_font = font.Font(family="Arial", size=14)
footer_font = font.Font(family="Arial", size=10)

# Create the history label
history_label = tk.Label(root, text="", font=display_font, bg="#f0f0f0", fg="#888", anchor="e")
history_label.grid(row=0, column=0, columnspan=6, padx=10, pady=(10, 0), sticky="e")

# Create the display
display = tk.Entry(root, width=20, font=display_font, justify="right", bd=10, relief=tk.FLAT, bg="#f0f0f0")
display.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/', '√', '^',
    '4', '5', '6', '*', '(', ')',
    '1', '2', '3', '-', '!', '%',
    '0', '.', '⌫', '+', 'Mod', '=',
    'C', 'π', 'e', 'log', 'sin', 'cos',
    'tan', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh',
    'tanh', 'M+', 'M-', 'MR', 'MC', '☀️'
]

# Button colors
button_bg = "#e0e0e0"  # Light gray
operator_bg = "#ff9500"  # Orange
equal_bg = "#34c759"  # Green
clear_bg = "#ff3b30"  # Red
backspace_bg = "#555"  # Dark gray

# Add buttons to the window
buttons_list = []
row, col = 2, 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=equal_bg, fg="white", relief=tk.RAISED, bd=3, command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=clear_bg, fg="white", relief=tk.RAISED, bd=3, command=clear_display)
    elif button == "⌫":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=backspace_bg, fg="white", relief=tk.RAISED, bd=3, command=backspace)
    elif button == "☀️":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=button_bg, relief=tk.RAISED, bd=3, command=toggle_dark_mode)
    elif button in ['/', '*', '-', '+', '^', '√', '!', 'log', 'sin', 'cos', 'tan', '(', ')', '%', 'Mod', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh', 'cosh', 'tanh']:
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=operator_bg, fg="white", relief=tk.RAISED, bd=3, command=lambda b=button: scientific_operation(b))
    elif button == "M+":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=operator_bg, fg="white", relief=tk.RAISED, bd=3, command=memory_add)
    elif button == "M-":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=operator_bg, fg="white", relief=tk.RAISED, bd=3, command=memory_subtract)
    elif button == "MR":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=operator_bg, fg="white", relief=tk.RAISED, bd=3, command=memory_recall)
    elif button == "MC":
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=operator_bg, fg="white", relief=tk.RAISED, bd=3, command=memory_clear)
    else:
        btn = tk.Button(root, text=button, width=5, font=button_font, bg=button_bg, relief=tk.RAISED, bd=3, command=lambda b=button: update_display(b))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons_list.append(btn)
    col += 1
    if col > 5:
        col = 0
        row += 1

# Footer label
footer_label = tk.Label(root, text="Made by Vishwas Chakilam", font=footer_font, bg="#f0f0f0", fg="#888")
footer_label.grid(row=row, column=0, columnspan=6, pady=(10, 0))

# Configure grid weights to make buttons expand
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(8):
    root.grid_rowconfigure(i, weight=1)

# Keyboard support
def key_press(event):
    key = event.char
    if key in '0123456789./*-+':
        update_display(key)
    elif key == '\r':  # Enter key
        calculate()
    elif key == '\x08':  # Backspace key
        backspace()

root.bind("<Key>", key_press)

# Run the application
root.mainloop()