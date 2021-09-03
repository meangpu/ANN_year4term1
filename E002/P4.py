import numpy as np


def gmax(u0, lr, N):
    u_now = u0

    for i in range(N):
        diff_u = grad(u_now)
        u_now += lr*diff_u

    return u_now


def grad(x):
    return 3 - 2*x


if __name__ == "__main__":
    ux = gmax(u0=0, lr=0.2, N=10)
    print(ux)

