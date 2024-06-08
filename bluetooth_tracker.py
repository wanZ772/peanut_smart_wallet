import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
for i in range(0,20):
    try:
        server.connect(('c0:2e:25:54:c2:38', i))
        print(f"[ + ] Connected @ CH {i} !")
        break
    except:
        print(f"{i} --> Not available")

try:
    while True:
        server.send("1".encode('utf-8'))
        if (server.recv(1024)):
            print("connected")
        else:
            print("connection lost! check your wallet!")

except:
    print("Error")