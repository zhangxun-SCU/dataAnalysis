from utils import *
import numpy as np


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


def iter(start, times, parameters):
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


def NewTonIter(f, start, loss=1e-5 / 2):
    df = autoderivation(f, 1e-5)
    x_t = start
    x_t1 = x_t - (f(x_t) / df(x_t))
    while np.fabs(x_t - x_t1) > loss:
        x_t = x_t1
        x_t1 = x_t - (f(x_t) / df(x_t))
        print(f"""初始值：{start}，导数值：{df(x_t)} 迭代值：{x_t1}，误差：{np.fabs(x_t - x_t1)}，要求误差：{loss}
                """)
    return x_t1


def LDU(X):
    """
    将矩阵分解为LDU
    :param X: 方程参数矩阵
    :return:
        - L : X中i>j的部分
        - D : x中i=j的部分
        - U : x中i>j的部分
    """
    shape = X.shape
    L = np.zeros(shape)
    D = np.zeros(shape)
    U = np.zeros(shape)
    i, j = 0, 0
    while i != shape[0]:
        j = 0
        while j != shape[1]:
            if i > j:
                L[i, j] = X[i, j]
            elif i < j:
                U[i, j] = X[i, j]
            else:
                D[i, j] = X[i, j]
            j += 1
        i += 1
    return L, D, U


def JacobiIter(X, ls=0.5e-6):
    """
    Jacobi迭代法求解方程组
    :param X: 方程系数矩阵
    :return:
    """
    # 得到LDU和b
    L, D, U = LDU(X[:, :-1])
    b = X[:, -1]
    # 随机初始化x_0
    start = np.random.random(b.shape)
    x_0 = start
    x_1 = -np.matmul(-np.linalg.inv(D), np.matmul(L + U, x_0)) + np.matmul(np.linalg.inv(D), b)
    while np.linalg.norm(x_1 - x_0) > ls:
        x_0 = x_1
        x_1 = -np.matmul(np.linalg.inv(D), np.matmul(L + U, x_0)) + np.matmul(np.linalg.inv(D), b)
        print(f"""初始值: {start}, 迭代值: {x_1} 
        """)
    return x_1


def Gauss_Seidel_Iter(X, ls=0.5e-6):
    """
    Gauss-Seidel迭代法求线性方程组
    :param X:
    :return: result
    """
    L, D, U = LDU(X[:, :-1])
    b = X[:, -1]
    # 初始值
    start = np.random.random(b.shape)
    x_0 = start
    x_1 = -np.matmul(np.linalg.inv(D + L), np.matmul(U, x_0)) + np.matmul(np.linalg.inv(D + L), b)
    while np.linalg.norm(x_1 - x_0) > ls:
        x_0 = x_1
        x_1 = -np.matmul(np.linalg.inv(D + L), np.matmul(U, x_0)) + np.matmul(np.linalg.inv(D + L), b)
        print(f"""初始值: {start}, 迭代值: {x_1} 
            """)
    return x_1


if __name__ == '__main__':
    matrix = np.array([[4, 3, 0, 24],
                       [3, 4, -1, 30],
                       [0, -1, 4, -24]])

    print(JacobiIterative(matrix))
    print(G_SIterative(matrix))
