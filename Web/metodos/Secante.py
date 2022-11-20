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
print("x1:")
x1 = float(input())
print("tol:")
tol = float(input())
print("niter:")
niter = float(input())
print("function:")
fun = input()"""

def secante(x0, x1, tol, niter, fun): 
    fn=[]
    xn=[]
    E=[]
    n=[]
    x0=float(x0)
    x1=float(x1)
    tol=float(tol)
    niter=float(niter)
    xc=x0
    x=xc
    fxc=eval(fun)
    c=0
    Error=100               
    fn.append(fxc)
    xn.append(x)
    E.append(Error)
    n.append(c)
    xb=x1
    x=xb
    fxb=eval(fun)
    c=c+1              
    fn.append(fxb)
    xn.append(x)
    E.append(Error)
    n.append(c)
    while Error>tol and fxb!=0 and fxc!=0 and c<niter:
        xa=xb-fxb*((xb-xc)/(fxb-fxc))
        x=xa
        f=eval(fun)
        fn.append(f)
        xn.append(xa)
        c=c+1
        xc=xb
        x=xc
        fxc=eval(fun)
        xb=xa  
        x=xb
        fxb=eval(fun)  
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

"""result = secante(0.5,1, 1e-7, 100, "math.log(math.sin(x)**2 + 1)-(1/2)")
print(result)
print(type(result))
"""