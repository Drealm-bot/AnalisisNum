import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()

"""print("x0:")
x0 = float(input())
print("tol:")
tol = float(input())
print("niter:")
niter = float(input())
print("function f:")
f = input()
print("function g:")
g = input()"""
def punto_fijo(x0, tol, niter, f, g):	
        n=[]
        xn=[]
        fn=[]
        gn=[]
        E=[]
        x0=float(x0)
        tol=float(tol)
        niter=float(niter)
        x=x0
        xn.append(x)
        fx0=eval(f)
        gx0=eval(g)
        c=0
        Error=100 
        n.append(c)
        gn.append(gx0)              
        fn.append(fx0)
        E.append(Error)

        while Error>tol and f!=0 and c<niter:
                x=eval(g)
                xn.append(x)
                fi=eval(f)
                fn.append(fi)
                gi=eval(g)
                gn.append(gi)        	
                c=c+1
                n.append(c)	
                Error=abs(xn[c]-xn[c-1])	
                E.append(Error)	
        if fi==0:
            s=x
            print(s,"es raiz de f(x)")
            print("n",n)
            print("xn",xn)
            print("fn",fn)
            print("gn",gn)
            print("Error",E)
        elif Error<tol:
            s=x
            print(s,"es una aproximacion de un raiz de f(x) con una tolerancia de", tol)
            print("n",n)
            print("xn",xn)
            print("fn",fn)
            print("gn",gn)
            print("Error",E)
        else:
            s=x
            print("Fracasó en ",niter, " iteraciones ") 
        return n, xn, fn, gn, E
    

"""result = punto_fijo(-0.5, 1e-7, 100, "math.log(math.sin(x)**2 + 1)-(1/2)-x", "math.log(math.sin(x)**2 + 1)-(1/2)")
print(result)
print(type(result))
"""
