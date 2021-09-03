"""
P4
Student name: Nattapong Tangsatheanrapap
613040128-7
"""
import sys


def ebm_calculator():
    k = 5.67e-8
    try:
        s = float(input("S: "))
        a = float(input("a: "))
        e = float(input("e: "))
    except ValueError:
        print("You Did Not Enter A Valid Number! ")
        sys.exit()

    upper = (1-a)*s
    lower = e*k
    div = upper/lower
    t = div**0.25

    print(f"T= {t:.2f}")


if __name__ == '__main__':
    ebm_calculator()
