def corte(linea):
    EsImagen=False
    j=0
    punto=[]
    for i in linea:
        if linea[j]!= 0 and EsImagen==False:
            punto.append(j)
            EsImagen=True
        elif linea[j]==0 and EsImagen==True:
            punto.append(j)
            EsImagen=False
        j+=1
    return punto

def EncontrarEsquinas(imagen, esquinas=[]):
    linea=imagen.sum(axis=(1,2))
    tam= esquinas.count
    esquinas.append(corte(linea))
    esquinas.append(-1)
    imagen=imagen.T
    if esquinas.count <= tam+2:
        esquinas.append(corte(imagen))
    else:
        esquinas.append(EncontrarEsquinas(imagen,esquinas))
    
    return esquinas
    