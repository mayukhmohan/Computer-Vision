import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "E:\\opencv\\dataset\\"

imp1 = path + "4.2.01.tiff"
imp2 = path + "4.2.04.tif"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
img1 = cv2.imread(imp1,1)
img2 = cv2.imread(imp2,1)

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

# mult = img1*img2
# add =img1 + img2
# sub = img1 - img2
# subd = img2 - img1
# div = img1 / img2
alpha = 0.5
beta = 0.5
gamma = 0
output = cv2.addWeighted(img1,alpha,img2,beta,gamma)
## output = img1 * alpha + img2 * beta + gamma (where alpha + beta = 1)

# titles = ["Liquid Drop","Lena","Add","Sub","Subd","mult","div"]
# images = [img1,img2,add,sub,subd,mult,div]
titles = ["Liquid Drop","Lena","Weighted"]
images = [img1,img2,output]

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()

###############################################
import time
path = "E:\\opencv\\dataset\\"

imp1 = path + "4.2.01.tiff"
imp2 = path + "4.2.04.tif"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
img1 = cv2.imread(imp1,1)
img2 = cv2.imread(imp2,1)

alpha = 0.0
beta = 1.0
gamma = 0

for i in np.linspace(0,1,10):
    alpha = i
    beta = 1 - alpha
    output = cv2.addWeighted(img1,alpha,img2,beta,gamma)
    cv2.imshow("Transition",output)
    time.sleep(1)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
################################################
path = "E:\\opencv\\dataset\\"

def emptyFunction():
    pass

imp1 = path + "4.2.01.tiff"
imp2 = path + "4.2.04.tif"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
img1 = cv2.imread(imp1,1)
img2 = cv2.imread(imp2,1)

alpha = 0.5
beta = 0.5
gamma = 0
output = cv2.addWeighted(img1,alpha,img2,beta,gamma)

windowName = "transition Demo"
cv2.namedWindow(windowName)

cv2.createTrackbar("alpha",windowName,0,100,emptyFunction)

while True:
    cv2.imshow(windowName,output)
    if cv2.waitKey(1) == 27:
        break
    alpha = cv2.getTrackbarPos("alpha",windowName)/100
    beta = 1 - alpha
    
    output = cv2.addWeighted(img1,alpha,img2,beta,gamma)
    cv2.imshow(windowName,output)
    

cv2.destroyAllWindows()






