import herramientas1 as herramientas
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
     
def EncontrarEsquinas(imagen,esquinas=[],rango=20,distancia=[0]):
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
                distancia[-1]=-1
                break
        esquinas, distancia= EncontrarEsquinas(subimagen.T,esquinas,rango,distancia)        
        if distancia[-1]==-1:
            distancia[-1]=len(subimagen)
            distancia.append(0)
        esquinas.append(temesquinas)
    return esquinas, distancia

def EncontrarCuadros(imagen,rango=20):
    movBidi=imagen.sum(axis=2)
    esquinas, distancia=EncontrarEsquinas(movBidi,rango=rango)
    cuadros=[]
    x1=0
    y1=0
    ancho=0
    alto=0
    contador=0
    esX=True
    for i in range(len(esquinas)-1):
        #el carro corre hasta el final del vector
        if esquinas[i][0]==-1:   
            #busca el final de cada imagen
            for ret in range(i-1,0,-1):
                #recorre de regreso hasta el inicio
                if esquinas[ret][-1]!=-1:
                    #define cuando estamos en eje x o en eje y
                    herramientas.switchBoolean(esX)
                    for k in range(len(esquinas[ret])-1): 
                        #busca entre los cortes del eje
                        if esquinas[ret][k]!=-1:
                            #busca los parametros del eje a escribir
                            if contador==0:
                                if esX:
                                    x1+=esquinas[ret][k]    
                                else:
                                    y1+=esquinas[ret][k]
                            elif contador==1:
                                if esX and ancho==0:
                                    ancho=esquinas[ret][k]-esquinas[ret][k-1]
                                if not esX and alto==0:
                                    alto=esquinas[ret][k]-esquinas[ret][k-1]                                              
                            elif contador==2:
                                break
                            if k== i-1:
                                #elimina el primer corte
                                esquinas[ret][k]=-1  
                    contador+=1
            cuadros.append(x1,y1,ancho,alto)
        else:
            esX=herramientas.switchBoolean(esX)
    return cuadros    
            
            

