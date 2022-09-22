import polynomial
import numpy as np

def iterative(start, times, parameters):
    """
    迭代法求解多项式方程的解
    :param start: 迭代其实值
    :param times: 迭代次数
    :param parameters: 多项式参数
    :return: 迭代结果，迭代经过
    """

    _len = len(parameters)

    def f(x):
        _sum = 0
        for i in range(1, _len):
            _sum += parameters[i] * x ** (_len - i - 1)
        _sum = (-_sum / parameters[0]) ** (1 / (_len - 1))
        return _sum

    x_t = start
    for i in range(times):
        x_t1 = f(x_t)
        x_t = x_t1
    return x_t


def softIterative(start, times, parameters):
    pass


def NewTonIterative(start, times, parameters):
    x_t = start
    f = polynomial.polynomial(parameters)
    f_1 = polynomial.polynomial(polynomial.derivation(parameters, 1))
    for i in range(times):
        x_t1 = x_t - (f(x_t)/f_1(x_t))
        x_t = x_t1
    return x_t


if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt
    #
    # fig, ax = plt.subplots()
    # x, nums = NewTonIterative(10, 10, [1, 0, 0, -10])
    #
    # ax.plot(nums)
    # plt.show()
