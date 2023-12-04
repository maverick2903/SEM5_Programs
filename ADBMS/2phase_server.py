import socket
import threading

class TwoPhaseCommitServer:
    def __init__(self):
        self.closed = False
        self.clients = []
        self.decisions = []
        self.lock = threading.Lock()

    def start(self, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", port))
        server_socket.listen()

        print("Server is listening for connections...")

        try:
            while not self.closed:
                client_socket, address = server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
                self.clients.append((client_socket, address, client_thread))
                self.decisions.append(None)
        except Exception as e:
            print(f"Exception occurred: {e}")
        finally:
            server_socket.close()

    def handle_client(self, client_socket):
        try:
            with client_socket:
                client_address = client_socket.getpeername()
                print(f"Accepted connection from {client_address}")

                client_id = len(self.clients) - 1
                client_socket.sendall(f"Welcome! You are client {client_id}\n".encode())

                while True:
                    message = client_socket.recv(1024).decode().strip()
                    print(f"Received from client {client_id}: {message}")

                    if message.upper() == "READY":
                        with self.lock:
                            self.decisions[client_id] = "READY"
                        self.broadcast("VOTE_REQUEST")

                    elif message.upper() == "NOT READY":
                        with self.lock:
                            self.decisions[client_id] = "NOT READY"

                    all_decided = all(decision is not None for decision in self.decisions)
                    if all_decided:
                        if all(decision == "READY" for decision in self.decisions):
                            self.broadcast("GLOBAL_COMMIT")
                            print("Global commit!")
                            self.closed = True
                        else:
                            self.broadcast("GLOBAL_ABORT")
                            print("Global abort!")
                            self.closed = True
                            break

                    # Check for custom messages from the client
                    if message.upper() == "READY":
                        custom_message = client_socket.recv(1024).decode().strip()
                        print(f"Custom message from client {client_id}: {custom_message}")

        except Exception as e:
            print(f"Exception occurred in client handling: {e}")

    def broadcast(self, message):
        with self.lock:
            for client_socket, _, _ in self.clients:
                try:
                    client_socket.sendall(f"{message}\n".encode())
                except:
                    pass

if __name__ == "__main__":
    server = TwoPhaseCommitServer()
    server.start(1111)