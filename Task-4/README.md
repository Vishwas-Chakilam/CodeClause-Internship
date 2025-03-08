# Mail Application With UI

A Python-based mail application with a modern graphical user interface (GUI) that allows users to send emails with attachments. The application is designed to resemble Gmail's compose box and includes features like a gradient background, a header, and a footer.

---

## Features

- **Modern GUI**: Clean and professional design with a gradient background.
- **Send Emails**: Send emails to one or more recipients.
- **Attachments**: Attach files to your emails.
- **Error Handling**: Proper error handling for network issues, authentication failures, etc.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
- **Tkinter**: Usually comes pre-installed with Python. If not, install it using your package manager.
- **smtplib**: Part of Python's standard library.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vishwas-Chakilam/CodeClause-Internship.git
   cd Task-4
   ```

2. **Install Dependencies**:
   No additional dependencies are required as the application uses Python's standard libraries.

3. **Run the Application**:
   ```bash
   python mail_app.py
   ```

---

## Usage

1. **Enter Your Email Credentials**:
   - **From**: Enter your email address.
   - **App Password**: Enter your app password (if using Gmail, follow [these instructions](#app-password)).

2. **Compose Your Email**:
   - **To**: Enter the recipient's email address(es). Separate multiple addresses with commas.
   - **Subject**: Enter the subject of your email.
   - **Body**: Write the content of your email.

3. **Attach Files (Optional)**:
   - Click the **Browse** button to select a file for attachment.

4. **Send the Email**:
   - Click the **Send** button to send the email.

---

## App Password

If you're using Gmail, you need to generate an **App Password** to authenticate the application. Follow these steps:

1. Go to your [Google Account](https://myaccount.google.com/).
2. Navigate to **Security** > **2-Step Verification** and enable it.
3. Go to **App Passwords** and generate a new password for the app.
4. Use this password in the **App Password** field.

---

## Screenshots

![Mail Application Screenshot](https://i.imgur.com/xyz1234.png)  
*(Replace with an actual screenshot of your application.)*

---

## Code Structure

- **mail_app.py**: The main Python script containing the application logic.
- **README.md**: This file.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Python**: For providing the tools to build this application.
- **Gmail**: For inspiration in the design.

---

## Contact

For questions or feedback, please contact:

- **Vishwas Chakilam**  
  Email: work.vishwas1@gmail.com 
  GitHub: [vishwas-chakilam](https://github.com/vishwas-chakilam)

---

Enjoy using the Mail Application! 🚀
