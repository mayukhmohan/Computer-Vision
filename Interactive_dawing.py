import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

#####################################

windowName = "Drawing"
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)

# bind the callback function
cv2.setMouseCallback(windowName,draw_circle)

while True:
    cv2.imshow(windowName,img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cv2.destroyAllWindows()

#######################################
windowName = "Drawing"
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

# true if mouse is pressed
drawing = False

# if True,draw rectangle.Press 'm' to toggle to curve
mode = True
(ix,iy) = (-1,-1)

# Mouse Callback Function
def draw_shape(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix,iy)=x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode ==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


cv2.setMouseCallback(windowName,draw_shape)


global mode
   
while True:
    cv2.imshow(windowName,img)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
        
cv2.destroyAllWindows()
        
        
        
        
        
        
        
