import cv2
import numpy as np
image=cv2.imread('messi.jpg')
transpose_image=cv2.transpose(image)
cv2.imshow("original",image)
cv2.imshow("Transposed image",transpose_image)
cv2.waitKey(0)
cv2.destroyAllWindows()