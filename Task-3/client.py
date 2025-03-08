import socket
import threading
import tkinter as tk
from tkinter import messagebox

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Server details
host_ip = "127.0.0.1"
port_number = 7500

# Connect to the server
try:
    client_socket.connect((host_ip, port_number))
except Exception as e:
    messagebox.showerror("Connection Error", f"Failed to connect to server: {e}")
    exit()

# GUI setup
window = tk.Tk()
window.title(f"Connected To: {host_ip}:{port_number}")

# Text widget to display messages
txt_messages = tk.Text(window, width=50, state="disabled")
txt_messages.grid(row=0, column=0, padx=10, pady=10)

# Entry widget to type messages
txt_your_message = tk.Entry(window, width=50)
txt_your_message.insert(0, "Type your message...")
txt_your_message.grid(row=1, column=0, padx=10, pady=10)

# Function to send messages
def send_message():
    message = txt_your_message.get().strip()
    if message and message != "Type your message...":
        try:
            client_socket.send(message.encode("utf-8"))
            txt_your_message.delete(0, tk.END)
            update_message_display(f"You: {message}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

# Button to send messages
btn_send_message = tk.Button(window, text="Send", width=20, command=send_message)
btn_send_message.grid(row=2, column=0, padx=10, pady=10)

# Function to update the message display
def update_message_display(message):
    txt_messages.config(state="normal")
    txt_messages.insert(tk.END, f"\n{message}")
    txt_messages.config(state="disabled")
    txt_messages.see(tk.END)  # Scroll to the bottom

# Function to receive messages from the server
def recv_message():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            update_message_display(message)
        except ConnectionResetError:
            update_message_display("Disconnected from the server.")
            break
        except Exception as e:
            update_message_display(f"Error: {e}")
            break

# Start a thread to receive messages
recv_thread = threading.Thread(target=recv_message, daemon=True)
recv_thread.start()

# Run the GUI
window.mainloop()

# Close the socket when the window is closed
client_socket.close()