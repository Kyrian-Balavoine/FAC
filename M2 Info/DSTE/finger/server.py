import socket

users = {
    "Alison" : "Alice",
    "Bobinson" : "Bob",
    "Charlson" : "charles"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 8888))
server.listen(5)

while True:
    client, adresse = server.accept()
    data = client.recv(1024).decode('utf-8').strip()
    first_name = users.get(data, "Unknown user")
    client.sendall((first_name + "\n").encode('utf-8'))
    client.close()