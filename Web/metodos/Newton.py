
import pandas as pd
import numpy as np
import math
from sympy import *
#import wdb
#wdb.set_trace()
x = Symbol('x', real=true)
print("X0:")
X0 = float(input())
print("Tol:")
Tol = float(input())
print("Niter:")
Niter = float(input())

print("Function:")
Fun = input()

fn=[]
xn=[]
E=[]
N=[]
x1=X0
f=eval(Fun)
derivada=f.diff(x)
f = f.subs(x, x1)
derivada = derivada.subs(x, x1)
c=0
Error=100               
fn.append(f)
xn.append(x1)
E.append(Error)
N.append(c)
while Error>Tol and f!=0 and derivada!=0  and c<Niter:
  x1=x1-f/derivada
  derivada=f.diff(x)
  f=eval(Fun)
  fn.append(f)
  xn.append(x1)
  c=c+1
  Error=abs(xn[c]-xn[c-1])
  N.append(c)
  E.append(Error)
if f==0:
    s=x1
    print(s,"es raiz de f(x)")
elif Error<Tol:
    s=x1
    print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
    print("N",N)
    print("xn",xn)
    print("fn",fn)
    print("Error",E)
else:
    s=x1
    print("Fracaso en ",Niter, " iteraciones ") 


