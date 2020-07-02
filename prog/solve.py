import socket
from mpmath import *

def test0(n):
    count = 0
    for i in range((2 ** n) -1):
        test = str(format(i, 'b'))
        error = False
        k = 0
        while k < len(test) and test[k] != '1':
            k += 1
        for j in range(k, len(test), 2):
            if test[j] != '1':
                error = True
                break

        if error == False:
            count += 1
    return count+1

def test1(n):
    result = 2
    mult = 2
    for i in range(2, n+1, 2):
        result += 2 * (result + mult)
        mult *= 2

    return result

def test2(n):
    p = int(n / 2) + 1
    p1 = int(mpf(2) ** (p -1))

    if n % 2 != 0:
        return (p1 * 4) - 2
    else:
        return (p1 * 4) - p1 - 2

def solve():
    IP = "142.93.73.149"
    PORT = 26065

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    s.recv(1024*2)
    s.send('start'.encode())
    s.recv(1024)
    count = 1

    while count <= 50:
        try:
          r = s.recv(1024).decode('utf-8')
          c = r.split('Problema')[1].split('\n')[0].strip()
          n = int(r.split("Número de bits:")[1].replace('\n', '').split()[0])
          result = test2(n) % 133337
          print(c)

          s.send(str(result).encode())
          r = s.recv(1024).decode('utf-8')
          print(r.replace('\n', ''))
          if count == 50:
              r = s.recv(1024).decode('utf-8')
              s.close()
              return print(r.replace('\n', ''))
          count += 1
        except:
          return solve()

solve()
