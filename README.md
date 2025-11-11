# 🖥️ Server–Client File Transfer System (Python Sockets)

## 📄 Overview
This project implements a **TCP-based file transfer system** using **Python sockets**, enabling reliable communication between a **server** and multiple **clients**.  
It supports both **file upload** and **file download** functionalities with threaded server handling for concurrent connections.

---

## ⚙️ Features
- 🔄 **Two-way file transfer:** Clients can upload files to or download files from the server.  
- 🧵 **Multi-threaded Server:** Handles multiple client connections simultaneously.  
- 📁 **Directory Sync:** Lists all available files on the server before transfer.  
- ⚡ **Error Handling:** Manages missing files and disconnections gracefully.  
- 💬 **Real-time Feedback:** Displays connection status, transfer progress, and completion messages.

---

## 🧩 Files Included

| File | Description |
|------|--------------|
| `server.py` | Multi-threaded TCP server for handling client connections and file transfers. |
| `client.py` | Client-side script to upload or download files from the server. |
| `server.txt` | Sample text file located on the server (for testing downloads). |
| `client.txt` | Sample text file located on the client (for testing uploads). |

---

## 🚀 How to Run

### 🖥️ Step 1 — Start the Server
```bash```
- python server.py
- Enter a valid directory path (where files are stored on the server).
- Default port: 3333 

### 💻 Step 2 — Start the Client
```bash```
- python client.py

---

### **🧰 Tools & Environment**

- **Language:** Python 3.x
- **Libraries:** socket, threading, os
- **Platform:** Works on Windows, Linux, or macOS
- **Network:** Localhost or LAN

---

### **⚡ Future Enhancements**

- Add file integrity verification (MD5 checksum).
- Include progress bar for transfer visualization.
- Build GUI interface for better usability.

---

### **👨‍💻 Author**

**Aravinthvasan S**
B.Tech — Electronics & Communication Engineering
SASTRA Deemed University
🔗 [GitHub Profile](https://github.com/av1429)
---

### **🪪 License**

This project is licensed under the MIT License — free to use, modify, and share with attribution.
