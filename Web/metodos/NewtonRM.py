import pandas as pd
import numpy as np
import sympy as sy
import math


#import wdb
#wdb.set_trace()
#2*(1/(sin(x)^2 + 1))*(sin(x)*cos(x))
#2*(1/(math.sin(x)**2 + 1))*(math.sin(x)*math.cos(x))
"""print("x0:")
x0 = float(input())
print("tol:")
tol = float(input())
print("niter:")
niter = float(input())
print("function:")
fun = input()
print("derivate function df:")
df = input()
print("second derivate function df:")
df2 = input()"""

def newtonRM(x0, tol, niter, fun, df, df2):
    fn=[]
    xn=[]
    E=[]
    n=[]
    dfn=[]
    dfn2=[]
    x0=float(x0)
    tol=float(tol)
    niter=float(niter)
    x=x0
    f=eval(fun)
    derivada=eval(df)
    derivada2=eval(df2)
    c=0
    Error=100               
    fn.append(f)
    dfn.append(derivada)
    dfn2.append(derivada2)
    xn.append(x)
    E.append(Error)
    n.append(c)
    while Error>tol and f!=0 and derivada!=0  and c<niter:
        x=x-(f*derivada/((derivada**2)-f*derivada2))
        derivada=eval(df)
        derivada2=eval(df2)
        f=eval(fun)
        fn.append(f)
        dfn.append(derivada)
        dfn2.append(derivada2)
        xn.append(x)
        c=c+1
        Error=abs(xn[c]-xn[c-1])
        n.append(c)
        E.append(Error)
    if f==0:
        s=x
        print(s,"es raiz de f(x)")
        print("N",n)
        print("xn",xn)
        print("fn",fn)
        print("Error",E)
    elif Error<tol:
        s=x
        print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", tol)
        print("N",n)
        print("xn",xn)
        print("fn",fn)
        print("Error",E)
    else:
        s=x
        print("Fracaso en ",niter, " iteraciones ") 
    return n, xn, fn, E

"""result = newtonRM(1, 1e-7, 100, "math.exp(x)-x-1", "math.exp(x)-1", "math.exp(x)")
print(result)
print(type(result))"""


