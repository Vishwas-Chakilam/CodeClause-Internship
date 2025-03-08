import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to handle the "Shorten" button click
def on_shorten_click():
    long_url = entry.get().strip()  # Get the URL from the input field
    
    if not long_url:
        messagebox.showwarning("Input Error", "Please enter a URL!")
        return
    
    try:
        # Initialize the pyshorteners object
        shortener = pyshorteners.Shortener()
        
        # Generate the shortened URL
        short_url = shortener.tinyurl.short(long_url)
        
        # Display the shortened URL in the output label
        output_label.config(text=f"Shortened URL: {short_url}", fg="blue", cursor="hand2")
        
        # Enable the "Copy" button and store the shortened URL
        copy_button.config(state=tk.NORMAL)
        global current_short_url
        current_short_url = short_url
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

# Function to handle the "Copy" button click
def on_copy_click():
    if current_short_url:
        # Copy the shortened URL to the clipboard
        root.clipboard_clear()
        root.clipboard_append(current_short_url)
        root.update()  # Required to finalize the clipboard update
        messagebox.showinfo("Copied!", "Shortened URL copied to clipboard!")

# Function to handle clicking the shortened URL
def on_url_click(event):
    if current_short_url:
        # Open the shortened URL in the default web browser
        import webbrowser
        webbrowser.open(current_short_url)

# Create the main GUI window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x350")  # Set window size
root.resizable(False, False)  # Disable resizing

# Add a header label
header_label = tk.Label(root, text="URL Shortener", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Add an input label and entry field
input_label = tk.Label(root, text="Enter Long URL:", font=("Arial", 12))
input_label.pack(pady=5)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

# Add a "Shorten" button
shorten_button = tk.Button(root, text="Shorten URL", font=("Arial", 12), command=on_shorten_click)
shorten_button.pack(pady=10)

# Add an output label to display the shortened URL
output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", cursor="hand2")
output_label.pack(pady=20)

# Bind the click event to the output label
output_label.bind("<Button-1>", on_url_click)

# Add a "Copy" button (initially disabled)
copy_button = tk.Button(root, text="Copy", font=("Arial", 12), state=tk.DISABLED, command=on_copy_click)
copy_button.pack(pady=10)

# Add a footer label
footer_label = tk.Label(root, text="Made by Vishwas Chakilam", font=("Arial", 10), fg="gray")
footer_label.pack(side="bottom", pady=10)

# Variable to store the current shortened URL
current_short_url = ""

# Run the Tkinter event loop
root.mainloop()