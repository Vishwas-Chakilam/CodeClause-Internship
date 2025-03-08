import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Compose Mail")
        master.geometry("600x550")  # Increased height to ensure all widgets fit
        master.resizable(False, False)

        # Gradient Background
        self.canvas = tk.Canvas(master, width=600, height=550)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient("#ffffff", "#e8f0fe")  # Light blue to white gradient

        # Header
        self.header_frame = ttk.Frame(self.canvas, style="Header.TFrame")
        self.header_frame.place(relx=0, rely=0, relwidth=1, height=50)
        self.header_label = ttk.Label(self.header_frame, text="Compose Mail", style="Header.TLabel")
        self.header_label.pack(side="left", padx=10)

        # Main Content Frame
        self.main_frame = ttk.Frame(self.canvas, style="Main.TFrame")
        self.main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)  # Adjusted relheight

        # From field
        self.from_label = ttk.Label(self.main_frame, text="From:", style="Main.TLabel")
        self.from_label.grid(row=0, column=0, sticky="w", pady=5)
        self.from_entry = ttk.Entry(self.main_frame, width=50, style="Main.TEntry")
        self.from_entry.grid(row=0, column=1, sticky="w", pady=5)

        # App Password field
        self.pass_label = ttk.Label(self.main_frame, text="App Password:", style="Main.TLabel")
        self.pass_label.grid(row=1, column=0, sticky="w", pady=5)
        self.pass_entry = ttk.Entry(self.main_frame, width=50, show="*", style="Main.TEntry")
        self.pass_entry.grid(row=1, column=1, sticky="w", pady=5)

        # To field
        self.to_label = ttk.Label(self.main_frame, text="To (comma separated):", style="Main.TLabel")
        self.to_label.grid(row=2, column=0, sticky="w", pady=5)
        self.to_entry = ttk.Entry(self.main_frame, width=50, style="Main.TEntry")
        self.to_entry.grid(row=2, column=1, sticky="w", pady=5)

        # Subject field
        self.subject_label = ttk.Label(self.main_frame, text="Subject:", style="Main.TLabel")
        self.subject_label.grid(row=3, column=0, sticky="w", pady=5)
        self.subject_entry = ttk.Entry(self.main_frame, width=50, style="Main.TEntry")
        self.subject_entry.grid(row=3, column=1, sticky="w", pady=5)

        # Body field
        self.body_label = ttk.Label(self.main_frame, text="Body:", style="Main.TLabel")
        self.body_label.grid(row=4, column=0, sticky="nw", pady=5)
        self.body_text = scrolledtext.ScrolledText(self.main_frame, height=10, width=50, font=("Helvetica", 10))
        self.body_text.grid(row=4, column=1, sticky="w", pady=5)

        # Attachment field
        self.attachment_label = ttk.Label(self.main_frame, text="Attachment:", style="Main.TLabel")
        self.attachment_label.grid(row=5, column=0, sticky="w", pady=5)
        self.attachment_entry = ttk.Entry(self.main_frame, width=40, style="Main.TEntry")
        self.attachment_entry.grid(row=5, column=1, sticky="w", pady=5)
        self.attachment_button = ttk.Button(self.main_frame, text="Browse", command=self.browse_file, width=10, style="Main.TButton")
        self.attachment_button.grid(row=5, column=2, sticky="w", padx=5)

        # Send button
        self.send_button = ttk.Button(self.main_frame, text="Send", command=self.send_mail, width=20, style="Send.TButton")
        self.send_button.grid(row=6, column=1, sticky="e", pady=20)

        # Footer
        self.footer_frame = ttk.Frame(self.canvas, style="Footer.TFrame")
        self.footer_frame.place(relx=0, rely=0.95, relwidth=1, height=30)
        self.footer_label = ttk.Label(self.footer_frame, text="Made by Vishwas Chakilam", style="Footer.TLabel")
        self.footer_label.pack(side="right", padx=10)

        # Configure styles
        self.configure_styles()

    def draw_gradient(self, color1, color2):
        """Draw a gradient background on the canvas."""
        for i in range(550):  # Adjusted for new window height
            gradient = self.interpolate_color(color1, color2, i / 550)
            self.canvas.create_line(0, i, 600, i, fill=gradient, width=1)

    def interpolate_color(self, color1, color2, ratio):
        """Interpolate between two colors."""
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        return self.rgb_to_hex(r, g, b)

    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB."""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, r, g, b):
        """Convert RGB to hex color."""
        return f"#{r:02x}{g:02x}{b:02x}"

    def configure_styles(self):
        """Configure ttk styles for the application."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Header
        self.style.configure("Header.TFrame", background="#d3e3fd")
        self.style.configure("Header.TLabel", background="#d3e3fd", font=("Helvetica", 14, "bold"), foreground="#1a73e8")

        # Main Content
        self.style.configure("Main.TFrame", background="#ffffff")
        self.style.configure("Main.TLabel", background="#ffffff", font=("Helvetica", 10), foreground="#202124")
        self.style.configure("Main.TEntry", font=("Helvetica", 10), padding=5)
        self.style.configure("Main.TButton", font=("Helvetica", 10), background="#1a73e8", foreground="white", padding=5)

        # Send Button
        self.style.configure("Send.TButton", font=("Helvetica", 10, "bold"), background="#1a73e8", foreground="white", padding=10)
        self.style.map("Send.TButton", background=[("active", "#1557b5")])

        # Footer
        self.style.configure("Footer.TFrame", background="#f1f3f4")
        self.style.configure("Footer.TLabel", background="#f1f3f4", font=("Helvetica", 8), foreground="#5f6368")

    def browse_file(self):
        """Open a file dialog to select a file for attachment."""
        filename = filedialog.askopenfilename()
        if filename:
            self.attachment_entry.delete(0, tk.END)
            self.attachment_entry.insert(0, filename)

    def send_mail(self):
        try:
            # Get the email data from the UI
            from_address = self.from_entry.get()
            app_password = self.pass_entry.get()
            to_addresses = self.to_entry.get().split(',')
            subject = self.subject_entry.get()
            body = self.body_text.get("1.0", tk.END)
            attachment_path = self.attachment_entry.get()

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = ', '.join(to_addresses)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Attach file if provided
            if attachment_path:
                attachment = open(attachment_path, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(attachment_path)}")
                msg.attach(part)
                attachment.close()

            # Connect to the SMTP server
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_address, app_password)

            # Send the email
            server.sendmail(from_address, to_addresses, msg.as_string())

            # Server clean up
            server.quit()
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")

# Run the application
root = tk.Tk()
mail_app = MailApp(root)
root.mainloop()