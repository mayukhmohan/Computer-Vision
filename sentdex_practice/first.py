'''loading images and videos'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
#                               0
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMRERAD_UNCHANGED = -1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([50,100],[30,40],color='cyan')
#plt.show()

#cv2.imwrite('hey.png',img) # creating file



cap = cv2.VideoCapture(0)  ##cap = cv2.VideoCapture('output.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()