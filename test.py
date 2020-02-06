import numpy as np
import cv2
from os import path

file_dir = 'source_file'
video_file_name = path.join(file_dir, 'video_demo.mp4')
image_file_name = path.join(file_dir, 'image_demo.png')

# cap = cv2.VideoCapture(video_file_name)

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if(ret == True):
#         frame = cv2.flip(frame,180)

#         cv2.imshow('frame',frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()

img = cv2.imread(image_file_name)
cv2.imshow('image',img)
cv2.waitKey(1000) # wait for 1000ms = 1s
cv2.destroyAllWindows()