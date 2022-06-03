[![DOI](https://zenodo.org/badge/484051775.svg)](https://zenodo.org/badge/latestdoi/484051775)

[![Made at CERN!](https://img.shields.io/badge/CERN-OpenSource-orange)](https://home.cern)
[![Made at CERN!](https://img.shields.io/badge/CERN-Innovation-purple)](https://information-technology.web.cern.ch/about/organisation/strategy-executive-governance)
[![Made at CERN!](https://img.shields.io/badge/CERN-CERN%20openlab-blue)](https://openlab.cern/)
[![Documentation Status](https://readthedocs.org/projects/pymandelbrot/badge/?version=latest)](https://pymandelbrot.readthedocs.io/en/latest/?badge=latest)

# PyMandelbrot - Mandelbrot Set Visualizer with Python

This package helps visualizing the Mandelbrot set.

## Documentation

The documentation for PyMandelbrot can be consulted in the readthedocs page:
[pymandelbrot.readthedocs.io](https://pymandelbrot.readthedocs.io/en/latest/)

## How to install

The package can be installed with Python's pip package manager.

```bash
git clone https://github.com/openlab-test/example-repo.git PyMandelbrot
cd PyMandelbrot
pip install .
```

This process will copy the `PyMandelbrot` library to your environment python path.

## Quickstart

In a python script, just import the `MandelbrotDynamics` class defined in the
`PyMandelbrot` package:

```python
from PyMandelbrot.mandelbrot import MandelbrotDynamics

z0s = np.zeros_like(c) # starting point
cs = np.linspace(-1,1,10) # offset parameter

# load the points in the MandelbrotDynamics object
dynamics = MandelbrotDynamics(z0s, cs)

# call one evaluation of the f(z) = z**2 + c function
z1s = dynamics()

# call multiple evaluations of the f(z) = z**2 + c function
z4s = dynamics.n_steps(n=4)

# compute divergency speed for the grid of points
it = dynamics.get_divergency_iter()
```

## Examples

The [examples](examples) foldes contains a full example in `.py` and `.ipynb`
format to visualize the Mandelbrot set.
