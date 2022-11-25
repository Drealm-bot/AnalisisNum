from flask import Blueprint, render_template, request
import numpy as np

interpol = Blueprint('interpol', __name__)

from .metodos.Interpol import *

@interpol.route('/vandermonde', methods=['GET', 'POST'])
def vandermonde():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = vander(x, y, size, 101)
        return render_template("vandermonde.html", D=result[0], coef=result[1], polin=result[2], grafica=result[3], n = size, bol = 1)
    else:
        return render_template("vandermonde.html", bol = 0)

@interpol.route('/newton-int', methods=['GET', 'POST'])
def newton_int():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = NewtonDifDiv(x, y)
        return render_template("newton_int.html", a=result[0], t=result[1], dDiv=result[2], pol=result[3], psim=result[4], lena = len(result[0]), n = size, bol = 1)
    else:
        return render_template("newton_int.html", bol = 0)

@interpol.route('/lagrange', methods=['GET', 'POST'])
def lagrange():
    if request.method == 'POST':
        np.printoptions(precision=4)
        size = int(request.form.get('size'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = lagi(x, y)
        return render_template("lagrange.html", result=result, bol = 1)
    else:
        return render_template("lagrange.html", bol = 0)

@interpol.route('/spline', methods=['GET', 'POST'])
def spline():
    if request.method == 'POST':

        size = int(request.form.get('size'))

        met = int(request.form.get('met'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = Spline(x, y, met)
        return render_template("spline.html", result=result, n=size, bol = 1)
    else:
        return render_template("spline.html", bol = 0)