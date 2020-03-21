import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False
    
cap.release()

if ret:
    cv2.imshow('frame',frame)
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

'''
while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################

windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0) 

# FourCC - Four Character Code WMV2,WMV1,MJPG,DIVX,XVID,H264
codec = cv2.VideoWriter_fourcc(*'XVID')
framerate = 30
resolution = (640,480)
out = cv2.VideoWriter('output.avi',codec,framerate,resolution)

print("Width:",cap.get(3),"Height:",cap.get(4))

# cap.set(3,5000)
# cap.set(4,5000)
# print("Width:",cap.get(3),"Height:",cap.get(4))

while True:
    ret,frame = cap.read()
    out.write(frame)
    cv2.imshow(windowName,frame)
    k = cv2.waitKey(1) 
    if k==ord('q'):
        break

cap.release()
out.release()
cv2.destroyWindow(windowName)











