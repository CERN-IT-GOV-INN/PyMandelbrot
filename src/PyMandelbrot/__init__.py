from importlib.metadata import metadata

PACKAGE = "PyMandelbrot"

__version__ = metadata(PACKAGE)["version"]