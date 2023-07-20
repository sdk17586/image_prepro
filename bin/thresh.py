import os
import json
import cv2


# dir_paths = '/data/sungmin/threshholding/gh_image'

# file_paths = [os.path.join(dir_paths, f) for f in os.listdir(dir_paths) if f.endswith('.jpg')]

# for i in file_paths:
    
#     file_name = os.path.basename(i)
#     name_only = os.path.splitext(file_name)[0]
#     path = f"/data/sungmin/threshholding/thresh_image/{name_only}.jpg"
    
#     img = cv2.imread(i)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     _, binary =  cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     cv2.imwrite(path, binary)


#<이진화>

img_path = '/data/sungmin/fog_resnet/sample/test_sample/CCTV_INS_YJD_20211118103800-1.jpg'
img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('binary.png', binary)










