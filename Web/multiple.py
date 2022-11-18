from flask import Blueprint, render_template, request
import numpy as np

multiple = Blueprint('multiple', __name__)

from .metodos.gausspiv import *

def gauss_form(x, mark, Ab):
    return f'Ab = {Ab} \nMark = {mark} \nX = {x}'

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
        print(result)
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
        print(result)
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

        x, mark, Ab = gaussSim(a, b, size,1)
        result = gauss_form(x, mark, Ab)
        print(result)
        return render_template("gauss_tot.html", resultado = str(result))
    else:
        return render_template("gauss_tot.html")