import pandas as pd
import numpy as np
import math
import copy


def sustreg(Ab,n):
	x=np.zeros(n)
	x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
	for i in range(n-2,-1,-1):
		sum=0
		for p in range(i+1,n):
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



#A=np.array([[1, -3, -5],[5, 7, -9],[-10, 4, 7]], dtype='float64')
#n=len(A)
#b=np.array(([[15],[-20],[-15]]), dtype='float64')
#Piv=0
#Ab=np.zeros((3,4))
#Ab=np.concatenate((A, b), axis = 1)
#mark=list(range(n))

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

