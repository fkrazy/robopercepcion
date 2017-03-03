import cv2
import Movimiento
im=cv2.imread("movimiento.png")
cuadro=Movimiento.EncontrarCuadros(im,rango=0)
print(cuadro)