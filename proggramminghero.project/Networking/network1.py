import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
                      #(socket_family, socket_type, protoc (it can remain by-defalut 0)), and we can also skip the protocol. 
# server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, protoc)    
# server_unix = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, protoc)                   

server.bind(('192.168.0.103', 9999))    # it binds the server socket with an ip main machine ip address and a free port.
print('Waiting for connection...')

server.listen(1)     # .listen() method can take parameter, like here, 3 so it will listen only maximum 3 clients

while True:
    cliend_obj_or_socket, client_ip = server.accept()
    usr = cliend_obj_or_socket.recv(1024).decode()

    print(f"Connected with {client_ip}, usr: {usr}")

    # cliend_obj_or_socket.send("Hey, welcome to HxD Server..") 
    cliend_obj_or_socket.send(bytes("Hey, welcome to HxD Server...", "utf-8"))    # data can't be sent in sting format throuth network, so we have encoded that into 'utf-8' format bytes.
    cliend_obj_or_socket.close()
    
