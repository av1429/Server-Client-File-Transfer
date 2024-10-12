import socket
import os

class TCPClient:
    def __init__(self, dir_name, host, port):
        self.dir_name = dir_name
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.settimeout(10)

    def run(self):
        try:
            # Greeting message
            print(self.client_socket.recv(1024).decode())

            # Receive file list from the server
            file_count = int(self.client_socket.recv(1024).decode())
            files = [self.client_socket.recv(1024).decode() for _ in range(file_count)]
            print(f"Files available on server: {files}")

            action = input("Type 'upload' or 'download': ").lower()
            filename = input("Enter the file name: ")

            if action == 'download':
                self.client_socket.sendall(f"*{filename}*".encode())
                response = self.client_socket.recv(1024).decode()
                if response == "Success":
                    self.receive_file(filename)
                else:
                    print(f"File '{filename}' not found on server.")
            elif action == 'upload':
                filepath = os.path.join(self.dir_name, filename)
                if os.path.exists(filepath):
                    self.client_socket.sendall(filename.encode())
                    self.send_file(filepath)
                else:
                    print(f"File '{filename}' not found locally.")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            self.client_socket.close()

    def send_file(self, filepath):
        with open(filepath, "rb") as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.client_socket.sendall(data)
        print(f"File '{filepath}' uploaded successfully.")

    def receive_file(self, filename):
        filepath = os.path.join(self.dir_name, filename)
        with open(filepath, "wb") as file:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"File '{filename}' downloaded successfully.")
        self.display_file_content(filepath)

    def display_file_content(self, filepath):
        print("\nDownloaded File Content:")
        with open(filepath, "r") as file:
            print(file.read())

if __name__ == "__main__":
    dir_name = input("Enter the directory path: ")
    host = input("Enter the server address (default 'localhost'): ") or 'localhost'
    port = int(input("Enter the port number (default 3333): ") or 3333)

    if not os.path.exists(dir_name):
        print("Directory does not exist.")
    else:
        client = TCPClient(dir_name, host, port)
        client.run()
