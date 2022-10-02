import math

import numpy as np


def A(m, n):
    """
    排列数
    :param m:
    :param n:
    :return:
    """
    return math.factorial(m) / math.factorial(n)


def C(m, n):
    """
    组合数
    :param m:
    :param n:
    :return:
    """
    return math.factorial(m) / math.factorial(n) / math.factorial(m - n)


def Gamma(a, interval=1e-5):
    """
    Gamma函数
    :param a:
    :param interval:
    :return:
    """
    s = 0 + interval
    result = 0
    f = lambda x: np.power(x, a - 1) * np.exp(-x)
    while True:
        x_tmp = f(s)
        if x_tmp == 0:
            break
        result += x_tmp * interval
        s += interval

    return result


if __name__ == '__main__':
    print(Gamma(1, 0.00001))
