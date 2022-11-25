import pandas as pd
import numpy as np
import math
import copy


def sustpro(Ab, n):
    x=np.zeros((n,1),dtype='float64')
    x[0]=Ab[0][n]/Ab[0][0]
    for i in range(1,n):
        sum=0
        for p in range(i):
            sum = sum + Ab[i][p]*x[p]
        x[i]=(Ab[i][n]-sum)/Ab[i][i]
    return x

def sustreg(Ab,n):
	x=np.zeros((n,1), dtype='float64')
	x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
	for i in range(n-2,-1,-1):
		sum=0
		for p in range(i,n):
			sum=sum+Ab[i][p]*x[p]
		x[i]=(Ab[i][n]-sum)/Ab[i][i]
	return x

def pivpar(Ab, n, k):
	mayor=abs(Ab[k][k])
	maxrow=k
	for s in range(k+1,n):
		if abs(Ab[s][k])>mayor:
			mayor = abs(Ab[s][k])
			maxrow = s
	if mayor==0:
		NotImplemented
	elif maxrow!=k:
		aux=copy.deepcopy(Ab[k])
		Ab[k]=Ab[maxrow]
		Ab[maxrow]=aux
	return Ab

def pivtot(Ab, mark, n, k):
	mayor = 0
	maxrow = k
	maxcolumn = k
	for r in range(k, n):
		for c in range(k, n):
			if abs(Ab[r][c])>mayor:
				mayor = Ab[r][c]
				maxrow = r
				maxcolumn = c
	if mayor==0:
		NotImplemented
	else:
		if maxrow!=k:
			aux = copy.deepcopy(Ab[k])
			Ab[k]=Ab[maxrow]
			Ab[maxrow]=aux
		if maxcolumn!=k:
			aux = copy.deepcopy(Ab[:][k])
			Ab[:][k] = Ab[:][maxcolumn]
			Ab[:][maxcolumn] = aux
			aux2 = copy.deepcopy(mark[k])
			mark[k] = mark[maxcolumn]
			mark[maxcolumn] = aux2
	return Ab, mark


def gaussSim(A, b, size, piv):
	n=size
	mode=piv
	Ab=np.zeros((n,n+1))
	Ab=np.concatenate((np.split(A, n), np.split(b, n)), axis = 1, dtype='float64')
	mark=list(range(n))

	for k in range(0,n-1):
		if mode==1:
			Ab = pivpar(Ab,n,k)
		elif mode==2:
			Ab, mark = pivtot(Ab, mark, n, k)
		for i in range(k+1,n):
			M=Ab[i][k]/Ab[k][k]
			for j in range(k,n+1):
				Ab[i][j]=Ab[i][j]-M*Ab[k][j]
	x=sustreg(Ab,n)

	return x, mark, Ab

def pivLU(A, P, n, k):
    mayor=abs(A[k][k])
    maxrow=k 
    for s in range(k,n):
        if abs(A[s][k])>mayor:
            mayor=abs(A[s][k]) 
            maxrow=s
    if mayor==0:
       print('El sistema no tiene solución única')
    elif maxrow!=k:
        aux=copy.deepcopy(A[k])
        auxP=copy.deepcopy(P[k])
        A[k]=A[maxrow]
        P[k]=P[maxrow]
        A[maxrow]=aux 
        P[maxrow]=auxP 
    return A, P


def LU(A,b,n,met):
    P=np.eye(n,dtype='float64')
    L=copy.deepcopy(P)
    A=np.split(A,n)
    b=np.split(b,n)
    for k in range(0,n-1):
        if met == 1:
            A, P = pivLU(A,P,n,k)
        for i in range(k+1, n):
            M=A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j]=A[i][j]-M*A[k][j]
                
            A[i][k]=M
    U=np.triu(A)
    L=L+np.tril(A,-1)
    LB=np.concatenate((L,b),axis = 1,dtype='float64')
    print(LB)
    z = sustpro(LB,n)
    Uz=np.concatenate((U,z),axis = 1,dtype='float64')
    x = sustreg(Uz,n)
    return x, L, U

def dirLU(A, b, n, met):
    P=np.eye(n, dtype='float64')
    U=copy.deepcopy(P)
    L=copy.deepcopy(P)
    A=np.split(A,n)
    b=np.split(b,n)
    for k in range(n):
        sum1=0
        for p in range(k):
            sum1=sum1+L[k][p]*U[p][k]
        if met==0:
            U[k][k]=(A[k][k]-sum1)/L[k][k]
        elif met==1:
            L[k][k]=(A[k][k]-sum1)/U[k][k]
        else:
            U[k][k]=math.sqrt(A[k][k]-sum1)
            L[k][k]=U[k][k]
        for i in range(k+1,n):
            sum2=0
            for p in range(k):
                sum2=sum2+L[i][p]*U[p][k]
            L[i][k]=(A[i][k]-sum2)/U[k][k]
        for j in range(k+1,n):
            sum3=0
            for p in range(k):
                sum3=sum3+L[k][p]*U[p][j]
            U[k][j]=(A[k][j]-sum3)/L[k][k]
    LB=np.concatenate((L,b),axis = 1,dtype='float64')
    print(LB)
    z = sustpro(LB,n)
    Uz=np.concatenate((U,z),axis = 1,dtype='float64')
    x = sustreg(Uz,n)
    return L, U, x

def jacobi_seid(x0, A, b, Tol, niter, met, n, w):
    c=0
    error=Tol+1
    A=np.asmatrix(np.split(A,n), dtype='float64')
    b=np.asmatrix(np.split(b,n), dtype='float64')
    x0=np.asmatrix(np.split(x0,n), dtype='float64')
    D=np.diag(np.diag(A))
    L=-np.tril(A,-1)
    U=-np.triu(A,+1)
    nit = []
    sol = []
    Err = []
    E = [0]
    if met==0:
        T=np.dot(np.linalg.inv(D),(L+U))
        C=np.dot(np.linalg.inv(D),b)
    if met==1:
        T=np.dot(np.linalg.inv(D-L),(U))
        C=np.dot(np.linalg.inv(D-L),b)
    if met==2:
        T=np.dot(np.linalg.inv(D-(w*L)),(((1-w)*D)+(w*U)))
        C=w*np.dot(np.linalg.inv(D-(w*L)),b)
    spectralrad = max(abs(np.linalg.eigvals(T)))
    while error>Tol and c<niter:
        x1=np.dot(T,x0)+C
        E.append(np.linalg.norm(x1-x0, np.inf))
        error=copy.deepcopy(E[c+1])
        Err.append(error)
        nit.append(c)
        sol.append(x1)
        x0=copy.deepcopy(x1)
        print(Err, nit, sol, E)
        c=c+1
    sol = np.transpose(sol)
    if error < Tol:
        s=x0
        n=c
        s
        print('es una aproximación de la solución del sistmea con una tolerancia=',Tol)
        return T,C,nit, np.transpose(sol), Err
    else:
        s=x0
        n=c
        print('Fracasó en iteraciones',niter) 