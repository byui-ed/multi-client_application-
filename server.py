import datetime
import socket
import threading
import time

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

# Server State Tracking
START_TIME = time.time()
request_count = 0
count_lock = threading.Lock()  # Ensures thread-safe counter increments


def handle_client(conn, addr):
    """Handles communication with a single connected client."""
    global request_count
    print(f"[+] New Connection Established: {addr}")

    try:
        while True:
            # Receive data from client (buffer size 1024 bytes)
            data = conn.recv(1024)
            if not data:
                break  # Client disconnected

            request = data.decode('utf-8').strip()
            print(f"[{addr}] Received: {request}")

            # Thread-safe increment of total requests processed
            with count_lock:
                request_count += 1

            # Command Processing Logic
            if request.upper() == 'TIME':
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                response = f"SERVER TIME: {now}"

            elif request.upper().startswith('ECHO '):
                # Extract message after 'ECHO '
                user_msg = request[5:].upper()
                char_count = len(request[5:])
                response = f"ECHO RESPONSE: {user_msg} | [Metadata: Length={char_count} chars]"

            elif request.upper() == 'STATS':
                uptime_seconds = int(time.time() - START_TIME)
                with count_lock:
                    total_reqs = request_count
                response = f"SERVER STATS: Uptime={uptime_seconds}s | Processed Requests={total_reqs}"

            else:
                response = "ERROR: Unknown Command. Supported commands: TIME, ECHO <msg>, STATS"

            # Send formatted response back to client
            conn.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        print(f"[-] Connection forcibly closed by {addr}")
    finally:
        conn.close()
        print(f"[-] Connection Closed: {addr}")


def start_server():
    """Initializes and runs the TCP server socket."""
    # Create TCP Socket (IPv4, TCP/SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Re-use socket address to prevent 'Address already in use' errors
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[*] Server listening on {HOST}:{PORT}...")

        while True:
            # Accept incoming connection
            conn, addr = server_socket.accept()
            # Spawn a new thread to handle the client concurrently
            client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            client_thread.start()


if __name__ == "__main__":
    start_server()