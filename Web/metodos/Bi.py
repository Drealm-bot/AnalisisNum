import math
import pandas as pd
import numpy as np
import math

#print("X0:")
#X0 = float(input())
#print("Delta:")
#Delta = float(input())
#print("Niter:")
#Niter = float(input())
#print("Function:")
#Fun = input()
def bi(X0, Delta, Niter, Fun):
        X0 = float(X0)
        Delta = float(Delta)
        Niter = float(Niter)
        x=X0
        f0=eval(Fun)

        if f0==0:
                s=x
                print(X0, "es raiz de f(x)")
        else:
                X1=X0+Delta
                x=X1
                c=1
                f1=eval(Fun)
                while f0*f1>0 and c<Niter:
                    X0=X1
                    f0=f1
                    X1=X0+Delta
                    x=X1                 
                    f1=eval(Fun)
                    c=c+1
                if f1==0:
                    s=x
                    result = (X1,"es raiz de f(x)")
                elif f0*f1<0:
                    s=x
                    result = ("Existe una raiz de f(x) entre ",X0," y ",X1)
                else:
                    s=x
                    result = ("Fracaso en ",Niter, " iteraciones ") 
        return result
