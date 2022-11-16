import matplotlib.pyplot as plt
import numpy as np
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, request, escape, Response


app = Flask(__name__)


@app.route("/plot")
def plot():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    xmin = request.args.get('xmin')
    xmax = request.args.get('xmax')
    ymin = request.args.get('ymin')
    ymax = request.args.get('ymax')

    x = np.linspace(float(xmin), float(xmax))
    y = float(a) * x ** 2 + float(b) * x + float(c)
    fig, ax = plt.subplots()
    ax.set_title("Quadratic Equations with Python")
    plt.ylim([ymin, ymax])
    ax.plot(x, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

