import socket
import sys
from os import path
import cv2

ip_address = "127.0.0.1"
port = 10000
receive_length = 1024
file_dir = 'source_file'
received_file_name = path.join(file_dir, 'received_text_demo.txt')
received_video_file_name = path.join(file_dir, 'received_video_demo.mp4')
received_image_file_name = path.join(file_dir, 'received_image_demo.png')

# create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = (ip_address,port)
print(sys.stderr, 'starting up on {} port {}'.format(server_address[0],server_address[1]))
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

################## text
# while True:
#     # wait for a connection
#     print(sys.stderr, "waiting for a connection")
#     connection, client_address = sock.accept()

#     try:
#         print(sys.stderr, "connection from", client_address)
#         receive_file = open(received_file_name,'w')
#         # receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(receive_length)
#             print(sys.stderr, 'received "{}"'.format(data))
#             receive_file.write(data.decode())
#             if data:
#                 print(sys.stderr, "sending data back to the client")
#                 connection.sendall(data)
#             else:
#                 print(sys.stderr, "no more data from", client_address)
#                 break
#         receive_file.close()

#     finally:
#         # clean up the connection
#         connection.close()

################## image
# while True:
#     # wait for a connection
#     print(sys.stderr, "waiting for a connection")
#     connection, client_address = sock.accept()

#     try:
#         print(sys.stderr, "connection from", client_address)
#         receive_file = open(received_image_file_name,'wb')
#         # receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(receive_length)
#             print(sys.stderr, 'received "{}"'.format(data))
#             receive_file.write(data)
#             if data:
#                 print(sys.stderr, "sending data back to the client")
#                 connection.sendall(data)
#             else:
#                 print(sys.stderr, "no more data from", client_address)
#                 break
#         receive_file.close()

#     finally:
#         # clean up the connection
#         connection.close()
#     img = cv2.imread(received_image_file_name)
#     cv2.imshow('image',img)
#     cv2.waitKey(1000) # wait for 1000ms = 1s
#     cv2.destroyAllWindows()

################## video
while True:
    # wait for a connection
    # print(sys.stderr, "waiting for a connection")
    connection, client_address = sock.accept()

    try:
        # print(sys.stderr, "connection from", client_address)
        receive_file = open(received_video_file_name,'wb')
        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(receive_length)
            # print(sys.stderr, 'received "{}"'.format(data))
            receive_file.write(data)
            if data:
                pass
                # print(sys.stderr, "sending data back to the client")
                # connection.sendall(data)
            else:
                # print(sys.stderr, "no more data from", client_address)
                break
        receive_file.close()

    finally:
        # clean up the connection
        connection.close()
    cap = cv2.VideoCapture(received_video_file_name)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret == True):
            frame = cv2.flip(frame,180)

            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

    # server can listen many tasks
    # transmiting a video takes too much time
    # divide a video into many tasks and sent to server seperately, combine these in the server, with tag
    # if server is full, how to tackle the stuck