# Real-Time Encrypted Chat Application

This is a real-time chat application built using **Django Channels** and **WebSockets**, with message encryption for secure communication. The app allows users to exchange encrypted messages in real-time without storing them in a database.

---

## Features

- **Real-Time Messaging**: Built with Django Channels and WebSockets for instant communication.
- **End-to-End Encryption**: Messages are encrypted on the sender side and decrypted on the receiver side.
- **No Message Storage**: Messages are not stored in the database for privacy.
- **Redis Backend**: Redis is used as a channel layer for managing real-time events.
- **Simple and Lightweight**: Designed for easy use and modification.

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django Channels 4.0+
- Redis Server (5.0+)
- Node.js (for frontend dependencies like `crypto-js`)

---

## Installation

### 1. Clone the Repository
```
git clone https://github.com/yourusername/chat-app.git
cd chat-app
```

## Installation

### 1. Clone the Repository

```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

```

### Install dependencies:
```
pip install -r requirements.txt
```
### Set up Redis:
Ensure Redis is installed and running. If using WSL or Docker, make sure Redis is configured correctly.

### Start the ASGI server:
```
daphne -b 0.0.0.0 -p 8000 chat_app.asgi:application
```

## Usage
- Open your browser and navigate to the chat application:

    - Example: http://127.0.0.1:8000/chat/<room_name>/
    - Replace <room_name> with the name of the chat room you want to join or create.

## License
This project is licensed under the CC BY-NC 4.0 License. You are free to use, modify, and share this code for non-commercial purposes only. Commercial use is prohibited.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request. For major changes, please open an issue first to discuss your ideas.

## Acknowledgments
- **Django Channels**: For enabling WebSocket support in Django.
- **Redis**: For managing real-time message broadcasting.

## Contact
For any questions, feedback, or issues, feel free to reach out:

- Email: atinder.singh67@gmail.com
GitHub: atindersingh67

