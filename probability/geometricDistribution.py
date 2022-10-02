import matplotlib.pyplot as plt


class G:
    def __init__(self, p):
        """
        几何分布
        :param p: 事件发生概率
        """
        self.p = p
        self.q = 1-p

    def prob(self, k):
        """
        第k次成功的概率：
        :param k: 第k次p发生
        :return: 概率值
        """
        return self.p * self.q ** (k - 1)

    def plot(self, n, show=True):
        """
        画图，
        :param n:试验总次数为n
        :param show: 是否显示
        :return: 子图对象
        """
        x = [i for i in range(1, n + 1)]
        probs = [self.prob(i) for i in range(1, n + 1)]
        fig, ax = plt.subplots()
        ax.scatter(x, probs)
        plt.show()
        return ax, (x, probs)


if __name__ == '__main__':
    test = G(0.7)
    print(test.prob(2))
    test.plot(10)
