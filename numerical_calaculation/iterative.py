def iterative(start, times, parameters):
    """

    :param start:
    :param times:
    :param parameters:
    :return:
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


if __name__ == '__main__':
    print(iterative(1.5, 16, [1, 0, -1, -1]))

