import cv2
import matplotlib.pyplot as plt

imgpath = "E:\\opencv\\dataset\\4.2.04.tif"
img = cv2.imread(imgpath)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

# cv2.imshow('Lena',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###########################################

imgpath = "E:\\opencv\\dataset\\4.2.04.tif"
img = cv2.imread(imgpath,0)

plt.imshow(img,cmap = 'gray')
plt.show()

###########################################

imgpath = "E:\\opencv\\dataset\\4.2.04.tif"
img = cv2.imread(imgpath)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img,cmap = 'gray')
plt.show()

###########################################

j=0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        print(filename)
        j += 1
print("There are",j,"files")