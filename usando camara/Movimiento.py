anchoImagen=480
altoImagen=640
def corte(linea,rango=20):
    EsImagen=False
    punto=[]
    conteo=-1
    for i in range(0,len(linea)-1):
        if linea[i] != 0 and EsImagen == False:
            punto.append(i)
            EsImagen = True     
        elif linea[i]==0 and EsImagen==True:
            conteo+=1
            if conteo==rango:
                punto.append(i-conteo)
                EsImagen=False
                conteo=-1
        if i==len(linea)-2 and conteo>0:
            punto.append(i-conteo)    
    return punto
    
def EncontrarEsquinas(imagen,esquinas=[],rango=20,cuadros=[],columna=0):
    linea=imagen.sum(axis=(1))
    temesquinas=[]     
    temesquinas=corte(linea,rango)
    if temesquinas!=[] and cuadros==[]:
        cuadros=[[0,0,anchoImagen,altoImagen]]   
    x_y=columna%2
    columna+=1
    if len(cuadros)!=0:
        temcuadros=cuadros[-1].copy()
    for i in range(0,len(temesquinas),2):       
        if len(temesquinas)!=1:           
            if len(temesquinas) != i+1:
                lado=temesquinas[i]
                subimagen= imagen[lado:temesquinas[i+1],:]
            else:
                subimagen = imagen[temesquinas[i]:, :]
        else:
            subimagen = imagen[temesquinas[i]:, :]
            linea=subimagen.sum(axis=(0))
            tem=corte(linea,rango)
            if len(tem)==1:
                if temesquinas[0]!=0:
                    #cuando es fin de corte pero no es 0 se suma
                    cuadros[-1][x_y]+=temesquinas[0]
                if tem[0]==0:
                    temesquinas[0]=-1
                    esquinas.append(temesquinas)  
                    
                else:
                    temesquinas[0]=tem[0]
                    temesquinas.append(-1)
                    esquinas.append([temesquinas[1]])                    
                    esquinas.append([temesquinas[0]])                    
                    cuadros[-1][1-x_y]+=tem[0] 
                break 
        if i>1:
             cuadros.append(temcuadros.copy())   
        cuadros[-1][x_y]+=temesquinas[i]
        if i+1!= len(temesquinas):
             cuadros[-1][x_y+2]=temesquinas[i+1]-temesquinas[i]+cuadros[-1][x_y]                
        esquinas,cuadros= EncontrarEsquinas(subimagen.T,esquinas,rango,cuadros,columna)   
        esquinas.append(temesquinas[i:i+2])    
    return esquinas,cuadros

def EncontrarCuadros(imagen,rango=20):
    movBidi=imagen.sum(axis=2)
    esquinas,cuadros=EncontrarEsquinas(movBidi,esquinas=[],rango=rango)
    return cuadros
            

