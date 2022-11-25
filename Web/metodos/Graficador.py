import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import math

def graficador(polinomio):
    x = np.arange(-100, 101, 5)
    #x = [-1,0,1,3,4]
    #y = x+1
    yi = []
    yi = eval(polinomio)
    print(yi)
    plt.plot(x, yi)
    plt.title(polinomio)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show
    plt.savefig("Web/static/grafica.png")
    plt.clf()
    grafica = os.path.join("/Web","/static", 'grafica.png')
    return grafica

def graficadorInt(polinomio, xi,fi,xin,yin):
    plt.plot(xi,fi,'o', label='[xi,fi]')
    plt.plot(xin,yin, label='p(x)')
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.legend()
    plt.title(polinomio)
    plt.show()
    plt.savefig("Web/static/grafica.png")
    plt.clf()
    grafica = os.path.join("/Web","/static", 'grafica.png')
    return grafica
