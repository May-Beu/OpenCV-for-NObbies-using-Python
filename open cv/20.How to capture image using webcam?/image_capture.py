import cv2
import matplotlib.pyplot as plt
image=cv2.VideoCapture(0)
#now to cheak if stream is comming or not
if image.isOpened():
    ret,frame=image.read()
    #if we want to cheak which type of values are coming as return value in variable 'ret' and 'frame'
    print(ret)
    print(frame)
else:
    ret=False
img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #we can change in any format ex- Gray scale,RGB,HSV   
plt.imshow(img) 
plt.title("Output Image")
plt.xticks([])  
plt.yticks([])
plt.show()
cv2.waitKey(0)
image.release()
cv2.destroyAllWindows()

