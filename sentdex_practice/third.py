#image operation
import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

px = img[55,55]
print(px) 

# Region of Image (ROI)
roi = img[100:150,100:150]
print(roi) 
# img[100:150,100:150] = [255,255,255] # White box

watch_face = img[37:111,107:194] # Copy paste
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image arithmetics and logics
img1 = cv2.imread('3d_plot.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('class1.jpg',cv2.IMREAD_COLOR)
img3 = cv2.imread('logo.jpg',cv2.IMREAD_COLOR)

# add = img1 + img2
# add = cv2.add(img1,img2) #directly summed up pixel by pixel so 339 -> 255 downsized so most of it white 
# weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels = img3.shape 
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY) # Gray version
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
# Binary thresold for 0 and 1
# pixel greater than 220 converted into white(255)
# less than 220 converted into black then flipping that around as it is Inverse

#cv2.imshow('mask',mask)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img3_fg = cv2.bitwise_and(img3,img3,mask=mask)

dst = cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols]=dst
#cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('mask',mask)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img3_fg',img3_fg)

# cv2.imshow('weighted',weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

