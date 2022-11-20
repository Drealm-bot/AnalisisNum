import math
import pandas as pd
import numpy as np
import math

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

def biseccion(a, b, tol, niter, fun): 
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
	fa = eval(fun)
	x=b
	fb = eval(fun)

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
		xm=(a+b)/2
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
				fb=eval(fun)
			xa=xm
			xm=(a+b)/2
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
