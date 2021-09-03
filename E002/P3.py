"""
P3
Student name: Nattapong Tangsatheanrapap
613040128-7
"""


import numpy as np


def gmin(u0, lr, N):
    u_now = u0

    for i in range(N):
        diff_u = diff_func(u_now)
        u_now -= lr*diff_u

    return u_now


def diff_func(x):
    upper = -np.exp(17 * x) + 14 * np.exp(9 * x) + 8 * np.exp(8 * x) + 8 * np.exp(10 * x) - np.exp(x)
    lower = (np.exp(9 * x) + np.exp(8 * x) + np.exp(x) + 1) ** 2
    ans = upper / lower
    return ans


if __name__ == "__main__": 
    ux = gmin(u0=0, lr=0.2, N=10) 
    print(ux)
