import cv2
import numpy as np
import matplotlib.pyplot as plt




# <clahe gray>
img = cv2.imread('/data/sungmin/fog_resnet/sample/test_sample/CCTV_INS_YJD_20211118082900-1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(gray)

cv2.imwrite('gray_clahe.png', clahe_img)



# <3chanel h.s.v clahe>
# image = cv2.imread('/data/sungmin/fog_resnet/sample/test_sample/CCTV_INS_YJD_20211118082900-1.jpg')

# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# v_eq = clahe.apply(v)
# hsv_eq = cv2.merge((h, s, v_eq))
# bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

# cv2.imwrite('.jpg', bgr_eq)