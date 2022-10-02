import math


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
    return math.factorial(m) / math.factorial(n) / math.factorial(m-n)



