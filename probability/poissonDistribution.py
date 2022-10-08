import math
import matplotlib.pyplot as plt
import numpy as np


class P:
    def __init__(self, _lambda):
        """
        泊松分布
        :param _lambda: n*p
        """
        self._lambda = _lambda
        self.getProb = lambda x: _lambda**x * np.exp(-_lambda) / math.factorial(x)

    def prob(self, k):
        return self.getProb(k)

