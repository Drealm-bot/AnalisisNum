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
df = input()"""
def newton_raphson(x0, tol, niter, fun, df):
    fn=[]
    xn=[]
    E=[]
    n=[]
    x0=float(x0)
    tol=float(tol)
    niter=float(niter)
    x=x0
    f=eval(fun)
    derivada=eval(df)
    c=0
    Error=100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    n.append(c)
    while Error>tol and f!=0 and derivada!=0  and c<niter:
        x=x-f/derivada
        derivada=eval(df)
        f=eval(fun)
        fn.append(f)
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

"""result = newton_raphson(0.5, 1e-7, 100, "math.log(math.sin(x)**2 + 1)-(1/2)", "2*(1/(math.sin(x)**2 + 1))*(math.sin(x)*math.cos(x))")
print(result)
print(type(result))"""
