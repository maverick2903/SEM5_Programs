import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

HOST = socket.gethostname()		# Host IP
PORT = 12345			        # specified port to connect

print ("Target IP:", HOST)
print ("Target Port:", PORT)

while True:   
    msg = input("Enter a message: ")
    client_socket.sendto(bytes(msg,'utf-8'),(HOST,PORT))		# Sending message to server
    if msg == "close":
        client_socket.close
        break    
