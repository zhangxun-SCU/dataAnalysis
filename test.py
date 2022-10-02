import matplotlib.pyplot as plt


class GeometricDistribution:
    def __int__(self, p):
        self.p = p
        self.q = 1-p

    def prob(self, k):
        """
        第k次成功的概率：
        :param k: 第k次p发生
        :return: 概率值
        """
        return self.p * self.q ** (k - 1)

    def plot(self):
        pass


if __name__ == '__main__':
    test = GeometricDistribution(0.7)
    print(test.prob(2))