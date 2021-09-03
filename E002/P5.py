"""
P5
Student name: Nattapong Tangsatheanrapap
613040128-7
"""


import numpy as np


def g2min(u0, lr, N):
    u_now = u0

    for i in range(N):
        diff_u = [diff_u1(u_now), diff_u2(u_now)]
        remove = lr*np.array(diff_u)
        u_now = np.subtract(u_now, remove)

    return u_now


def diff_u1(u_array):
    ans = 2*u_array[0][0] + 1.5*u_array[1][0] - 16
    return [ans]


def diff_u2(u_array):
    ans = 1.5*u_array[0][0] + 4*u_array[1][0] - 35
    return [ans]


if __name__ == "__main__": 
    u0 = np.array([[0], [0]])
    ux = g2min(u0, lr=0.1, N=50)
    print("u*=", ux)
