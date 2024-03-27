import cv2

classificador = "haarcascade_eye_tree_eyeglasses.xml"
face = cv2.CascadeClassifier(classificador)
lista_fotos = [r'fotos\angelina.jpg',
               r'fotos\dicaprio.jpg',
               r'fotos\gaga.jpg',
               r'fotos\katy.jpg',
               r'fotos\murphy.jpg',
               r'fotos\rock.jpg',
               r'fotos\smith.jpg']

for nome in lista_fotos:
    imagem = cv2.imread(nome)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(
        cinza,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 210), 2)
        
    cv2.imshow("detec~cao de olhos", imagem)
    cv2.waitKey(0)  
print("Fim do programa")