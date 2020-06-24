import socket

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    IP = "142.93.73.149"
    PORT = 12064

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    s.recv(1024*2).decode('utf-8')
    s.send('start'.encode())
    s.recv(1024).decode('utf-8')

    while True:
        try:
            r = s.recv(1024).decode('utf-8')
            r = r.replace(' ', '')
            c = r.split('Problema')[1].split('\n')[0]
            print(c)
            hourglass1 = int(r.split('Ampulheta01')[1].split(':')[1].split('\n')[0])
            hourglass2 = int(r.split('Ampulheta02')[1].split(':')[1].split('\n')[0])
            closing_time = int(r.split('MomentodeEncerramento')[1].split(':')[1].split('\n')[0])

            count = 0
            if closing_time > 10000000000 or (closing_time % hourglass1 != 0 and closing_time % hourglass1 != 0):
                count = -1
            else:
                while count <= closing_time and lcm(lcm(hourglass1, hourglass2), count) != closing_time:
                    count += 1
                if count > closing_time:
                    count = -1

            s.send(str(count).encode())
            r = s.recv(1024).decode('utf-8')
            print(r.replace('\n', ''))
            if c.split('/')[0] == "050":
                r = s.recv(1024).decode('utf-8')
                s.close()
                return print(r.replace('\n', ''))
        except:
            s.close()
            return solve()

solve()
