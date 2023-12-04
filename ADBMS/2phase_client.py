import socket

class TwoPhaseCommitClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to the server.")
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            exit(1)

    def start(self):
        self.connect_to_server()

        try:
            welcome_message = self.client_socket.recv(1024).decode()
            print(welcome_message)

            while True:
                decision = input("Enter 'READY' or 'NOT READY': ")
                self.client_socket.sendall(decision.encode())

                response = self.client_socket.recv(1024).decode().strip()
                print(f"Received from server: {response}")

                if response.upper() == "GLOBAL_COMMIT":
                    print("Transaction committed globally!")
                 
                elif response.upper() == "GLOBAL_ABORT":
                    print("Transaction aborted globally!")
                    break

                # Allow the client to send a custom message
                if decision.upper() == "READY":
                    message = input("Enter your message to send to the server: ")
                    self.client_socket.sendall(message.encode())

        except Exception as e:
            print(f"Error during communication: {e}")
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    client = TwoPhaseCommitClient("localhost", 1111)
    client.start()