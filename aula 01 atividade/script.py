'''
aplicar reconhecimento de carros e Filtro gaussiano
ns fotos (car1.jpg, car2.jpg, car3.jpg, car4.jpg, car5.jpg)
Fazer para 3 valores de cariância do filtro Gaussiano: (1, 5, 10)
Total de 15 simulações
Salvar o resultado e apresentar
'''
import cv2
import numpy as np

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car1.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)

for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car1.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)

for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),1)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car1.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 5)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),5)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car1.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 10)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car2.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),1)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car2.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 5)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),5)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car2.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 10)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car3.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)

for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),1)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car3.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 5)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),5)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car3.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 10)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car4.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),1)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car4.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 5)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),5)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car4.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 10)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car5.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 1)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),1)
    carros[y:y+h,x:x+w]=regiao_filtro
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car5.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),5)
    carros[y:y+h,x:x+w]=regiao_filtro

    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''

id_carros = cv2.CascadeClassifier('cars.xml')
carros = cv2.imread('car5.jpg')
cinza = cv2.cvtColor(carros, cv2.COLOR_BGR2GRAY)
filtro = cv2.GaussianBlur(carros, (15, 15), 10)
localizados = id_carros.detectMultiScale(cinza, 1.1, 3)


for (x,y,w,h) in localizados:
    cv2.rectangle(carros, (x,y), (x+w, y+h), (0, 255, 0), 2)
    regiao=carros[y:y+h,x:x+w]
    regiao_filtro=cv2.GaussianBlur(regiao,(15, 15),10)
    carros[y:y+h,x:x+w]=regiao_filtro
    
    
cv2.imshow('Identificando os carros', carros)

cv2.waitKey(0)

'''--------------------------------------------------------'''
