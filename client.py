import socket
import sys
from os import path
import cv2
# create a TCP/IP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 10000
receive_length = 1024
file_dir = 'source_file'
text_file_name = path.join(file_dir, 'text_demo.txt')
video_file_name = path.join(file_dir, 'video_demo.mp4')
image_file_name = path.join(file_dir, 'image_demo.png')

#connection the socket to the port where the server is listening
server_address = (ip_address,port)
print(sys.stderr, 'connecting to {} port {}'.format(server_address[0],server_address[1]))
sock.connect(server_address)

##################### text
# try:
#     # send data
#     with open(text_file_name, 'r') as text_file:
#         for message in text_file:

#             print(sys.stderr, "sending '{}'".format(message))
#             sock.sendall(message.encode())

#             # look for the response
#             amount_received = 0
#             amount_expected = len(message)

#             while(amount_received < amount_expected):
#                 data = sock.recv(receive_length)
#                 amount_received += len(data)
#                 print(sys.stderr,'received "{}"'.format(data))

# finally:
#     print(sys.stderr, 'closing socket')
#     sock.close()


##################### image
# try:
#     # send data
#     with open(image_file_name, 'rb') as image_file:
#         for message in image_file:

#             print(sys.stderr, "sending '{}'".format(message))
#             sock.sendall(message)

#             # look for the response
#             amount_received = 0
#             amount_expected = len(message)

#             while(amount_received < amount_expected):
#                 data = sock.recv(receive_length)
#                 amount_received += len(data)
#                 print(sys.stderr,'received "{}"'.format(data))

# finally:
#     print(sys.stderr, 'closing socket')
#     sock.close()


##################### video
try:
    # send data
    with open(video_file_name, 'rb') as video_file_name:
        for message in video_file_name:

            # print(sys.stderr, "sending '{}'".format(message))
            sock.sendall(message)

            # look for the response
            amount_received = 0
            amount_expected = len(message)

            while(amount_received < amount_expected):
                data = sock.recv(receive_length)
                amount_received += len(data)
                # print(sys.stderr,'received "{}"'.format(data))

finally:
    print(sys.stderr, 'closing socket')
    sock.close()