import cv2
from h import last
image = cv2.imread("x.png")
w, h = image.shape[:2]
bounding_boxes = [(0, 0, w, h)]

# pipeline = my_pipeline(bounding_boxes= bounding_boxes)
pipeline = last(bounding_boxes= bounding_boxes)
import time
st = time.time()
new_image, mask, keypoints, bounding_boxes= pipeline(image)
print(time.time()-st)
# print(pipeline)
# cv2.imshow("folding", data)
# print(bounding_boxes)
cv2.imwrite("folding.png", new_image)