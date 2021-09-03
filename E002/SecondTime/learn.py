import numpy as np


def loss(u):
    return 1/(1+np.exp(-8*u)) - 1/(1+np.exp(-u))


def grad(u):
    ans = np.gradient(loss(u), 0.25)
    return ans


if __name__ == "__main__":
    us = np.linspace(-1, 0, num=5)  # [-1.   -0.75 -0.5  -0.25  0.  ] 5 number from -1 to 0
    print(us)
    print(loss(us))
    print(grad(us))

