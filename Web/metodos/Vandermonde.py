# El polinomio de interpolación
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def vander(xi, B, n, nit):
    print(B)
    D = np.zeros(shape=(n,n),dtype ='float64')
    print(D)
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

    return D, coeficiente, polinomio

#sym.pprint(polinomio)
#
## Grafica
#plt.plot(xi,fi,'o', label='[xi,fi]')
#plt.plot(xin,yin, label='p(x)')
#plt.xlabel('xi')
#plt.ylabel('fi')
#plt.legend()
#plt.title(polinomio)
#plt.show()