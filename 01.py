import math

a = 0.0
b = math.pi / 2
h = 1.0
eps = 1e-15


def f(x):
    return x - math.cos(x)


def bin(l, r):
    while abs(l - r) > eps:
        mid = (l + r) / 2
        if f(mid) * f(l) < 0:
            r = mid
        elif f(mid) * f(r) < 0:
            l = mid
    return (l + r) / 2


def scan(l, r, step):
    x1 = l
    x2 = x1 + step
    while True:
        if x2 > r:
            step -= 0.1
            x1 = l
            x2 = x1 + step
            continue
        if f(x1) * f(x2) > 0:
            x1 = x2
            x2 = x1 + step
        else:
            break
    return x1, x2


def g(x):
    return math.cos(x)


def iter():
    xk = g(0.1)
    xk_1 = g(xk)
    while abs(xk_1 - xk) > eps:
        xk = g(xk_1)
        xk_1 = g(xk)
    return xk_1


if __name__ == "__main__":
    lend, rend = scan(a, b, h)
    pred_x1 = bin(lend, rend)
    print(pred_x1)
    print(f(pred_x1))
    pred_x2 = iter()
    print(pred_x2)
    print(f(pred_x2))

# from matplotlib import pyplot as plt
#
# list = []
#
#
# def iterative(start, times, parameters):
#     """
#
#     :param start:
#     :param times:
#     :param parameters:
#     :return:
#     """
#
#     _len = len(parameters)
#
#     def f(x):
#         _sum = 0
#         for i in range(1, _len):
#             _sum += parameters[i] * x ** (_len - i - 1)
#         _sum = (-_sum / parameters[0]) ** (1 / (_len - 1))
#         return _sum
#
#     x_t = start
#     for i in range(times):
#         x_t1 = f(x_t)
#         x_t = x_t1
#         list.append(x_t1)
#     return x_t
#
#
# if __name__ == '__main__':
#     print(iterative(1.5, 8, [1, 0, -1, -1]))
#
#     fig, ax = plt.subplots()
#     time = range(1, 9)
#     plt.xlabel('time')
#     plt.ylabel('iteration')
#     plt.plot(time, list)
#     plt.show()
