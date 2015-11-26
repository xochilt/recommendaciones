import numpy 

def mat():
    #Insertar los ratings.
    music={}
    movies={}
    #for line in open('movies.dat'):
       #(id,title)=line.split('::')[0:2]
    for line in open('u.item'):
     (id,title)=line.split('|')[0:2]
     movies[id]=id
    # Load data
    #prefs={}
    items=[]
    users=[]
    listarat=[]
    #for line in open('ml-1m//r1.base'):
    for line in open('u3.base'):
     tem=[]
     (user,movieid,rating,ts)=line.split('\t')
     #prefs.setdefault(user,{})
     #prefs[user][movies[movieid]]=float(rating)
     tem.append(user)
     tem.append(movieid)
     tem.append(rating)
     listarat.append(tem)
     if movieid in items:continue
     items.append(movieid)
     if user in users:continue
     users.append(user)
    cols=943
    rows=1682
    m=[] 
    matriz = numpy.ones((rows, cols)) * 0
    print 'matriz', matriz
    print 'items',len(matriz)
    print 'users',len(matriz[0])
    c=0
    for i in listarat:
        matriz[ int(i[1]) -1 ][ int(i[0]) -1 ] = int(i[2])
        #print  'pos1', 'pos2', int(i[1]) -1 , int(i[0]) -1 , 'rating:', float(i[2])
        c=c+1             
    print 'c', c
    print 'trabajando con u3.base...'
    numpy.savetxt('/Users/xochilt/mf/matrices2/movielens-u3base.txt',matriz,fmt='%1.2f', delimiter=',')
    return matriz,items,users, listarat



def mat1m():
    #Insertar los ratings.
    # music={}
    # movies={}
    # for line in open('movies.dat'):
    #  #print line
    #  (id,title)=line.split('::')[0:2]
    #  movies[id]=id
    # # Load data
    #prefs={}
    items=[]
    users=[]
    listarat=[]
    for line in open('filmtrust//ratings-all.txt'):
     tem=[]
     #print line

     (user,movieid,rating)=line.split('\t')
     #(user,movieid,rating,ts)=line.split('::')   #\t')
     #prefs.setdefault(user,{})
     #prefs[user][movies[movieid]]=float(rating)
     tem.append(user)
     tem.append(movieid)
     tem.append(float(rating))
     listarat.append(tem)
     if movieid in items:continue
     items.append(movieid)
     if user in users:continue
     users.append(user)
    # cols=71567#6040
    # rows=65133#10681#3952
    # m=[] 
    # matriz = numpy.ones((rows, cols)) * 0
    # print 'items',len(matriz)
    # print 'users',len(matriz[0])
    # c=0
    # for i in listarat:
    #     print i
    #     matriz[ int(i[1]) -1 ][ int(i[0]) -1 ] = int(i[2])
    #     #print  'pos1', 'pos2', int(i[1]) -1 , int(i[0]) -1 , 'rating:', float(i[2])
    #     c=c+1             
    # print 'c', c
    print 'ratings..10m...'
    #numpy.savetxt('/Users/xochilt/mf/matrices2/movielens-10m.txt',matriz,fmt='%1.2f', delimiter=',')
    return listarat, users,items #matriz,items,users, listarat




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

    print 'listrain', len(listrain)

    print 'creando  datasets...'
    listest=[]

    for j in  range(ini,end):
        print j
        listest.append(listrain[j])
    
    #eliminamos de la lista

    print 'crear el train.' 
    for k in listest:
        if k in listrain:
            listrain.remove(k)

    print 'len listrain', len(listrain)
    print 'len listest', len(listest)

    return listrain,listest
 




import math
from math import *
import decimal
def get_error(R,nR,users,items):
    sumarmse=0
    sumamae=0
    c=0.0
    print 'nuevos m x n...'
    for i in range(1,items):
        for j in range(1,users):
            if R[i-1][j-1]==0.0:continue
            rmsed = ((R[i-1][j-1])-(nR[i-1][j-1]))**2
            # print R[i-1][j-1], nR[i-1][j-1]
            # print 'rmse',rmsed
            
            maed= fabs((R[i-1][j-1])-(nR[i-1][j-1]))
            c=c+1.0
            # print R[i-1][j-1],nR[i-1][j-1]
            # print 'maed', format(maed, '.5f')
            
            sumarmse=sumarmse+rmsed
            sumamae=sumamae+maed
            
    t=(sumarmse/c)
    rmse = sqrt(t)

    mae=sumamae/c

    print 'mae:', mae 
    print 'rmse:', rmse
    print 'c',c

    return rmse,mae  


def savedata(matrix):
    import numpy
    numpy.savetxt('matrix.txt', matrix, delimiter=',', fmt='%1.3f')
    return


def matmusic(music):
    items=[]
    for i in music:
        if i[1] in items:continue
        items.append(i[1])        

    items.sort()
    cols=42
    rows=len(items)

    mat = numpy.ones((rows, cols)) * 0

    for i in music:
        mat[i[1]-1][i[0]-1]=i[2]
    
        
    #Creando el diccionario para utilizarlo en las recomendaciones.
    pref = dict([(t[0],{}) for t in music])
    for t in music:
        pref[t[0]][t[1]]=float(t[2])
    

    return pref,mat,items


def matmovie(movie):
    items=[]
    for i in movie:
        if i[1]  in items:continue
        items.append(i[1])        

    items.sort()
    cols=943
    rows=1682

    mat = numpy.ones((rows, cols)) * 0

    for i in movie:
        mat[i[1]-1][i[0]-1]=i[2]
    
        
    #Creando el diccionario para utilizarlo en las recomendaciones.
    pref = dict([(t[0],{}) for t in movie])
    for t in movie:
        pref[t[0]][t[1]]=float(t[2])
                    
    return pref,mat,items
