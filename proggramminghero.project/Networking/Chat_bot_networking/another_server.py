import socket
import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.103', 12000))
print("Socket Created")

s.listen(1)
print("Waiting for connection...")

while True:
    connection_obj, addr_ip = s.accept()
    exeTime = datetime.datetime.now().strftime("%I:%M:%S %p |%d-%m-%Y %a|")
    print(f"Connected with {addr_ip} at {exeTime}")

    client_data = connection_obj.recv(1024).decode()
    print(client_data)

    connection_obj.close()


