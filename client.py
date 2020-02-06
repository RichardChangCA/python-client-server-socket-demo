import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connection the socket to the port where the server is listening
server_address = ("localhost",10000)
print(sys.stderr, 'connecting to {} port {}'.format(server_address[0],server_address[1]))
sock.connect(server_address)

try:
    # send data
    message = "This is the message and it will be repeated"
    print(sys.stderr, "sending '{}'".format(message))
    sock.sendall(message.encode())

    # look for the response
    amount_received = 0
    amount_expected = len(message)

    while(amount_received < amount_expected):
        data = sock.recv(16)
        amount_received += len(data)
        print(sys.stderr,'received "{}"'.format(data))

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
