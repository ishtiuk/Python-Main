import socket

client = socket.socket()

usr_nm = input("Enter usrname: ")

client.connect(('127.0.0.1', 9997))
print("Connected with server...")

receved_data = client.recv(1024)
print(receved_data.decode())

print("Data Received")

client.send(bytes(usr_nm, 'utf-8'))
print("Sending Data...")
print("done")


client.close()