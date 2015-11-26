import numpy 
import math
from math import *
import decimal


#Funcion para trabajar con Movielens 100m
def matrizfac():
    #Insertar los ratings.
    movies={}
    for line in open('u.item'):
         (id,title)=line.split('|')[0:2]
         movies[id]=id
    # Load data
    items=[]
    users=[]
    listarat=[]
    for line in open('u3.base'):
         tem=[]
         (user,movieid,rating,ts)=line.split('\t')
         tem.append(user)
         tem.append(movieid)
         tem.append(rating)
         listarat.append(tem)
         if movieid in items:continue
         items.append(movieid)
         if user in users:continue
         users.append(user)
    cols=943#Size Movielens.
    rows=1682
    m=[] 
    #Crea la matriz inicial de ceros.
    matriz = numpy.ones((rows, cols)) * 0
    c=0
    #Carga los ratings en la matriz de ceros.
    for i in listarat:
        matriz[ int(i[1]) -1 ][ int(i[0]) -1 ] = int(i[2])
        c=c+1             
    print 'c', c
    #Save matrix.
    numpy.savetxt('/Users/xochilt/mf/matrices2/movielens-u3base.txt',matriz,fmt='%1.2f', delimiter=',')
    #Regresa la matriz y la lista de ratings de la matriz.
    return matriz,listarat

#Funcion para crear matrices iniciales para movielens-1m y 10m.
def mat1m():
    #Insertar los ratings.
    movies={}
    for line in open('movies.dat'):
         (id,title)=line.split('::')[0:2]
         movies[id]=id
    # Load data
    items=[]
    users=[]
    listarat=[]
    for line in open('ml-1m//train3.txt'):
         tem=[]
         (user,movieid,rating)=line.split()
         tem.append(user)
         tem.append(movieid)
         tem.append(rating)
         listarat.append(tem)
         if movieid in items:continue
         items.append(movieid)
         if user in users:continue
         users.append(user)
    cols=6040#Size dataset.
    rows=3952
    m=[] 
    #Crea la matriz inicial de ceros.
    matriz = numpy.ones((rows, cols)) * 0
    c=0
    for i in listarat:
        matriz[ int(i[1]) -1 ][ int(i[0]) -1 ] = int(i[2])
        c=c+1             
    
    print 'Total de ratings insertados: ', c
    #Guardar la matriz.
    numpy.savetxt('/Users/xochilt/mf/matrices2/movielens-r1base.txt',matriz,fmt='%1.2f', delimiter=',')
    #Regresa la matriz y la lista de ratings de la matriz.
    return matriz, listarat



#Funcion para crear las listas de Filmtrust.
#No crea la matriz para factorizar.
def filmtrust():
    items=[]
    users=[]
    listarat=[]
    for line in open('filmtrust//ratings-all.txt'):
     tem=[]
     (user,movieid,rating)=line.split('\t')
     tem.append(user)
     tem.append(movieid)
     tem.append(float(rating))
     listarat.append(tem)
     if movieid in items:continue
     items.append(movieid)
     if user in users:continue
     users.append(user)
     
    print 'ratings...'
    numpy.savetxt('/Users/xochilt/mf/matrices2/ratings.txt',matriz,fmt='%1.2f', delimiter=',')
    return listarat, users,items

#Funcion para hacer datasets de ml-1m y ml-10m, datasets train y test.
def moviedts(ini,end):
    movies={}
    for line in open('movies.dat'):
        (id,title)=line.split('::')[0:2]
        movies[id]=id
    items=[]
    users=[]
    listrain=[]
    for line in open('ml-1m//ratings.dat'):
        tem=[]
        (user,movieid,rating,ts)=line.split('::')
        tem.append(user)
        tem.append(movieid)
        tem.append(rating)
        listrain.append(tem)
        if movieid in items:continue
        items.append(movieid)
        if user in users:continue
        users.append(user)
    #Creando  datasets...
    listest=[]
    #Crea la lista de prueba en el rango ini,end.
    for j in  range(ini,end):
        print j
        listest.append(listrain[j])
    #eliminamos la lista de prueba del dataset inicial.
    #crea el dataset de entrenamiento. 
    for k in listest:
        if k in listrain:
            listrain.remove(k)
    #Devuelve el conjunto de datos de entrenamiento y de prueba.
    return listrain,listest
 
 
#Funcion para obtener el error RMSE y  MAE.
#Utiliza la matriz factorizada con los datos de prueba
#y la matriz test, las compara y obtiene el error.
def get_error(R,nR,users,items):
    sumarmse=0
    sumamae=0
    c=0.0
    print 'nuevos m x n...'
    for i in range(1,items):
        for j in range(1,users):
            if R[i-1][j-1]==0.0:continue
            rmsed = ((R[i-1][j-1])-(nR[i-1][j-1]))**2
            maed= fabs((R[i-1][j-1])-(nR[i-1][j-1]))
            c=c+1.0
            sumarmse=sumarmse+rmsed
            sumamae=sumamae+maed
    t=(sumarmse/c)
    rmse = sqrt(t)
    mae=sumamae/c
    print 'c',c
    #Devuelve el error calculado.
    return rmse,mae  

#funcion para salvar la matriz factorizada.
def savedata(matrix):
    numpy.savetxt('matrix.txt', matrix, delimiter=',', fmt='%1.3f')
    return

#Funcion para crear las matrices iniciales para factorizar con
#Music dataset.
def matmusic(music):
    items=[]
    #music es el dataset.
    for i in music:
        if i[1] in items:continue
        items.append(i[1])        

    items.sort()
    cols=42 #Size dataset.
    rows=len(items)
    #Crea la matriz inicial de cero.
    mat = numpy.ones((rows, cols)) * 0
    #Agregamos los ratings a la matriz inicial.
    for i in music:
        mat[i[1]-1][i[0]-1]=i[2]
        
    #Creando el diccionario para utilizarlo en las recomendaciones.
    pref = dict([(t[0],{}) for t in music])
    for t in music:
        pref[t[0]][t[1]]=float(t[2])
    #Devuelve las preferencias de los usuarios, la matriz de ratings.
    return pref,mat

