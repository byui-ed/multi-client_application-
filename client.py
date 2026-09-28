import socket

# Target Server Configuration
HOST = '127.0.0.1'
PORT = 65432


def start_client():
    """Connects to the TCP server and handles user input/responses."""
    print("=========================================")
    print("   Multi-Client TCP Networking Client    ")
    print("=========================================")
    print("Available Commands:")
    print("  1. TIME        -> Get server current timestamp")
    print("  2. ECHO <msg>  -> Echo back text in uppercase with metadata")
    print("  3. STATS       -> Get server uptime & processed count")
    print("  Type 'EXIT' or 'QUIT' to close client.")
    print("=========================================\n")

    try:
        # Create TCP socket and connect to server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print(f"[+] Connected to Server at {HOST}:{PORT}\n")

            while True:
                user_input = input("Client > ").strip()

                if not user_input:
                    continue

                if user_input.upper() in ['EXIT', 'QUIT']:
                    print("[*] Disconnecting from server...")
                    break

                # Send command payload over TCP socket
                client_socket.sendall(user_input.encode('utf-8'))

                # Receive server response
                response = client_socket.recv(1024).decode('utf-8')
                print(f"Server Response > {response}\n")

    except ConnectionRefusedError:
        print("[!] Error: Could not connect to server. Make sure server.py is running.")
    except Exception as e:
        print(f"[!] Network Error: {e}")


if __name__ == "__main__":
    start_client()