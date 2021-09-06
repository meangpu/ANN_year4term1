import sympy as sp
import numpy as np


def loss(u):
    ans = 1/(1+np.exp(-8*u)) - 1/(1+np.exp(-u))
    return ans


def diff():
    u = sp.symbols("u")
    ans = sp.diff(1/(1+sp.exp(-8*u)) - 1/(1+sp.exp(-u)))
    print(ans)


def grad(u):
    ans = -np.exp(-u)/(1 + np.exp(-u))**2 + 8*np.exp(-8*u)/(1 + np.exp(-8*u))**2
    return ans


if __name__ == "__main__":
    diff()
    # us = np.linspace(-1, 0, num=5)  # [-1.   -0.75 -0.5  -0.25  0.  ] 5 number from -1 to 0
    # print(us)
    # print(loss(us))
    # print(grad(us))

