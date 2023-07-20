# <히스토그램 균일화>
import cv2
import numpy as np
import os


import cv2
import numpy as np

def contrast_stretching(image):
    # 영상의 최소값과 최대값 계산
    min_val = np.min(image)
    max_val = np.max(image)

    # 스트레칭 함수 계산
    stretched_image = ((image - min_val) / (max_val - min_val)) * 255
    stretched_image = stretched_image.astype(np.uint8)

    return stretched_image


#<바꿀 이미지가 있는 폴더>
img_path = '/data/sungmin/fog_data/jd_img'
img_file_path = os.listdir(img_path)
end ='.jpg'

# <3chanel h.s.v clahe>


# for file_name in img_file_path:
#     if file_name.endswith(end):
#         image_path = os.path.join(img_path, file_name)
#         image = cv2.imread(image_path)

#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#         h, s, v = cv2.split(hsv)
#         clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#         v_eq = clahe.apply(v)
#         hsv_eq = cv2.merge((h, s, v_eq))
#         bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

#         cv2.imwrite('/data/sungmin/fog_test_data/3ch_clache/{}'.format(file_name), bgr_eq)

#<이미지 스트레칭>
for file_name in img_file_path:
    if file_name.endswith(end):
        image_path = os.path.join(img_path, file_name)
        image = cv2.imread(image_path)
        stretched_image = contrast_stretching(image)

        cv2.imwrite('/data/sungmin/fog_test_data/contarst_strech/{}'.format(file_name),stretched_image)



# <gray equalizHist all>
# for file_name in img_file_path:
#     if file_name.endswith(end):
#         image_path = os.path.join(img_path, file_name)
        
#         img = cv2.imread(image_path)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         eql = cv2.equalizeHist(gray)
#         #<바꾼 이미지가 저장될 폴더>
#         cv2.imwrite('/data/sungmin/fog_test_data/jd_eqh_img/{}'.format(file_name), eql)    



# <gray equalizHist>
# image = cv2.imread('/data/sungmin/fog_test_data/jd_image/CCTV_INS_JD_20211121170600-0.jpg')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# equalized = cv2.equalizeHist(gray)

# cv2.imwrite('/data/sungmin/preprocessing/histo_eql.png',equalized)

# <origin image>
# cv2.imwrite('/data/sungmin/preprocessing/origin.png',image)


