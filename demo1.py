import cv2

import os,dlib,glob,numpy
from skimage import io

# 数据库中存储个人信息，图片信息
# 调用本机摄像头
# 对比图片信息


def get_person_face():
    # 调用本机摄像头  0代表本机
    cap = cv2.VideoCapture(0)
    # 判断是否成功

    flag = cap.isOpened()

    index = 1
    while (flag):
        ret, frame = cap.read()
        cv2.imshow("Capture_Paizhao", frame)
        k = cv2.waitKey(1) & 0xFF
        # 按下s键，进入下面的保存图片操作
        if k == ord('s'):
            cv2.imwrite(".//face//photo" + str(index) + ".jpg", frame)
            print(cap.get(3))
            print(cap.get(4))
            print("save" + str(index) + ".jpg successfuly!")
            print("-------------------------")
            index += 1
        # 按下q键，程序退出
        elif k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return index

# get_person_face()