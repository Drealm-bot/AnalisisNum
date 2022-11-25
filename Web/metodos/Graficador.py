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
    print("polinomi")
    print(polinomio)
    print(yi)
    #print(y)
    print(type(yi))
    #print(type(y))
    print('Values of x: ', x)
    print('Values of y: ', yi)
    plt.plot(x, yi)
    plt.title("Identity Function")
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.show
    plt.savefig("grafica.png")
    plt.clf()
    grafica = os.path.join('grafica.png')
    return grafica
