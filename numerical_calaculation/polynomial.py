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
