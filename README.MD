# File Encryptor and Decryptor

This project provides a simple yet powerful tool for encrypting and decrypting files using AES encryption in CTR mode. It includes a client-server architecture that allows for secure file operations over a network.

## Features

- **AES Encryption**: Utilizes the AES algorithm in CTR mode for secure file encryption.
- **Parallel Processing**: Supports simultaneous encryption and decryption of multiple files to enhance performance.
- **Cross-Platform Support**: Works on both Windows and Linux, automatically detecting available partitions and directories.
- **Persistent Client**: The client script runs in the background, maintaining a connection to the server and listening for decryption commands.
- **Customizable Key**: You can set a custom encryption key, making it easy to manage security according to your needs.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `Cryptodome` (Install via `pip install pycryptodome`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2. Install the required libraries:
    ```bash
    pip install pycryptodome

3. Usage
- **Start the Server**: Run the server script to listen for incoming connections from clients.

    ```bash
    python server.py

4. Start the Client:
- **Run the client script**, which will automatically encrypt files in specified directories and listen for decryption commands.

    ```bash
    python client.py

- **Decrypting Files**: To decrypt files, send the decryption key to the client. The client will process the decryption in the background.


## Configuration
Modify the key in the FileEncryptor class if you wish to use a different encryption key. The default key is set to "aaaaaaaa".
## Security Considerations
Ensure that your encryption key is kept secret. Sharing the key can lead to unauthorized access to your files.
Be aware of potential vulnerabilities in network communications. Use a secure network environment when running the server and client.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
PyCryptodome for the cryptography library.
GitHub for providing a platform to share and collaborate on code.
## Contact
For any questions or feedback, feel free to contact me at ibrahemabokila@gmail.com.