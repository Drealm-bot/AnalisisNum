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
