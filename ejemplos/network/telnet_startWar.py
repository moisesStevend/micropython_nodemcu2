import socket

#addr_info = socket.getaddrinfo("furrymuck.com", 8888)
addr_info = socket.getaddrinfo("aardmud.org",23)
addr = addr_info[0][-1]

s = socket.socket()
s.connect(addr)

while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')
