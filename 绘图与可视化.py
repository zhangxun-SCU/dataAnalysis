import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
import seaborn as sns

# data = np.arange(10)
# plt.plot(data)
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# plt.show()\

# fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(3):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
# plt.subplots_adjust(wspace=0, hspace=0)
# plt.show()

# x = np.random.randn(10)
# y = np.random.randn(10)
# fig, ax = plt.subplots()
# # ax.plot(x, y, 'g--')
# # ax[0].plot(x, y, linestyle='--', color='g')
# # ax[1].plot(np.random.randn(30).cumsum(), 'ko--')
# ax.plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
# plt.show()

# data = np.random.randn(30).cumsum()
# plt.plot(data, color='k', linestyle='--', label='default')
# plt.plot(data, 'k--', drawstyle='steps-post', label='step-post')
# plt.legend(loc='best')
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(np.random.randn(1000).cumsum())
# ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
#                             rotation=30,
#                             fontsize='small')
# ax.set_title('My first matplotlib plot')
# ax.set_xlabel('Stages')
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(np.random.randn(1000).cumsum(), color='k', label='one')
# ax.plot(np.random.randn(1000).cumsum(), color='k', linestyle='--', label='two')
# ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
# ax.legend(loc='best')
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(np.random.randn(1000).cumsum(), 'k.')
# x=60
# y=10
# ax.text(x, y, 'hello world', family='monospace', fontsize=10)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
#                    color='g', alpha=0.5)
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)
# # plt.show()
# fig.savefig('examples/fig.png', dpi=400, bbox_inches='tight')

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
#                    color='g', alpha=0.5)
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)
# # plt.show()
# buffer = BytesIO()
# fig.savefig(buffer)
# plot_data = buffer.getvalue()
# # print(plot_data)

# plt.rc('figure', figsize=(10, 10))
# font_options = {'family': 'monospace',
#                 'weight': 'bold',
#                 'size': '14'}
# plt.rc('font', **font_options)
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
#                    color='g', alpha=0.5)
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)
# plt.show()

# s = pd.Series(np.random.randn(10).cumsum(),
#               index=np.arange(0, 100, 10))
# s.plot()
# plt.show()

# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 设置颜色及透明度
#
# plt.title("RUNOOB Scatter Test") # 设置标题
#
# plt.show()

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
value = pd.Series(np.concatenate([comp1, comp2]))
sns.distplot(value, bins=100, color='k')
# sns.displot(value, bins=100, color='k')
plt.show()
