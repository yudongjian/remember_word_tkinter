import cv2


def getImageVar(imgPath):
    image = cv2.imread(imgPath)

    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()

    return imageVar


imgvar = getImageVar(r'C:\Users\25162\Desktop\微信图片_20210409151415.png')
print(type(imgvar))