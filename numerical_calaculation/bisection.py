def bisection(interval, accuracy, f):
    """
    二分法求近似解
    :param interval: 求解区间
    :param accuracy: 近似解精度
    :param f : 多项式函数
    :return: 近似解
    """
    left = interval[0]
    right = interval[1]
    while abs(left - right) > accuracy:
        mid = (left + right) / 2
        if f(left) == 0:
            return left
        if f(right) == 0:
            return right
        if f(mid) == 0:
            return mid
        if f(left) * f(mid) <= 0:
            right = mid
        elif f(mid) * f(right) <= 0:
            left = mid
    return (left + right) / 2
