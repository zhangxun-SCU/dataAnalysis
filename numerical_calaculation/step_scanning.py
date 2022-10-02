def scan(interval, step, rate, f):
    """
    等步长扫描法确定有解区间
    :param interval: a list of numbers, 扫描区间
    :param step: 扫描步长
    :param rate: step衰减系数
    :param f : 多项式函数
    :return: a tuple, 零点区间
    """
    if len(interval) != 2:
        raise Exception("区间长度异常！")
    left = interval[0]
    right = left + step
    while True:
        if right > interval[1]:
            step -= rate
            if step <= 0:
                raise Exception("没有零点或者rate过大")
            left = interval[0]
            right = left + step
        if f(left) * f(right) > 0:
            left = right
            right = left + step
        else:
            break
    return left, right


if __name__ == '__main__':
    from utils import *

    f = polynomial([1, 1, 1, 2])
    print(f(1))
    print(f(2))

    # a = [0, 2]
    # b = 1e-3
    # rate = 1e-5
    # interval = scan(a, b, rate)
    # print(interval)
    # print(f(interval[0]), f(interval[1]))
    # print(bisection(interval, 1e-5))
    # print(f(bisection(interval, 1e-15)))
