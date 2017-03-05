import cv2
import Movimiento
imagenes=[]
im=cv2.imread("movimiento2.png")
imagenes.append(im)
for j in imagenes:
    cuadro=Movimiento.EncontrarCuadros(j,rango=0)
    im=j
    k=255
    for i in cuadro:       
        cv2.rectangle(im, (i[1],i[0]),  ( i[3],i[2]), (0, k, 0), 2 )
    cv2.imshow("imagen",im)