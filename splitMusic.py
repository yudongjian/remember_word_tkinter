import pygame
import time
def play_music():
    filepath = r"C:\Users\25162\Desktop\起床闹钟.mp3"
    pygame.mixer.init()
    # 加载音乐
    print('加载中...')
    pygame.mixer.music.load(filepath)
    print('ok')
    pygame.mixer.music.play(start=0.0)
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    time.sleep(300)
    pygame.mixer.music.stop()

play_music()

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('temp.avi')
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # show gray picture
#     #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     #cv.imshow('frame', gray)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
