import socket

HOST = '0.0.0.0'
PORT = 8089
PORT1 = 12345
ADDR = (HOST,PORT)
ADDR1 = (HOST,PORT1)
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR1)


print 'Listening...'
while True:
    conn, addr = server.accept()
    print 'client connected ... ', addr
    try:
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
                client.close()
                break 
                    #data.append(chunk)
            client.send(data)
            print "Sending data"

    except:
        print("Main Server is offline")
        client.close()
        break

