from ctypes import DEFAULT_MODE
import socket

client = socket.socket()

client.connect(('192.168.0.103', 12000))

usr = input("Enter name: ")

while True:
    data = client.recv(1024).decode()
    print(data)

    sms = input(f"{usr}: ")
    print(sms)
    client.send(bytes(f"{usr}: {sms}", 'utf-8'))

    # client.close()