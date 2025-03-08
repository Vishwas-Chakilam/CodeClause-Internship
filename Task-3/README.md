# Real Time Chat Application

A simple real-time chat application built using Python, `socket` for networking, and `tkinter` for the GUI. The application allows multiple clients to connect to a server and exchange messages in real-time.

---

## Features

- **Real-Time Messaging**: Clients can send and receive messages instantly.
- **Multiple Clients**: The server supports multiple clients simultaneously.
- **Simple GUI**: Built using `tkinter` for ease of use.
- **Error Handling**: Handles connection errors and disconnections gracefully.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: The application is written in Python.
- **No additional libraries**: The application uses only built-in Python modules (`socket`, `threading`, and `tkinter`).

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Vishwas-Chakilam/CodeClause-Internship.git
cd Task-3
```

### 2. Start the Server

Run the `Server.py` script to start the chat server:

```bash
python Server.py
```

The server will start listening for incoming connections on `127.0.0.1:7500`.

### 3. Start the Clients

Run the `Client.py` script to start a client:

```bash
python Client.py
```

You can run multiple instances of `Client.py` to simulate multiple users.

---

## Usage

### Server

- The server listens for incoming client connections.
- It broadcasts messages from one client to all other connected clients.
- If a client disconnects, the server removes them from the list of active clients.

### Client

- The client connects to the server and provides a simple GUI for sending and receiving messages.
- Type your message in the input box and click **Send** to broadcast it to all connected clients.
- Received messages are displayed in the text area.

---

## Project Structure

```
Task-3/
├── Client.py            # Client-side script
├── Server.py            # Server-side script
├── README.md            # Project documentation
```


## Troubleshooting

### Common Issues

1. **Connection Errors**:
   - Ensure the server is running before starting the client.
   - Check that the server IP and port are correct.

2. **Port Already in Use**:
   - Ensure no other application is using port `7500`.
   - You can change the port in both `Server.py` and `Client.py`.

3. **Client Disconnects Unexpectedly**:
   - Check the server logs for errors.
   - Ensure the client and server are on the same network.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with Python's `socket` and `tkinter` libraries.
- Inspired by simple chat applications for learning purposes.

---

Enjoy chatting! 🚀
