import gnupg
from pathlib import Path
import socket
import threading

filepath = Path(r"D:\projects\Secure_transfer\recived_files")
decrypted_dir = filepath / "decyrpted_files"
decrypted_dir.mkdir(exist_ok=True)


gpg = gnupg.GPG(gnupghome='D:\projects\Secure_transfer\gpg_home')

def decrypt_files(file):
    for file in filepath.glob('*'):
        if file.is_file() and file.suffix.lower() in ['.gpg']:
            with open(file, 'rb') as f:
                result = gpg.decrypt_file(f, passphrase='password')
                if result.ok:
                    output_file = decrypted_dir / file.with_suffix('').name
                    with open(output_file, 'wb') as out:
                        out.write(result.data)
                        print(f"✅ Decrypted file saved to: {output_file}")
                else:
                    print(f"❌ Failed to decrypt {file.name}: {result.status}")

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        filename = conn.recv(1024).decode().strip()
        output_file = filepath / filename
        with output_file.open('wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
            print(f"Saved {filename}")
        decrypt_files(output_file)
    except Exception as e:
        print(f"❌ Error handling client {addr}: {e}")
    finally:
        conn.close()
    
def start_server(host='0.0.0.0', port=7777):
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
