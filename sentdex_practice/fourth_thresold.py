import cv2
import numpy as np

img=cv2.imread('book.jpg')

retreaval,threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retreaval2,threshold2 = cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)
retreaval3,otsu = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

gaus = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gauss',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()