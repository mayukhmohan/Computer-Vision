import cv2

imgpath = "E:\\opencv\\dataset\\4.2.04.tif"
img = cv2.imread(imgpath) 
# Default mode 1
# 0 for grayscale
# -1 as it is without alpha transparency

'''
outpath = "E:\\opencv\\4.2.04.jpg"
cv2.imwrite(outpath,img)
'''

print(type(img))
print(img.dtype)
print(img.shape)
print(img.ndim)
print(img.size)

cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
cv2.imshow('Lena',img)

cv2.waitKey(0)
cv2.destroyWindow('Lena')




    