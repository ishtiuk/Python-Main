import socket
import sqlite3


# cursor.execute("CREATE TABLE database (Id INTERGER PRIMARY KEY, Data VARCHAR)")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

s.bind(("127.0.0.1", 9997))
print("Waiting for connection...")

s.listen()

while True:
    connet_database = sqlite3.connect('server.db')
    cursor = connet_database.cursor()

    conn, ip = s.accept()
    print(f"Connected with {ip}")

    conn.send(bytes('Welcome to HxD Server', 'utf-8'))

    cursor.execute("SELECT MAX(id) FROM database")
    primary_id = cursor.fetchone()[0]
    primary_id += 1

    data = conn.recv(1024).decode()
    cursor.execute("INSERT INTO database VALUES(:id, :data)", {'id':primary_id, 'data':data})
    
    cursor.execute("SELECT * FROM database")
    print(cursor.fetchall())

    conn.close()
    connet_database.commit()
    connet_database.close()
    print(f"Client {ip} data has been indexed to database...")