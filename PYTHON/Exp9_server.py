import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()  # The server's IP address
PORT = 12345       # Port to listen on


server_socket.bind((HOST, PORT))

print(f"Server is listening on {HOST}:{PORT}")

# Accept incoming connections
while True:
	print("Waiting for client...")
	data,addr = server_socket.recvfrom(1024)	        #receive data from client
	if data.decode('utf-8') == "close":
		print("Closing server...")
		server_socket.close()
		break	
	print ("Received Messages:",data.decode('utf-8')," from",addr)
