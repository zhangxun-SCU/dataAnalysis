import matplotlib.pyplot as plt

from utils import *


class H:
    def __init__(self, n, m, N):
        """
        超几何分布初始化
        :param n: 总共要的数量
        :param m: 第一部分的数量
        :param N: 样本总数/样本空间
        """
        self.n = n
        self.m = m
        self.N = N
        self.probs = [(C(m, k) * C(N-m, n-k) / C(N, n)) for k in range(min(m, n) + 1)]

    def prob(self, k):
        """

        :param k: 第一类有k个
        :return: 第一类有k个的概率
        """
        return self.probs[k]

    def plot(self, show=False):
        """
        画出分布图
        :param show: 是否显示图像
        :return: 图像子图, (x, probs)
        """
        x = [i for i in range(min(self.m, self.n) + 1)]
        fig, ax = plt.subplots()
        ax.scatter(x, self.probs)
        if show:
            plt.show()
        return ax, (x, self.probs)


if __name__ == '__main__':
    test = H(3, 27, 30)
    print(test.prob(3) + test.prob(2) + test.prob(1) + test.prob(0))
    test.plot()
