import socket
import gnupg
from pathlib import Path

server_ip = '192.168.86.35'   # or your server IP
server_port = 7777
filepath = Path("/home/ubuntu/scripts/uploads")
gpg = gnupg.GPG(gnupghome='/home/ubuntu/scripts')


with open(r'/home/ubuntu/scripts/public_key.asc', 'r') as f:
    key_data = f.read()
    import_result = gpg.import_keys(key_data)
    print(f"Imported key(s): {import_result.fingerprints}")


def send_file(file_path: Path):
    if not file_path.exists():
        print(f"❌ File does not exist: {file_path}")
        return

    try:
        with socket.socket() as s:
            s.connect((server_ip, server_port))
            print(f"🔗 Connected to {server_ip}:{server_port}")

            # Send filename first
            s.sendall(file_path.name.encode().ljust(1024))  # Pad to 1024 bytes

            # Send file content
            with file_path.open('rb') as f:
                while chunk := f.read(1024):
                    s.sendall(chunk)

        print(f"✅ File '{file_path.name}' sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send file: {e}")


# . Encrypt a file using the public key
for file in list(filepath.glob('*')):
    if file.is_file():
        output_file = file.with_suffix(file.suffix + '.gpg')
        with open(file, 'rb') as f:
            encrypt_result = gpg.encrypt_file(
                f,
                recipients=import_result.fingerprints,
                output=str(output_file))
        if encrypt_result.ok:
            print("✅ File encrypted successfully.")
            send_file(output_file)
            try:
                file.unlink()
                output_file.unlink()
                print(f"🗑️ Deleted: {file.name} and {output_file.name}")
            except Exception as e:
                print(f"❌ Failed to delete files: {e}")
        else:
            print("❌ Encryption failed:", encrypt_result.status)
