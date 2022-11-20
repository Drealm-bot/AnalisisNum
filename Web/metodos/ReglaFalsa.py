import pandas as pd
import numpy as np
import math
from beautifultable import BeautifulTable
#import wdb
#wdb.set_trace()

"""print("a:")
a = float(input())
print("b:")
b = float(input())
print("tol:")
tol = float(input())
print("niter:")
niter = float(input())
print("function:")
fun = input()
"""


def regla_falsa(a, b, tol, niter, fun):		
	an=[]
	bn=[]
	n=[]
	m=[]
	fm=[]
	E=[]
	a=float(a)
	b=float(b)
	tol=float(tol)
	niter=float(niter)
	x=a
	fa=eval(fun)
	x=b
	fb=eval(fun)

	if fa==0:
		s=a
		E=0
		print(a, "es raiz de f(x)")
	elif fb==0:
		s=b
		E=0
		print(b, "es raiz de f(x)")
	elif fb*fa<0:
		c=0
		n.append(c+1)
		xm=b-((fb*(b-a))/(fb-fa))
		x=xm                 
		fmi=eval(fun)
		an.append(a)
		bn.append(b)
		m.append(x)
		fm.append(fmi)
		E.append(100)
		while E[c]>tol and fmi!=0 and c<niter:
			if fa*fmi<0:
					b=xm
					x=b                 
					fb=eval(fun)
			else:
					a=xm
					x=a
					fa=eval(fun)
			xa=xm
			xm=b-((fb*(b-a))/(fb-fa))
			x=xm 
			an.append(a)
			bn.append(b)
			m.append(x)
			fmi=eval(fun)
			fm.append(fmi)
			Error=abs(xm-xa)
			E.append(Error)
			c=c+1
			n.append(c+1)
		if fmi==0:
			s=x
			print(s,"es raiz de f(x)")
			print("n",n)
			print("a",an)
			print("b",bn)
			print("m",m)
			print("Fm",fm)
			print("Error",E)
		elif Error<tol:
			s=x
			print(s,"es una aproamacion de un raiz de f(x) con una tolerancia", tol)
			print("n",n)
			print("a",an)
			print("b",bn)
			print("m",m)
			print("Fm",fm)
			print("Error",E)
		else:
				s=x
				print("Fracaso en ",niter, " iteraciones ") 
	else:
		print("El intervalo es inadecuado")
	return n, an, bn, m, fm, E

