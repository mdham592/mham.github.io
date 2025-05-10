import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import time

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print_lock = threading.Lock()
FilePath = 'D:\projects\Port_Scanner\\'

#This method parses user input allowing easier user experience.
def parse_ports(ports_input):
    if "," in ports_input:
        PORT = ports_input.split(",")
        print ("Scanning port: " + str(PORT))
        return PORT
    elif "-" in ports_input:
        ports_input.split("-")
        PORT = list(range(int(ports_input.split("-", 1)[0]), int(ports_input.split("-", 1)[1])+1))
        print ("Scanning port: " + str(PORT))
        return PORT
    else:
        PORT = int(ports_input)
        print ("Scanning port: " + str(PORT))
        return [PORT]

#This method runs the scan itself. Creating a TCP Socket. If the user chose to scan an http port, the program will send a get request. Saving the banner/response to a text file.
#For all other ports, it will attempt to grab the banner and print it to the screen.
def scan_ports(host, port):
    response = b""
    try:
        with socket.create_connection((host, port), timeout=7) as sock:
            sock.settimeout(3)
            try:
                if port in [80, 8080]:
                    sock.sendall(b"GET / HTTP/1.1\r\nHost: %b\r\nConnection: close\r\n\r\n" % host.encode())
                    time.sleep(0.5)
                    while True:
                        banner = sock.recv(4096)
                        if not banner:
                            break
                        response += banner
                    banner = response.decode(errors="ignore").strip()
                    with open(FilePath+host+"_webports.txt", 'a') as file:
                        file.write(banner)
                else:
                    banner = sock.recv(1024).decode(errors="ignore").strip()
            except socket.timeout:
                banner = "No banner received (timeout)"
            except Exception as e:
                banner = f"Error grabbing banner: {e}"
            with print_lock:
                if port in [80, 443, 8080, 8000]:
                    print(f"[{port}] Open - Banner saved to: {FilePath}{host}_webports.txt")
                else:
                    print(f"[{port}] Open - Banner: {banner}")

#These exceptions are critical to identify if the port is closed or being filtered based off the error message.
    except ConnectionRefusedError:
        # Committed out for cleanliness
        # Connection was refused -> port is closed
        # with print_lock:
        #     print(f"[{port}] Closed")
        pass
    except socket.timeout:
        with print_lock:
            print(f"[{port}] Filtered (timeout)")
    except Exception as e:
        with print_lock:
            print(f"[{port}] Error: {e}")

#Accepting user's input loop.
while True:
    host = input("Enter target IP address: ").strip()
    port_input = input("Enter ports (e.g. 80,443 or 20-25 or 8080): ").strip()
    ports = parse_ports(port_input)

    print(f"Scanning {len(ports)} ports on {host}...\n")

#Thread pool uses for efficiency.
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_ports, host, port)

