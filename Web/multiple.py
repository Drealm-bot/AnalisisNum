from flask import Blueprint, render_template, request
import numpy as np

multiple = Blueprint('multiple', __name__)

from .metodos.gausspiv import *
from .metodos.LU import *

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

        x, mark, Ab = gaussSim(a, b, size,0)
        result = gauss_form(x, mark, Ab)
        return render_template("gauss_sim.html", resultado = str(result))
    else:
        return render_template("gauss_sim.html")

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

        x, mark, Ab = gaussSim(a, b, size,1)
        result = gauss_form(x, mark, Ab)
        return render_template("gauss_par.html", resultado = str(result))
    else:
        return render_template("gauss_par.html")

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

        x, mark, Ab = gaussSim(a, b, size,2)
        result = gauss_form(x, mark, Ab)
        return render_template("gauss_tot.html", resultado = str(result))
    else:
        return render_template("gauss_tot.html")

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
        return render_template("LU_sim.html", x=result[0], L = result[1], U = result[2], size = str(size))
    else:
        return render_template("LU_sim.html")

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
        return render_template("LU_par.html", x=result[0], L = result[1], U = result[2], size = str(size))
    else:
        return render_template("LU_par.html")

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
        return render_template("LU_little.html", L = result[0], U = result[1], x = result[2], size = str(size))
    else:
        return render_template("LU_little.html")

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
        return render_template("LU_crout.html", L = result[0], U = result[1], x = result[2], size = str(size))
    else:
        return render_template("LU_crout.html")

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
        return render_template("LU_cholesky.html", L = result[0], U = result[1], x = result[2], size = str(size))
    else:
        return render_template("LU_cholesky.html")