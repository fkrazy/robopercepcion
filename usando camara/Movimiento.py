def corte(linea,rango=20):
    EsImagen=False
    punto=[]
    conteo=0
    for i in range(0,len(linea)-1):
        if linea[i] != 0 and EsImagen == False:
            punto.append(i)
            EsImagen = True
        elif linea[i]==0 and EsImagen==True:
            conteo+=1
            if conteo==rango:
                punto.append(i)
                EsImagen=False
    return punto
     
def EncontrarEsquinas(imagen, esquinas=[],rango=20):
    linea=imagen.sum(axis=(1))
    esquinas.append(corte(linea,rango))
    for i in range(0,len(esquinas[-1]),2):
        if len(esquinas[-1])!=1 or esquinas[-1][0]!=0:
            if len(esquinas[-1]) != i+1:
                subimagen= imagen[esquinas[-1][i]:,:]
            else:
                subimagen = imagen[esquinas[-1][i]:, :]
        else:
            subimagen = imagen[esquinas[-1][i]:, :]
            tem=corte(linea,rango)
            if len(tem)==1:
                break
        esquinas= EncontrarEsquinas(subimagen.T,esquinas)
       
    return esquinas

