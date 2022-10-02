from mutils import *
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
    x_t1 = f(x_t)
    for i in range(times):
        x_t = x_t1
        x_t1 = f(x_t)
    return x_t


def softIterative(start, times, parameters):
    pass


def NewTonIterative(f, start, loss=1e-5/2):
    df = autoderivation(f, 1e-5)
    x_t = start
    x_t1 = x_t - (f(x_t)/df(x_t))
    while np.fabs(x_t - x_t1) > loss:
        x_t = x_t1
        x_t1 = x_t - (f(x_t)/df(x_t))
        print(f"""初始值：{start}，导数值：{df(x_t)} 迭代值：{x_t1}，误差：{np.fabs(x_t - x_t1)}，要求误差：{loss}
                """)
    return x_t1


if __name__ == '__main__':

    def f(x):
        return x**2 - 7

    print(NewTonIterative(f, 2.5))
    import matplotlib
    import matplotlib.pyplot as plt
    #
    # fig, ax = plt.subplots()
    # x, nums = NewTonIterative(10, 10, [1, 0, 0, -10])
    #
    # ax.plot(nums)
    # plt.show()
