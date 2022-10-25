import matplotlib.pyplot as plt
import numpy as np
import utils


def NewTonIter(f, start, loss=1e-5 / 2):
    df = utils.autoderivation(f, 1e-5)
    x_t = start
    x_t1 = x_t - (f(x_t) / df(x_t))
    count = 0
    while np.fabs(x_t - x_t1) > loss:
        count += 1
        print(f"""迭代次数:{count}, x_t: {x_t}, x_t1: {x_t1} 
                """)
        x_t = x_t1
        x_t1 = x_t - (f(x_t) / df(x_t))
    return x_t1


def f(x):
    return np.cos(x) + 1 / (1 + np.exp(-2 * x))


def f1(x):
    return x


def f2(x):
    return np.arccos((-1) / (1 + np.exp(-2 * x)))


def f3(x):
    return 0.5 * np.log(-1 / (1 + (1 / np.cos(x))))


if __name__ == '__main__':
    # 1.
    print("1:")
    x_t = 3
    x_t1 = f2(x_t)
    count = 0
    while np.abs(x_t - x_t1) > 1e-5 / 2:
        count += 1
        print(f"""迭代次数: {count}, x_t:{x_t}, x_t1: {x_t1} 
        """)
        x_t = x_t1
        x_t1 = f2(x_t)
    print("迭代结果: ", x_t1)

    # 2
    print("2:")
    x_t = 3
    x_t1 = f3(x_t)
    count = 0
    while np.abs(x_t - x_t1) > 1e-5 / 2:
        count += 1
        print(f"""迭代次数: {count}, x_t:{x_t}, x_t1: {x_t1} 
        """)
        x_t = x_t1
        x_t1 = f3(x_t)
    print("结果: ", x_t1)

    # newton
    print("newton:")
    print("迭代结果: ", NewTonIter(f, 3))

