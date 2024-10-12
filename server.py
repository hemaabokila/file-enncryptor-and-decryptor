import socket
import time

class Server:
    def __init__(self, host="0.0.0.0", port=2000):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        command = data.decode("ascii").strip()
                        if command == "exit":
                            conn.send(b"Server shutting down.")
                            break
                        if command == "send_key":
                            conn.send(b"aaaaaaaa")  
                        time.sleep(1) 

def main():
    server = Server()
    server.start()
if __name__ == "__main__":
    main()
