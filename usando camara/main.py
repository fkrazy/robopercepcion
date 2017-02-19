import cv2
import time
import Movimiento
camara = cv2.VideoCapture(0)
fondo= None
fondo2=None
while(camara.isOpened()):  # check !
    # capture frame-by-frame
    grabbed, frame = camara.read()
    if grabbed: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        #gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        frame2=cv2.GaussianBlur(frame,(21,21),0)
        if fondo is None:
            fondo=frame
            fondo2=frame2
            continue
        contornopres=cv2.absdiff(fondo,frame)
        movimiento=cv2.absdiff(fondo2,frame2)
        movimiento = cv2.threshold(movimiento, 25, 255, cv2.THRESH_BINARY)[1]
        movBidi=movimiento.sum(axis=2)
        cortes=Movimiento.EncontrarEsquinas(movimientoBidi)
        cv2.imshow('presente', frame)
        cv2.imshow('contorno',contornopres)
        cv2.imshow('movimiento',movimiento)
        fondo=frame
        fondo2=frame2
        key=cv2.waitKey(1) & 0xFF
        time.sleep(0.035)
        
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done release the capture
camara.release()
cv2.destroyAllWindows()
