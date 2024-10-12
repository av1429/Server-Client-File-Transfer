import socket
import threading
import os

# Threaded server for handling multiple clients
class ThreadedServer(threading.Thread):
    def __init__(self, connection_socket, client_id, dir_name):
        threading.Thread.__init__(self)
        self.connection_socket = connection_socket
        self.client_id = client_id
        self.dir_name = dir_name

    def run(self):
        try:
            connection = self.connection_socket
            print(f"Client with ID {self.client_id} connected...")
            
            # Send greeting message
            connection.sendall(b"Server says Hi!")
            
            # Get list of files from the directory and send to the client
            files = os.listdir(self.dir_name)
            connection.sendall(str(len(files)).encode())
            for filename in files:
                connection.sendall(filename.encode())

            # Receive file name from the client
            name = connection.recv(1024).decode()
            if name.startswith("*"):
                filename = name.strip("*")
                filepath = os.path.join(self.dir_name, filename)
                if os.path.exists(filepath):
                    connection.sendall(b"Success")
                    print(f"Starting download of {filename}")
                    with open(filepath, "rb") as f:
                        self.send_file(f, connection)
                    print("File download complete")
                else:
                    connection.sendall(b"FileNotFound")
            else:
                filepath = os.path.join(self.dir_name, name)
                print(f"Starting upload of {name}")
                self.receive_file(filepath, connection)
                print(f"File {name} uploaded successfully")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            connection.close()

    def send_file(self, file, connection):
        while True:
            data = file.read(1024)
            if not data:
                break
            connection.sendall(data)

    def receive_file(self, filepath, connection):
        with open(filepath, "wb") as file:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file.write(data)

def main():
    dir_name = input("Enter the directory path: ")
    port = int(input("Enter the port number (default 3333): ") or 3333)

    # Check if directory exists
    if not os.path.exists(dir_name):
        print("Directory does not exist")
        return

    print("Server started...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enable address reuse to prevent the "address in use" error
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind(("", port))
    server_socket.listen(5)

    client_id = 1
    while True:
        print("Waiting for connections...")
        connection_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        server_thread = ThreadedServer(connection_socket, client_id, dir_name)
        client_id += 1
        server_thread.start()

if __name__ == "__main__":
    main()
