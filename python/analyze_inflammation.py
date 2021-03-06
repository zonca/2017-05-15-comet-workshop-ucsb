import numpy

# configure matplotlib with a non-interactive backend so that it can run on the workers
import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot

# See details about this software on the Python tutorial of Software Carpentry at:
# https://swcarpentry.github.io/python-novice-inflammation/

def analyze(filename):
    """Create plot from inflammation data
    
    Load inflammation data from csv, create plots of average, max and min
    
    Parameters
    -----------
    filename : str
         filename of csv data
    """

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.savefig(filename.replace("csv", "png"))
    matplotlib.pyplot.close(fig)
