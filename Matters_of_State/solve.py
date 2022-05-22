import warnings
warnings.filterwarnings("ignore")

from pwn import remote
from orbital.elements import KeplerianElements
from orbital import earth
from math import radians

TICKET = '<Your ticket>'
HOST = 'matters_of_state.satellitesabove.me'
PORT = 5300

conn = remote(HOST, PORT)

conn.recvline().decode()
conn.sendline(TICKET.encode())
conn.recvline().decode()

while(True):
    conn.recvline().decode()

    semi_major_axis = conn.recvline().decode().split(':')[1].split(' ')[1]
    eccentricity = conn.recvline().decode().split(':')[1].split(' ')[1]
    inclination = conn.recvline().decode().split(':')[1].split(' ')[1]
    raan = conn.recvline().decode().split(':')[1].split(' ')[1]
    mean_anomaly =conn.recvline().decode().split(':')[1].split(' ')[1]
    argument_of_periapsis = conn.recvline().decode().split(':')[1].split(' ')[1]
    time = conn.recvline().decode().split(' ')[1]

    conn.recvline().decode()
    conn.recvline().decode()

    orbit = KeplerianElements(
        float(semi_major_axis), 
        float(eccentricity) + 0.7,
        radians(float(inclination)),
        radians(float(raan)),
        radians(float(argument_of_periapsis)),
        radians(float(mean_anomaly)),
        earth,
        time
    )

    position = orbit.r
    data = f'{position.x},{position.y},{position.z}'
    conn.sendline(data.encode())

    conn.recvline().decode()

    velocity = orbit.v
    data = f'{velocity.x},{velocity.y},{velocity.z}'
    conn.sendline(data.encode())

    conn.recvline().decode()
    conn.recvline().decode()
    
    data = conn.recvline().decode()

    if len(data.split('flag{')) > 1:
        print(data)
        break
    
conn.close()
