import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


"""xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])"""
"""xi = [-1,0,1,3,4]
fi = [15.5,3,7.5,8,1]"""
def Lagrange(xi, fi, n):
    # PROCEDIMIENTO
    # Polinomio de Lagrange
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

    return fi, divisorL, polinomio, polisimple

    ## SALIDA
    #print('    valores de fi: ',fi)
    #print('divisores en L(i): ',divisorL)
    #print()
    #print('Polinomio de Lagrange, expresiones')
    #print(polinomio)
    #print()
    #print('Polinomio de Lagrange: ')
    #print(polisimple)
#
    ## Gráfica
    #plt.plot(xi,fi,'o', label = 'Puntos')
    #plt.plot(pxi,pfi, label = 'Polinomio')
    #plt.legend()
    #plt.xlabel('xi')
    #plt.ylabel('fi')
    #plt.title('Interpolación Lagrange')
    #plt.show()
    #return polisimple
#