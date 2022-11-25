import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from  .Graficador import *

def vander(xi, B, n, nit):

    D = np.zeros(shape=(n,n),dtype ='float64')
    for i in range(0,n,1):
        for j in range(0,n,1):
            potencia = (n-1)-j 
            D[i,j] = xi[i]**potencia
    coeficiente = np.linalg.solve(D,B)

    x = sym.Symbol('x')
    polinomio = 0
    for i in range(0,n,1):
        potencia = (n-1)-i
        termino = coeficiente[i]*(x**potencia)
        polinomio = polinomio + termino
    px = sym.lambdify(x,polinomio)
    a = np.min(xi)
    b = np.max(xi)
    xin = np.linspace(a,b,nit)
    yin = px(xin)
    grafica = graficadorInt(polinomio, xi, B, xin, yin)

    return D, coeficiente, polinomio, grafica

def lagi(xi, fi):
    
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador
        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    polisimple = polinomio.expand()

    px = sym.lambdify(x,polisimple)

    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)
    grafica = graficadorInt(polinomio, xi, fi, pxi, pfi)

    return fi, divisorL, polinomio, polisimple, grafica

def NewtonDifDiv(x, y):
    xi = np.array(x)
    fi = np.array(y)

    
    n = len(xi)
    titulo = ["i   ","xi  ","fi  "]
    ki = np.arange(0,n,1)
    tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
    tabla = np.transpose(tabla)

    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)

    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    while (j < m):
        titulo.append('F['+str(j-2)+']')

        i = 0
        paso = j-2
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    dDividida = tabla[0,3:]
    n = len(dfinita)

    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1,n,1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor

    polisimple = polinomio.expand()

    px = sym.lambdify(x,polisimple)

    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)
    grafica = graficadorInt(polinomio, xi, fi, pxi, pfi)

    return titulo, tabla, dDividida, polinomio, polisimple, grafica

def Spline(x,y,d):
    n=len(x)
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
        c=0
        for i in range(1, n):
            A[h][c]=cua[i]
            A[h][c+1]=x[i]
            A[h][c+2]=1
            b[h]=y[i]
            c=c+3
            h=h+1
        c=0
        for i in range(1, n-1):
            A[h][c]=2*x[i]
            A[h][c+1]=1
            A[h][c+3]=-2*x[i]
            A[h][c+4]=-1
            b[h]=0
            c=c+4
            h=h+1
        A[h][0]=2
        b[h]=0
        
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
    Tabla=np.reshape(val,(d+1,n-1),'F')
    Tabla=np.transpose(Tabla)
    return Tabla