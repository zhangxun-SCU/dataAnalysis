import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # 解方程 得到a,b
    factor = np.array([[4, 10],
                       [10, 30]])
    results = np.array([[np.log(60) + np.log(30) + np.log(20) + np.log(15)],
                        [np.log(60) + np.log(30) * 2 + np.log(20) * 3 + np.log(15) * 4]])
    cb = np.linalg.inv(factor) @ results
    print(cb)
    a = np.exp(cb[0, 0])
    b = cb[1, 0]
    print(a, b)
    function = lambda x: a * np.exp(b * x)
    x = np.linspace(0, 5)
    y = function(x)
    sample_x = [1, 2, 3, 4]
    sample_y = [60, 30, 20, 15]
    # 作图
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.scatter(sample_x, sample_y, c='r')
    plt.show()
