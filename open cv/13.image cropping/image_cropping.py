import cv2
import numpy as np
image=cv2.imread('messi.jpg')
height,width=image.shape[:2]
start_row,start_col=int(height*.25),int(width*.25)
end_row,end_col=int(height*.45),int(width*.45)
img=image[start_row:end_row,start_col:end_col]
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.imshow("cropped",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
