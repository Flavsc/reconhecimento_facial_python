import cv2
import numpy as np

img = cv2.imread('coala.jpg')
filtro = cv2.GaussianBlur(img, (15, 15), 3)
cv2.imshow("Filtro Gaussiano", filtro)
cv2.waitKey(0)