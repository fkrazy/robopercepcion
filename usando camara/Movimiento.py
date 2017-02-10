def corte(imagen):
    EsImagen=False
    linea=imagen.sum(axis=(1,2))
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
