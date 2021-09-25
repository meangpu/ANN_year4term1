import sympy as sp
import numpy as np


def diff():
    i, o, p = sp.symbols('i o p', integer=True)

    a = sp.symbols("a")
    b = sp.symbols("b")
    c = sp.symbols("c")
    j = sp.symbols("j")
    k = sp.symbols("k")
    l = sp.symbols("l")
    n = sp.symbols("n")
    y = sp.symbols("y")
    front_y = (a*j) + (b*k) + (c*l) + n
    main_func = (front_y - y)**2

    the_big_L = 0.5*sp.summation(main_func, (i, o, p))
    without_sum = 0.5*((front_y - y)**2)

    ans = sp.diff(the_big_L, a)
    ans2 = sp.diff(without_sum, a)
    print(ans)
    print(ans2)


if __name__ == "__main__":
    diff()
