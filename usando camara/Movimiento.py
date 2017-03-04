def corte(linea,rango=20):
    EsImagen=False
    punto=[]
    conteo=0
    for i in range(0,len(linea)-1):
        if linea[i] != 0 and EsImagen == False:
            punto.append(i)
            EsImagen = True
        elif linea[i]==0 and EsImagen==True:
            if conteo==rango:
                punto.append(i)
                EsImagen=False
            conteo+=1
    return punto
     
def EncontrarEsquinas(imagen,esquinas=[],rango=20):
    linea=imagen.sum(axis=(1))
    temesquinas=[]
    temesquinas=corte(linea,rango)
    for i in range(0,len(temesquinas),2):
        if len(temesquinas)!=1:
            if len(temesquinas) != i+1:
                lado=temesquinas[i]
                subimagen= imagen[lado:temesquinas[i+1],:]
            else:
                subimagen = imagen[temesquinas[i]:, :]
        else:
            subimagen = imagen[temesquinas[i]:, :]
            tem=corte(linea,rango)
            if len(tem)==1:
                temesquinas[0]=-1
                esquinas.append(temesquinas)
                break
        esquinas= EncontrarEsquinas(subimagen.T,esquinas,rango)   
        esquinas.append(temesquinas[i:i+2])
    return esquinas

def EncontrarCuadros(imagen,rango=20):
    movBidi=imagen.sum(axis=2)
    esquinas=EncontrarEsquinas(movBidi,esquinas=[],rango=rango)
    cuadros=[]    
    if esquinas!= []:
        cuadros.append([0,0,len(movBidi),len(movBidi.T)])
    esX=True
    for i in range(len(esquinas)-1,0,-1):
        #el carro corre hasta el final del vector
        if esquinas[i][0]==-1:
            cuadros.append([0,0,len(movBidi),len(movBidi.T)])
            #x,y,ancho,alto
            esX=True 
        elif esX:
            if len(esquinas[i])%2==0:
                cuadros[-1][2]=esquinas[i][1]
            cuadros[-1][0]+=esquinas[i][0]
            esX=False
        else:
            if len(esquinas[i])%2==0:
                cuadros[-1][3]=esquinas[i][1]
            cuadros[-1][1]+=esquinas[i][0]
            esX=True
    return cuadros     
            

