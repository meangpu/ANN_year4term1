import numpy as np


def gmin(u0, lr, N):
    u_now = u0

    for i in range(N):
        diff_u = grad(u_now)
        u_now -= lr*diff_u

    return u_now


def grad(x):
    upper = -np.e**(17*x) + 14*np.e**(9*x) + 8*np.e**(8*x) + 8 * np.e**(10*x) - np.e**x
    lower = (np.e**(9*x) + np.e**(8*x) + np.e**x + 1)**2
    ans = upper/lower
    return ans


if __name__ == "__main__":
    ux = gmin(u0=0, lr=0.2, N=10)
    print(ux)
