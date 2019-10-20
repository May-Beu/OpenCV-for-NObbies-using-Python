import cv2
import numpy as np
#making a rectangle
zero_array=np.zeros((300,300),np.uint8)
cv2.rectangle(zero_array,(100,100),(200,200),255,-1)
cv2.imshow("rectangle",zero_array)
cv2.waitKey(0)
#making a ellipse
zero_array1=np.zeros((300,300),np.uint8)
cv2.ellipse(zero_array1,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",zero_array1)
cv2.waitKey(0)
#to perform bitwise and 
bitwiseand=cv2.bitwise_and(zero_array,zero_array1)
cv2.imshow("bitwise and",bitwiseand)
cv2.waitKey(0)
#to perform bitwise or
bitwiseor=cv2.bitwise_or(zero_array,zero_array1)
cv2.imshow("bitwise and",bitwiseand)
cv2.waitKey(0)
#to perform not 
bitwisenot=cv2.bitwise_not(zero_array,zero_array1)
cv2.imshow("bitwise not",bitwisenot)
cv2.waitKey(0)
#to perform bitwise xor
bitwisexor=cv2.bitwise_xor(zero_array,zero_array1)
cv2.imshow("bitwise xor",bitwisexor)
cv2.waitKey(0)
cv2.destroyAllWindows()