from flask import Blueprint, render_template, request
import numpy as np

interpol = Blueprint('interpol', __name__)

from .metodos.Vandermonde import vander
from .metodos.NewtonDifDiv import NewtonDifDiv

@interpol.route('/vandermonde', methods=['GET', 'POST'])
def vandermonde():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = vander(x, y, size, 101)
        return render_template("vandermonde.html", D=result[0], coef=result[1], polin=result[2], n = size, bol = 1)
    else:
        return render_template("vandermonde.html", bol = 0)

@interpol.route('/newton-int', methods=['GET', 'POST'])
def newton_int():
    if request.method == 'POST':
        size = int(request.form.get('size'))

        x = np.array(request.form.getlist('x'), dtype='float64')
        
        y = np.array(request.form.getlist('y'), dtype='float64')

        result = NewtonDifDiv(x, y)
        return render_template("newton_int.html", titulo=result[0], table=result[1], dDiv=result[2], pol=result[3], psim=result[4], n = size, bol = 1)
    else:
        return render_template("newton_int.html", bol = 0)