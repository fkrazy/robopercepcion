def corte(linea):
    EsImagen=False
    punto=[]
    for i in range(0,len(linea)):
        if linea[i]!= 0 and EsImagen==False:
            punto.append(i)
            EsImagen=True
        elif linea[i]==0 and EsImagen==True:
            punto.append(i)
            EsImagen=False
    return punto
     
def EncontrarEsquinas(imagen, esquinas=[]):
    linea=imagen.sum(axis=(1,2))
    esquinas.append(corte(linea))
    for i in range(0,len(esquinas[-1]),2):
        if esquinas[-1].count != 1:
            subimagen= imagen[esquinas[-1][i]:esquinas[-1][i+1],:,:]                
        else:
            subimagen=imagen[esquinas[-1][i]:,:,:]        
    return esquinas

