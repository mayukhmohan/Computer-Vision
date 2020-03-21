import cv2

'''
30 fps video capture rate to have a smooth playback
1000ms = 1s. Waitkey is 1 milisecond and we need 
30 frames per one second
1000/video_capture_fps = 1000/30 = 33
33*30 ~= 1000
'''

windowName = "OpenCV Video Player"
filename = "E:\\opencv\\output.avi"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(filename)

while (cap.isOpened()):
    ret,frame = cap.read()
    
    if ret:
        cv2.imshow(windowName,frame)
        k = cv2.waitKey(33) 
        if k==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyWindow(windowName)
