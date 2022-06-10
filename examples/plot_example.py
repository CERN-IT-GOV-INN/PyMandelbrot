"""
    This examples plots the Mandelbrot set.

    Usage:

    ```
    python examples/plot_example.py -o <output.png>
    ```
"""
from time import time as tm
import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PyMandelbrot.mandelbrot import MandelbrotDynamics


def plot_mandelbrot(fname: Path):
    """Plots the Mandelbrot set.

    Parameters
    ----------
    fname: Path
        The Mandelbrot set image output file.
    """
    x_ext = [-2.1, 0.6]
    y_ext = [-1.13, 1.13]
    ext = x_ext + y_ext

    x_pts = np.linspace(*x_ext, 1000)
    y_pts = np.linspace(*y_ext, 1000)
    cs = x_pts[None] + 1j * y_pts[:, None]
    z0s = np.zeros_like(cs)

    dynamics = MandelbrotDynamics(z0s, cs)
    dynamics.c = cs
    dynamics.z0 = z0s
    it = dynamics.get_divergency_iter()

    plt.rcParams.update({"text.usetex": True})
    fig = plt.figure()
    ax = fig.add_subplot()
    z = ax.imshow(it, origin="lower", extent=ext, cmap="plasma_r")
    plt.colorbar(z)

    # cosmetics
    fig.suptitle("Mandelbrot Set: divergency speed [iterations]", fontsize=20)
    ax.set_title(r"Dynamics of $f(z) = z^2 + c$", fontsize=20)
    ax.set_xlabel(r"$\Re(c)$", fontsize=20)
    ax.set_ylabel(r"$\Im(c)$", fontsize=20)
    ax.tick_params(axis="x", which="major", labelsize=14, direction="in", size=6)
    ticks = np.arange(-2, 1, 0.5)
    labels = ticks.astype(str)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    ax.tick_params(axis="y", which="major", labelsize=14, direction="in", size=6)
    ax.grid(alpha=0.6, linestyle="dashed")

    print(f"Saving Mandelbrot set image at {fname}")
    plt.savefig(fname, bbox_inches="tight")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mandelbrot set example")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("examples/mandelbrot_set.png")
    )
    args = parser.parse_args()

    start = tm()
    plot_mandelbrot(args.output)
    print(f"Program done in {tm()-start}s")
