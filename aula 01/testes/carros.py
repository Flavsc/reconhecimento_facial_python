import cv2
import numpy as np

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car1.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)

for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)