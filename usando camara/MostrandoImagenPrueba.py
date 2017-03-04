import cv2
import Movimiento
im=cv2.imread("movimiento.png")
cuadro=Movimiento.EncontrarCuadros(im,rango=0)
for i in cuadro:
    cv2.rectangle(im, (i[1],i[0]),  ( i[3],i[2]), (0, 255, 0), 2 )
cv2.imshow("imagen",im)