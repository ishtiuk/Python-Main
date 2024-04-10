from pydoc import cli
import socket


client = socket.socket()

client.connect(("192.168.0.103", 9999))

data = client.recv(1024).decode()
print(f"server: {data}\nconnected to server...")

client.send(bytes("hey, i'm windows", 'utf-8'))
print("data sent")

client.close()
