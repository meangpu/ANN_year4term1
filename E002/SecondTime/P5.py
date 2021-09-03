import numpy as np


def g2min(u0, lr, N):
    u_now = u0

    for i in range(N):
        diff_u = [first_equa(u_now), sec_equa(u_now)]
        remove = lr*np.array(diff_u)
        u_now = np.subtract(u_now, remove)

    return u_now


def first_equa(var_list):
    return 2*var_list[0] + 1.5*var_list[1] - 16


def sec_equa(var_list):
    return 1.5*var_list[0] + 4*var_list[1] - 35


if __name__ == "__main__":
    u0 = np.array([[0], [0]])
    ux = g2min(u0, lr=0.1, N=50)
    print("u*=", ux)
