import cv2
import Dir
import numpy as np

# 이미지를 읽기 위한 코드
image = cv2.imread(Dir.dir+"[Dataset]_Module22_images/pcb.png")

#  2D 컨볼루션을 실행하기 위해 회색조로 변환합니다.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 회색조 이미지 표시
cv2.imshow("Original Greyscale Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 평균값 필터 = kernel1 = np.ones((19,19),np.float32)/361 잡음을 제거하기 위해 사용
kernel1 = np.ones((19,19),np.float32)/361      # 19x19 컨볼루션 필터
filter1 = cv2.filter2D(gray,-1,kernel1)

# 1.필터링 종류
# 2. 필터링 작동 방법
# 3. cv2.filter2D()원형 알아보기
# scalefreeus.tistory.com/14

cv2.imshow("Original Greyscale Image",gray)
cv2.imshow("Filter1",filter1)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel2 = np.array((                        # 3x3 컨볼루션 필터
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]), np.float32)*2
filter2 = cv2.filter2D(gray,-1,kernel2)

cv2.imshow("Original Greyscale Image",gray)
cv2.imshow("Filter2",filter2)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel3 = np.array((
    [-2, -2, 0],
    [-2, 1, 2],
    [0, 2, 2]), dtype="int")
filter3 = cv2.filter2D(gray,-1,kernel3)

cv2.imshow("Original",gray)
cv2.imshow("Filter3",filter3)     # 출력된 이미지가 포토샵의 필터를 연상시키나요?
cv2.waitKey(0)
cv2.destroyAllWindows()