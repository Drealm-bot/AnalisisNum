from flask import Flask, Blueprint, render_template, request
import os

singular = Blueprint('singular', __name__)

from .metodos.Singulares import *
from .metodos.Graficador import graficador

@singular.route('/bus-inc', methods=['GET', 'POST'])
def bus_inc():
    if request.method == 'POST':
        fun = request.form.get('fun')
        x1 = request.form.get('x1')
        delta = request.form.get('delta')
        niter = request.form.get('niter')
        result = bi(x1,delta, niter, fun)
        return render_template("bus_inc.html", resultado = str(result), bol = 1)
    else:
        return render_template("bus_inc.html", bol = 0)

        
@singular.route('/bisection', methods=['GET', 'POST'])
def bisection():
    if request.method == 'POST':
        fun = request.form.get('fun')
        a = request.form.get('a')
        b = request.form.get('b')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = biseccion(a, b, tol, niter, fun)
        return render_template("bisection.html", n=result[0], a=result[1], b=result[2], m=result[3], fm=result[4], E=result[5], bol = 1)
    else:
        return render_template("bisection.html", bol = 0)

@singular.route('/false_position', methods=['GET', 'POST'])
def false_position():
    if request.method == 'POST':
        fun = request.form.get('fun')
        a = request.form.get('a')
        b = request.form.get('b')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = regla_falsa(a, b, tol, niter, fun)
        return render_template("false_position.html", n=result[0], a=result[1], b=result[2], m=result[3], fm=result[4], E=result[5], bol = 1)
    else:
        return render_template("false_position.html", bol = 0)

@singular.route('/fixed_point', methods=['GET', 'POST'])
def fixed_point():
    if request.method == 'POST':
        f = request.form.get('f')
        g = request.form.get('g')
        x0 = request.form.get('x0')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = punto_fijo(x0, tol, niter, f, g)
        return render_template("fixed_point.html", n=result[0], xn=result[1], fn=result[2], gn=result[3], E=result[4], bol = 1)
    else:
        return render_template("fixed_point.html", bol = 0)

@singular.route('/newton-raphson', methods=['GET', 'POST'])
def newton_rph():
    if request.method == 'POST':
        f = request.form.get('fun')
        df = request.form.get('df')
        x0 = request.form.get('x0')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = newton_raphson(x0, tol, niter, f, df)
        return render_template("newton_raphson.html", n=result[0], xn=result[1], fn=result[2], E=result[3], bol = 1)
    else:
        return render_template("newton_raphson.html", bol = 0)

@singular.route('/secant', methods=['GET', 'POST'])
def secant():
    if request.method == 'POST':
        fun = request.form.get('fun')
        print(type(fun))
        x0 = request.form.get('x0')
        x1 = request.form.get('x1')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = secante(x0, x1, tol, niter, fun)
        return render_template("secant.html", n=result[0], xn=result[1], fn=result[2], E=result[3], bol = 1)
    else:
        return render_template("secant.html", bol = 0)

@singular.route('/newtonMR', methods=['GET', 'POST'])
def newtonMR():
    if request.method == 'POST':
        fun = request.form.get('fun')
        df = request.form.get('df')
        df2 = request.form.get('df2')
        x0 = request.form.get('x0')
        tol = request.form.get('tol')
        niter = request.form.get('niter')
        result = newtonRM(x0, tol, niter, fun, df, df2)
        return render_template("newtonMR.html", n=result[0], xn=result[1], fn=result[2], E=result[3], bol = 1)
    else:
        return render_template("newtonMR.html", bol = 0)

@singular.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        fun = request.form.get('fun')
        grafica = graficador(fun)
        return render_template("graph.html", grafica=grafica, bol = 1)
    else:
        return render_template("graph.html", bol = 0)



