import pandas as pd
import numpy as np
import math
import copy

def jacobi_seid(x0, A, b, Tol, niter, met, n):
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