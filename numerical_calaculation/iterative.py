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
    :param ls:
    :return:
    """
    # 得到LDU和b
    L, D, U = LDU(X[:, :-1])
    b = X[:, -1]
    count = 1
    # 随机初始化x_0
    start = np.random.random(b.shape)
    x_0 = start
    x_1 = -np.matmul(-np.linalg.inv(D), np.matmul(L + U, x_0)) + np.matmul(np.linalg.inv(D), b)

    while np.linalg.norm(x_1 - x_0) > ls:
        count += 1
        x_0 = x_1
        x_1 = -np.matmul(np.linalg.inv(D), np.matmul(L + U, x_0)) + np.matmul(np.linalg.inv(D), b)
    return x_1


def Gauss_Seidel_Iter(X, ls=0.5e-6):
    """
    Gauss-Seidel迭代法求线性方程组
    :param X:
    :param ls:
    :return: result
    """
    L, D, U = LDU(X[:, :-1])
    b = X[:, -1]
    # 初始值
    count = 1
    start = np.random.random(b.shape)
    x_0 = start
    x_1 = -np.matmul(np.linalg.inv(D + L), np.matmul(U, x_0)) + np.matmul(np.linalg.inv(D + L), b)
    while np.linalg.norm(x_1 - x_0) > ls:
        count += 1
        x_0 = x_1
        x_1 = -np.matmul(np.linalg.inv(D + L), np.matmul(U, x_0)) + np.matmul(np.linalg.inv(D + L), b)
    return x_1


def SOR(X, w=1.0, ls=0.5e-6):
    """
    超松弛迭代求解线性方程组
    :param X:
    :param w:
    :param ls:
    :return:
    """
    L, D, U = LDU(X[:, :-1])
    b = X[:, -1]
    I = np.eye(L.shape[0], L.shape[1])
    # 初始值
    start = np.random.random(b.shape)
    x_0 = start
    count = 1
    x_1 = np.matmul(np.linalg.inv(I + w * np.matmul(np.linalg.inv(D), L)),
                    np.matmul((1 - w) * I - w * np.matmul(np.linalg.inv(D), U), x_0)) + w * np.matmul(
        np.linalg.inv(I + w * np.matmul(np.linalg.inv(D), L)), np.matmul(np.linalg.inv(D), b))
    while np.linalg.norm(x_1 - x_0) > ls:
        count += 1
        x_0 = x_1
        x_1 = np.matmul(np.linalg.inv(I + w * np.matmul(np.linalg.inv(D), L)),
                        np.matmul((1 - w) * I - w * np.matmul(np.linalg.inv(D), U), x_0)) + w * np.matmul(
            np.linalg.inv(I + w * np.matmul(np.linalg.inv(D), L)), np.matmul(np.linalg.inv(D), b))
    return x_1


def getMaxAbs(Matrix, i):
    """
    返回对应列的最大元素和行索引
    :param Matrix:
    :param i:
    :return:
    """
    maxIdx = i
    Max = np.abs(Matrix[i, i])
    for row in range(i, Matrix.shape[0]):
        if np.abs(Matrix[row, i]) > Max:
            maxIdx = row
            Max = Matrix[row, i]
    return maxIdx, Max


def swapLines(Matrix, row1, row2):
    """
    交换两行
    :param Matrix:
    :param row1:
    :param row2:
    :return:
    """
    for col in range(Matrix.shape[1]):
        Matrix[row1, col], Matrix[row2, col] = Matrix[row2, col], Matrix[row1, col]
    return Matrix


def Gauss(Matrix):
    """
    Gauss求解线性方程组
    :param Matrix: 线性方程组增加广矩阵
    :return:
    """
    row = Matrix.shape[0]
    col = Matrix.shape[1]
    for i in range(row - 1):
        # 第一层循环
        maxIdx, _max = getMaxAbs(Matrix, i)
        if i != maxIdx:
            # 交换
            Matrix = swapLines(Matrix, i, maxIdx)
        for j in range(i + 1, row):
            # 后面的每一行减去第一行除以首元素
            Matrix[j] -= Matrix[i] * (Matrix[j][i] / Matrix[i][i])

    # 回代
    re = row - 1
    while re > 0:
        re_1 = re - 1
        while re_1 >= 0:
            Matrix[re_1] -= Matrix[re] * (Matrix[re_1][re] / Matrix[re][re])
            re_1 -= 1
        re -= 1

    return np.array([(Matrix[i][-1] / sum(Matrix[i][:-1])) for i in range(row)])


if __name__ == '__main__':
    A = [[0.8147, 0.0975, 0.1576, 0.1419, 0.6557],
         [0.9058, 0.2785, 0.9706, 0.4218, 0.0357],
         [0.1270 * 10 ** 10, 0.5469, 0.9572, 0.9157, 0.8491],
         [0.9134, 0.9575, 0.4854 * 10 ** 8, 0.7922, 0.9340],
         [0.6324, 0.9649, 0.8003, 0.9595, 0.6787]]
    b = [0.000000002258000,
         0.000000001597700,
         1.270000002354900,
         0.024270003904200,
         0.000000003360250]
    tmp01 = np.array(A)
    tmp02 = np.array(b)
    tmp02 = tmp02.reshape([5, 1]) * 1e9
    # print(tmp01.shape, tmp02.shape)
    matrix = np.concatenate((tmp01, tmp02), axis=1)
    print(Gauss(matrix))

