import cv2
import numpy as np


img_path = '/data/sungmin/fog_resnet/sample/test_sample/CCTV_INS_YHD_20211111113900-0.jpg'
img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

edges = cv2.Canny(binary, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
horizontal_lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    slope = abs((y2 - y1) / (x2 - x1))
    if slope < 0.1: 
        horizontal_lines.append(line)

for line in horizontal_lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 2)  

# 블러 처리
for line in horizontal_lines:
    x1, y1, x2, y2 = line[0]
    # 왼쪽에 100 픽셀의 여유 공간을 줌
    # left = min(x1, x2) - 100 
    # # 오른쪽에 100 픽셀의 여유 공간을 줌 
    # right = max(x1, x2) + 100  
    # 상단에 100 픽셀의 여유 공간을 줌
    top = min(y1, y2) - 50
     # 하단에 100 픽셀의 여유 공간을 줌
    bottom = max(y1, y2) + 50 
    
    roi = img[top:bottom]
    blurred_roi = cv2.GaussianBlur(roi, (99, 99), 0)  
    img[top:bottom] = blurred_roi

cv2.imwrite('edge.png', edges)
cv2.imwrite('HoughL_No_fog.png', img)


