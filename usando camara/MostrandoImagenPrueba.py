import cv2
import Movimiento
imagenes=[]
im=cv2.imread("movimiento2.png")
imagenes.append(im)
for j in imagenes:
    cuadro=Movimiento.EncontrarCuadros(j,rango=20)
    im=j
    k=0
    for i in cuadro:           
        cv2.rectangle(im, (i[1],i[0]),  ( i[3],i[2]), (0, 255, 0), 2 )
        cv2.putText(im,str(k),(i[1],i[0]), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),2)
        k+=1
    cv2.imshow("imagen",im)