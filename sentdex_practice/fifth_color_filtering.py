import cv2
import numpy as np


cap = cv2.VideoCapture(0)  

while True:
    _, frame = cap.read()
    # HSV :: hue saturation and value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])
    
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    kernel = np.ones((5,5),np.uint8)
    #erosion = cv2.erode(mask,kernel,iterations = 1)
    #dilation = cv2.dilate(mask,kernel,iterations = 1)
    
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) # Removing false positive the background noise
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) # Removing false negative the noise on red hat
    
    
    #dark_red = np.uint8([[[12,22,121]]])
    #dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
    
    '''kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(res,-1,kernel)
    
    blur = cv2.GaussianBlur(res,(15,15),0)
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)'''
    
    '''
    # It is the difference between input image and opening of the image
    cv2.imshow('TopHat',tophat)
    # It is the difference between input image and closing of the image
    cv2.imshow('BlackHat',blackhat)'''
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    #cv2.imshow('erosion',erosion)
    #cv2.imshow('dilation',dilation)
    
    '''# cv2.imshow('bilateral',bilateral)
    # cv2.imshow('median',median) #less noisy
    # cv2.imshow('blur',blur)
    # cv2.imshow('smooth',smooth)'''
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()