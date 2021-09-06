import sympy as sp
import numpy as np


def diff():
    x = sp.symbols("x")
    # ans = sp.diff((1/(1+sp.exp(-8*x))) - (1/(1+sp.exp(-x))))
    ans = sp.diff((5*sp.cos(2*x)) * (4*sp.sin(2*x)))
    print(ans)


def diff2var():
    x = sp.symbols("x")
    y = sp.symbols("y")
    main_equa = x**2 + 1.5*x*y - 16*x + 2*(y**2) - 35*y
    diff_x = sp.diff(main_equa, x)
    diff_y = sp.diff(main_equa, y)
    print(diff_x)
    print(diff_y)


def main_ans(u):
    ans = -np.exp(-u) / (1 + np.exp(-u)) ** 2 + 8 * np.exp(-8 * u) / (1 + np.exp(-8 * u)) ** 2


if __name__ == "__main__":
    diff()
    # diff2var()