def polynomial(parameters):
    """
    多项式
    :param parameters: 未知数系数列表，从高到低
    :return: 多项式结果
    """
    len_ = len(parameters)

    def f(x):
        _sum = 0
        for i in range(len_):
            _sum += parameters[i] * x ** (len_ - i - 1)
        return _sum

    return lambda x: f(x)


def derivation(parameters, order=1):
    """
    外层循环控制求导阶数，相当于第一次循环就是一阶导数，第二次为二阶导数
    内层循环的_len - i - 1 则是当前求导阶数会产生的参数个数，_len - i -1 - j就是上一阶函数对应的幂
    :param parameters: 方程参数
    :param order: 求导阶数
    :return: 导数参数值的列表
    """
    _len = len(parameters)
    results = []
    for i in range(_len - 1):
        if i == order:
            break
        results.append([])
        for j in range(_len - 1 - i):
            if i == 0:
                results[i].append(parameters[j] * (_len - i - 1 - j))
            else:
                results[i].append(results[i-1][j] * (_len - i - 1 - j))
    return results[order - 1]


if __name__ == "__main__":
    test = derivation([3, 6,4,1], 3)
    print(test)
