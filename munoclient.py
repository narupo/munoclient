import socket
import sys

if len(sys.argv) < 2:
    print('munoclient.py [address:port]')
    sys.exit(1)

addr_port = sys.argv[1]
addr, port = addr_port.split(':')
port = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 8888))

sock.sendto(b'0', (addr, port))
