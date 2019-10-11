#!/usr/bin/env python3

import cv2
from mtcnn.mtcnn import MTCNN

image= cv2.imread("dhvanil.jpg")
detector = MTCNN()
#print(detector.detect_faces(image)

result = detector.detect_faces(image)

bounding_box = result[0]['box']
keypoints = result[0]['keypoints']

cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)
cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

cv2.imwrite("dhvanil_drawn.jpg", image)
cv2.namedWindow("image")
cv2.imshow("image",image)
cv2.waitKey(0)

