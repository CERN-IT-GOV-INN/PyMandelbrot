""" This module implements the base class to compute the Mandelbrot dynamics. """
import warnings
import numpy as np


class MandelbrotDynamics:
    """
    Implementation of the f(z) = z**2 + c function for the Mandelbrot Dynamics.

    Examples
    --------

    One Mandelbrot dynamics iteration:

    >>> import numpy as np
    >>> from PyMandelbrot.mandelbrot import MandelbrotDynamics
    >>> cs = np.linspace(-1,1,5) # offset parameter
    >>> cs
    array([-1. , -0.5,  0. ,  0.5,  1. ])
    >>> z0s = np.zeros_like(cs) # starting point
    >>> z0s
    array([0., 0., 0., 0., 0.])
    >>> dynamics = MandelbrotDynamics(z0s, cs)
    >>> z1s = dynamics()
    >>> z1s
    array([-1. , -0.5,  0. ,  0.5,  1. ])

    ``n = 4`` iterations:

    >>> z4s = dynamics.n_steps(n=4)
    >>> z4s
    array([ 0.     , -0.30859,  0.     ,  1.62890, 26.     ])

    Divergency speed calculation:

    >>> it = dynamics.get_divergency_iter()
    >>> it
    array([20, 20, 20,  5,  2], dtype=int16)
    """

    def __init__(
        self, z0: np.ndarray = None, c: np.ndarray = None, clip_value: float = 4.0
    ):
        """Basic constructor of the complex function describing Mandelbrot set.

        Parameters
        ----------
        z0 : np.ndarray
            Starting points of the Mandelbrot dynamics.
        c : np.array
            Offset parameters of the Mandelbrot function.
        clip_value : float
            The value to clip the starting point real and imaginary parts with.
            Defaults to 4.
        """

        self.__z0 = z0
        self.__c = c
        self.fn = lambda z, c: z**2 + c
        self.clip_value = clip_value

    @property
    def z0(self) -> np.ndarray:
        """Starting point property."""
        return self.__z0

    @z0.setter
    def z0(self, values: np.ndarray):
        """Starting point property setter.

        Checks that all the points have real and imaginary party lower than a
        certain value in the complex plane. Clips exeeding values otherwise.

        Parameters
        ----------
        values : np.ndarray
            Starting points of the Mandelbrot dynamics.
        """
        real = np.clip(np.real(values), -self.clip_value, self.clip_value)
        imag = np.clip(np.imag(values), -self.clip_value, self.clip_value)
        self.__z0 = real + 1j * imag

    def reset_z0(self):
        """Resets the starting point to `None`."""
        self.__z0 = None

    @property
    def c(self) -> np.ndarray:
        """Offset parameter property."""
        return self.__c

    @c.setter
    def c(self, values: np.ndarray):
        """Offset parameter property setter.

        Checks that all the points have real and imaginary party lower than a
        certain value in the complex plane. Clips exeeding values otherwise.

        Parameters
        ----------
        values: np.ndarray
            Offset parameters of the Mandelbrot dynamics.
        """
        real = np.clip(np.real(values), -self.clip_value, self.clip_value)
        imag = np.clip(np.imag(values), -self.clip_value, self.clip_value)
        self.__c = real + 1j * imag

    def reset_c(self):
        """Resets the offset parameter to `None`."""
        self.__c = None

    def __call__(self, z0: np.ndarray = None, c: np.ndarray = None) -> np.ndarray:
        """Computes one step of the Mandelbrot dynamics for the given starting
        point.

        Parameters
        ----------
        z0 : np.ndarray
            Starting points of the Mandelbrot dynamics.
        c : np.ndarray
            Offset parameters of the Mandelbrot dynamics.

        Returns
        -------
        np.ndarray
            The computed n-times repeated Mandelbrot points.
        """
        if z0 is None or c is None:
            self.check_params()
        z0 = z0 if z0 is not None else self.__z0
        c = c if c is not None else self.__c
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            z = self.fn(z0, c)
        return z

    def check_params(self):
        """Checks parameters are set.
        
        Raises
        ------
        ValueError
            If either starting point `z0` or offset parameter `c` is `None`.
        """
        if self.__z0 is None or self.__c is None:
            raise ValueError("Starting point not set, please set z0 attribute")

    def n_steps(self, n: int):
        """Computes `n` steps of the Mandelbrot dynamics for the given starting
        point.

        Parameters
        ----------
        z0 : np.ndarray
            Starting points of the Mandelbrot dynamic.
        n : int
            Number of steps of the Mandelbrot dynamics.
        """
        z = self.__z0
        for _ in range(n):
            z = self.__call__(z, self.__c)
        return z

    def get_divergency_iter(
        self, threshold: float = 4.0, max_iter: float = 20
    ) -> np.ndarray:
        """Computes the number of iteration needed by the dynamics to exceed
        some threshold.

        Given the stored starting point, it computes the number of steps for the
        dynamics modulusu to exceed a given threshold.

        Parameters
        ----------
        threshold : float
            The threshold above which the dynamics is considered divergent.
        max_iter : int
            The maximum number of steps to be evaluated.

        Returns
        -------
        np.ndarray
            The iteration number at which the dynamics has diverged.
        """
        z = self.__z0
        img = np.zeros_like(self.z0, dtype=np.int16)
        for _ in range(max_iter):
            z = self.__call__(z, self.__c)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                mask = (np.absolute(z) > threshold).astype(int)
            img += mask
        return 20 - img
