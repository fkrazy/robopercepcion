import cv2
import Movimiento
imagenes=[]
im=cv2.imread("movimiento.png")
imagenes.append(im)
im=cv2.imread("negro.png")
imagenes.append(im)
im=cv2.imread("movimiento.png")
imagenes.append(im)
for j in imagenes:
    cuadro=Movimiento.EncontrarCuadros(j,rango=0)
    im=j
    for i in cuadro:       
        cv2.rectangle(im, (i[1],i[0]),  ( i[3],i[2]), (0, 255, 0), 2 )
    cv2.imshow("imagen",im)