import matplotlib.pyplot as plt
from utils import *


class B:
    def __init__(self, n, p):
        """
        二项分布
        :param n: 试验总次数
        :param p: 试验成功概率
        """
        self.n = n
        self.p = p
        self.q = 1 - p
        self.probs = [(C(n, k) * p**k * self.q**(n-k)) for k in range(n + 1)]

    def prob(self, k):
        """
        成功k次的概率
        :param k: k次
        :return: 概率
        """
        return self.probs[k]

    def plot(self, show=False):
        """
        分布图
        :param show: 是否显示
        :return: 子图， （x, probs）
        """
        x = [i for i in range(self.n + 1)]
        fig, ax = plt.subplots()
        ax.scatter(x, self.probs)
        if show:
            plt.show()
        return ax, (x, self.probs)


if __name__ == '__main__':
    test = B(100, 0.5)
    print(test.prob(0))
    test.plot()