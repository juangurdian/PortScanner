
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.settimeout()

host = input("Enter IP to scan: ")
port = int(input("Enter Port: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print('Port is Closed')
    else:
        print('The port is Open')

portScanner(port)