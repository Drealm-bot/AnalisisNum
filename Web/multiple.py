from flask import Blueprint, render_template, request
import numpy as np

multiple = Blueprint('multiple', __name__)

from .metodos.Multiples import *

def gauss_form(x, mark, Ab):
    return f'Ab = {Ab} \nMark = {mark} \nX = {x}'

def LU_form(x, L, U):
    return f'L = {L} \nU = {U} \nX = {x}'

@multiple.route('/gauss-sim', methods=['GET', 'POST'])
def gauss_sim():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))

        result = gaussSim(a, b, size,0)
        return render_template("gauss_sim.html", x = result[0], Ab = result[2], n = size, bol = 1)
    else:
        return render_template("gauss_sim.html", bol = 0)

@multiple.route('/gauss-par', methods=['GET', 'POST'])
def gauss_par():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))

        result = gaussSim(a, b, size,1)
        return render_template("gauss_par.html", x = result[0], Ab = result[2], n = size, bol = 1)
    else:
        return render_template("gauss_par.html", bol = 0)

@multiple.route('/gauss-tot', methods=['GET', 'POST'])
def gauss_tot():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))

        result = gaussSim(a, b, size,2)
        return render_template("gauss_tot.html", x = result[0], mark = result[1], Ab = result[2], n = size, bol = 1)
    else:
        return render_template("gauss_tot.html", bol = 0)

@multiple.route('/LU-sim', methods=['GET', 'POST'])
def LU_sim():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = LU(a, b, size, 0)
        return render_template("LU_sim.html", x=result[0], L = result[1], U = result[2], size = str(size), bol = 1)
    else:
        return render_template("LU_sim.html", bol = 0)

@multiple.route('/LU-par', methods=['GET', 'POST'])
def LU_par():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = LU(a, b, size, 1)
        return render_template("LU_par.html", x=result[0], L = result[1], U = result[2], size = str(size), bol = 1)
    else:
        return render_template("LU_par.html", bol = 0)

@multiple.route('/LU-little', methods=['GET', 'POST'])
def LU_little():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = dirLU(a, b, size, 0)
        return render_template("LU_little.html", L = result[0], U = result[1], x = result[2], size = str(size), bol = 1)
    else:
        return render_template("LU_little.html", bol = 0)

@multiple.route('/LU-crout', methods=['GET', 'POST'])
def LU_crout():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = dirLU(a, size, 1)
        return render_template("LU_crout.html", L = result[0], U = result[1], x = result[2], size = str(size), bol = 1)
    else:
        return render_template("LU_crout.html", bol = 0)

@multiple.route('/LU-cholesky', methods=['GET', 'POST'])
def LU_cholesky():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = dirLU(a, size, 2)
        return render_template("LU_cholesky.html", L = result[0], U = result[1], x = result[2], size = str(size), bol = 1)
    else:
        return render_template("LU_cholesky.html", bol = 0)

@multiple.route('/jacobi-seidel', methods=['GET', 'POST'])
def jacobi_seidel():
    if request.method == 'POST':
        size = int(request.form.get('size'))
        met = int(request.form.get('met'))
        tol = float(request.form.get('tol'))
        niter = int(request.form.get('niter'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        x0 = np.array(request.form.get('x0'), dtype='float64')
        for i in range(size-1):
            x0 = np.append(x0, float(request.form.get('x'+str(i+1))))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = jacobi_seid(x0, a, b, tol, niter, met, size, 0)
        return render_template("jacobi_seidel.html", T=result[0], C=result[1], niter = result[2], sol = result[3], E = result[4], bol = 1, size=np.size(result[0]))
    else:
        return render_template("jacobi_seidel.html", bol = 0)

@multiple.route('/sor', methods=['GET', 'POST'])
def sor():
    if request.method == 'POST':
        size = int(request.form.get('size'))
        rel = int(request.form.get('rel'))
        tol = float(request.form.get('tol'))
        niter = int(request.form.get('niter'))

        a = np.array(request.form.getlist('A0'), dtype='float64')
        for i in range(size-1):
            a = np.append(a, np.asarray(request.form.getlist('A'+str(i+1)), dtype='float64'))

        x0 = np.array(request.form.get('x0'), dtype='float64')
        for i in range(size-1):
            x0 = np.append(x0, float(request.form.get('x'+str(i+1))))

        b = np.array(request.form.get('b0'), dtype='float64')
        for i in range(size-1):
            b = np.append(b, float(request.form.get('b'+str(i+1))))
        
        result = jacobi_seid(x0, a, b, tol, niter, 2, size, rel)
        return render_template("jacobi_seidel.html", T=result[0], C=result[1], niter = result[2], sol = result[3], E = result[4], bol = 1, size=np.size(result[0]))
    else:
        return render_template("jacobi_seidel.html", bol = 0)