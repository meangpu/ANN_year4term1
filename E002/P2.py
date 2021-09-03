"""
P2
Student name: Nattapong Tangsatheanrapap
613040128-7
* add int handler / add float**  // change format
"""
import numpy as np


def loss(x_list):

    if type(x_list) == int or type(x_list) == float:
        ans = (1 / (1 + np.exp(-8 * x_list))) - (1 / (1 + np.exp(-x_list)))
        return ans

    ans_list = []
    if type(x_list) == np.ndarray or type(x_list) == list:
        for item in x_list:
            ans = (1 / (1 + np.exp(-8 * item))) - (1 / (1 + np.exp(-item)))
            ans_list.append(ans)

    return np.array(ans_list)


def grad(x_list):

    if type(x_list) == int or type(x_list) == float:
        upper = -np.exp(17 * x_list) + 14 * np.exp(9 * x_list) + 8 * np.exp(8 * x_list) + 8 * np.exp(10 * x_list) - np.exp(x_list)
        lower = (np.exp(9 * x_list) + np.exp(8 * x_list) + np.exp(x_list) + 1) ** 2
        ans = upper / lower
        return ans

    ans_list = []
    if type(x_list) == np.ndarray or type(x_list) == list:
        for x in x_list:
            upper = -np.exp(17*x) + 14*np.exp(9*x) + 8*np.exp(8*x) + 8*np.exp(10*x) - np.exp(x)
            lower = (np.exp(9*x) + np.exp(8*x) + np.exp(x) + 1)**2
            ans = upper/lower
            ans_list.append(ans)

    return np.array(ans_list)


if __name__ == "__main__": 
    us = np.linspace(-1, 0, num=5)
    print(us)
    print(loss(us)) 
    print(grad(us))
