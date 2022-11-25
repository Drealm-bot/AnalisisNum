import numpy as np
#Spline: Calcula los coeficienetes de los polinomios de interpolación de
# grado d (1, 2, 3) para el conjunto de n datos (x,y), 
# mediante el método spline.
def Spline(x,y,d):
    n=len(x)
    print(n)
    siz=(d+1)*(n-1)
    A=np.zeros((siz,siz))
    b=np.zeros((siz,1))
    cua=np.power(x,2)
    cub=np.power(x,3)
    
    # lineal
    if d==1:
        c=0
        h=0
        for i in range(0, n-1):
            A[i][c]=x[i]
            A[i][c+1]=1
            b[i]=y[i]
            c=c+2
            h=h+1
        c=0

        for i in range(1, n):
            A[h][c]=x[i]
            A[h][c+1]=1
            b[h]=y[i]
            c=c+2
            h=h+1

    # Cuadratic
    elif d==2:
        c=0
        h=0
        for i in range(0, n-1):
            A[h][c]=cua[i]
            A[i][c+1]=x[i]
            A[i][c+2]=1
            b[i]=y[i]
            c=c+3
            h=h+1
        print(A)
        c=0
        for i in range(1, n):
            A[h][c]=cua[i]
            A[h][c+1]=x[i]
            A[h][c+2]=1
            b[h]=y[i]
            c=c+3
            h=h+1
        print(A)
        c=0
        for i in range(1, n-1):
            A[h][c]=2*x[i]
            A[h][c+1]=1
            A[h][c+3]=-2*x[i]
            A[h][c+4]=-1
            b[h]=0
            c=c+4
            h=h+1
        print(A)
        A[h][0]=2
        b[h]=0
        print(A)
        
  # Cubic
    elif d==3:
        c=0
        h=0
        for i in range(0, n-1):
            A[i][c]=cub[i]
            A[i][c+1]=cua[i]
            A[i][c+2]=x[i]
            A[i][c+3]=1
            b[i]=y[i]
            c=c+4
            h=h+1
         
        c=0
        for i in range(1, n):
            A[h][c]=cub[i]
            A[h][c+1]=cua[i]
            A[h][c+2]=x[i]
            A[h][c+3]=1
            b[h]=y[i]
            c=c+4
            h=h+1
         
        c=0
        for i in range(1, n-1):
            A[h][c]=3*cua[i]
            A[h][c+1]=2*x[i]
            A[h][c+2]=1
            A[h][c+4]=-3*cua[i]
            A[h][c+5]=-2*x[i]
            A[h][c+6]=-1
            b[h]=0
            c=c+4
            h=h+1
         
        c=0
        for i in range(1, n-1):
            A[h][c]=6*x[i]
            A[h][c+1]=2
            A[h][c+4]=-6*x[i]
            A[h][c+5]=-2
            b[h]=0
            c=c+4
            h=h+1
         
        A[h][0]=6*x[0]
        A[h][1]=2
        b[h]=0
        h=h+1
        A[h][c]=6*x[-1]
        A[h][c+1]=2
        b[h]=0

    
    val=np.dot(np.linalg.inv(A),b)
    #print(np.linalg.inv(A))
    Tabla=np.reshape(val,(d+1,n-1),'F')
    print(Tabla)
    Tabla=np.transpose(Tabla)
    print(Tabla)
    print("Tracers")
    print(Tabla)
    return Tabla

x = [-1,0,3,4]
y = [15.5,3,8,1]
d=2
Spline(x,y,d)