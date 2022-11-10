from flask import Blueprint, render_template, request

singular = Blueprint('singular', __name__)

from .metodos.Bi import bi

@singular.route('/bus-inc', methods=['GET', 'POST'])
def bus_inc():
    if request.method == 'POST':
        fun = request.form.get('fun')
        x1 = request.form.get('x1')
        delta = request.form.get('delta')
        niter = request.form.get('niter')
        result = bi(x1,delta, niter, fun)
        return render_template("bus_inc.html", resultado = str(result))
    else:
        return render_template("bus_inc.html")