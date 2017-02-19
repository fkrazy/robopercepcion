import cv2
import Movimiento
im=cv2.imread("movimiento.png")
im=im.sum(axis=2)
linea=Movimiento.EncontrarEsquinas(im,rango=0)