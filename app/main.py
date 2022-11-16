import matplotlib.pyplot as plt
import numpy as np
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/plot")
def plot():
    a = request.args.get('a', default=0)
    b = request.args.get('b', default=0)
    c = request.args.get('c', default=0)
    xmin = request.args.get('xmin', default=-5)
    xmax = request.args.get('xmax', default=5)
    ymin = request.args.get('ymin', default=-5)
    ymax = request.args.get('ymax', default=5)

    x = np.linspace(float(xmin), float(xmax))
    y = float(a) * x ** 2 + float(b) * x + float(c)
    fig, ax = plt.subplots()
    ax.set_title("Quadratic Equations with Python")
    plt.ylim([ymin, ymax])
    ax.plot(x, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
