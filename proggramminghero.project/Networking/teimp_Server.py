import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("192.168.0.103", 9999))

server.listen()
print("listening....")

while True:
    addr, ip = server.accept()
    
    addr.send(bytes("hey, client.! Welcome to server...", 'utf-8'))

    data_client = addr.recv(1024).decode()
    print(f"client: {ip} sms: {data_client}")

