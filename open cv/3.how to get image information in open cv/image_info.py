#in this section i will show you how to see or get information about image
#the information will tell you the the height and width of image in terms of pixel
import cv2
image=cv2.imread("messi.jpg")
cv2.imshow("output image",image)
#now to see the information of image we will use "shape ()"module/function of opencv
#it will give the information in tuple
#it will give the information of Pixel in Width
#it will give the information of Pixel in Height
#it will give the information of layer
#it gives the output as (height,width,layer)
print(image.shape)
#if we want to print the height and width seprate 
print("Height Pixel Value: ",image.shape[0]) #here 0,1 represent the index location in tuple
print("Height Pixel Value: ",image.shape[1])
cv2.waitKey(0)
cv2.distroyAllWindow() 