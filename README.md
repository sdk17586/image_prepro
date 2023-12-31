# image_prepro
CLAHE를 이용한 그레이스케일 이미지 처리
CLAHE는 이미지의 대비를 개선하는 알고리즘으로, 특히 밝기 대비가 낮은 이미지에서 유용합니다.

python
Copy code
import cv2

# 이미지 읽기
img = cv2.imread('path/to/image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# CLAHE 객체 생성
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))

# CLAHE 적용
clahe_img = clahe.apply(gray)

# 결과 저장
cv2.imwrite('gray_clahe.png', clahe_img)
이 코드는 이미지를 그레이스케일로 변환한 후 CLAHE를 적용합니다. clipLimit는 대비 제한 임계값을, tileGridSize는 이미지를 분할하는 영역의 크기를 설정합니다.

3채널 HSV 이미지에 CLAHE 적용
이미지의 색상 정보를 보존하면서 밝기 대비를 개선하고자 할 때, HSV(Hue, Saturation, Value) 형식으로 변환한 후 V 채널에 CLAHE를 적용할 수 있습니다.

python
Copy code
import cv2

# 이미지 읽기
image = cv2.imread('path/to/image.jpg')

# HSV로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# CLAHE 객체 생성 및 적용
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
v_eq = clahe.apply(v)
hsv_eq = cv2.merge((h, s, v_eq))
bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

# 결과 저장
cv2.imwrite('hsv_clahe.jpg', bgr_eq)
여기서도 clipLimit와 tileGridSize를 통해 CLAHE 알고리즘의 동작을 조절할 수 있습니다.
