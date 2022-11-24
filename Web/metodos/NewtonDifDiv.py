import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

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
    print(type(tabla), type(titulo))
    return titulo, tabla, dDividida, polinomio, polisimple
#    # SALIDA
#    print('Tabla Diferencia Dividida')
#    print([titulo])
#    print(tabla)
#    print('dDividida: ')
#    print(dDividida)
#    print('polinomio: ')
#    print(polinomio)
#    print('polinomio simplificado: ' )
#    print(polisimple)
#
#    # Gráfica
#    plt.plot(xi,fi,'o', label = 'Puntos')
#    ##for i in range(0,n,1):
#    ##    plt.axvline(xi[i],ls='--', color='yellow')
#    plt.plot(pxi,pfi, label = 'Polinomio')
#    plt.legend()
#    plt.xlabel('xi')
#    plt.ylabel('fi')
#    plt.title('Diferencias Divididas - Newton')
#    plt.show()
#    return polisimple
#
#x = [-1,0,3,4,7]
#y = [15.5,3,8,1,9]
#NewtonDifDiv(x, y)