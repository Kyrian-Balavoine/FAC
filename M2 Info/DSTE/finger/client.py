import socket
import sys

if len(sys.argv) != 3:
    print("ERROR : not enough argument")
    sys.exit(1)

user = sys.argv[1]
machine = sys.argv[2]
port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((machine, port))
client.sendall((user + "\n").encode('utf-8'))
reponse = client.recv(1024).decode('utf-8')

print(reponse.strip())

client.close()
