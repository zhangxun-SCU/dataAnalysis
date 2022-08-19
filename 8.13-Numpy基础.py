
import numpy as np
import matplotlib.pyplot as plt

# 转置：转置是重塑的一种特殊形式，它返回的是源数据的视图（不会进行任何复制操作）
arr = np.arange(15).reshape((3, 5))
print("a:", arr)
print("a.T:", arr.T)
print("转置计算矩阵内积")
arr = np.random.randn(6, 3)
print(arr)
print(np.dot(arr.T, arr))
# 高位数组转置transpose
arr = np.arange(16).reshape((2, 2, 4))
print(arr.transpose((1, 0, 2)))


# 通用函数
arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))
x = np.random.randn(8)
y = np.random.randn(8)
# print(np.random.rand(2))
print("x: ", x)
print("y: ", y)
print("maxOfXY: ", np.maximum(x, y))
arr = np.random.randn(7)*10
remainder, whole_part = np.modf(arr)
print(arr)
print(remainder)
print(whole_part)

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)


# 逻辑标书为数组运算
# numpy.where
x = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y = np.array([11, 12, 13, 14, 15])
cond = np.array([True, False, True, True, False])
result = np.where(cond, x, y)
print(result)


# 统计
arr = np.random.randn(5, 4)
print(arr.mean())
print(arr.sum())

# bool
arr = np.random.randn(100)
print((arr > 0).sum())
bools = np.array([True, False, True, True, False])
print(bools.any())
print(bools.all())

# np.random.seed(1234)
arr = np.array([1, 2, 3, 4])
select = np.array([True, False, True, False])
print(arr[select])

arr = np.arange(10)
np.save('examples/some_array', arr)
print(np.load('examples/some_array.npy'))
np.savez('examples/array_archive.npz', a=arr, b=arr)
arch = np.load('examples/array_archive.npz')
print(arch)
print(arch['a'])
np.savez_compressed('examples/arrays_compressed.npz', a=arr, b=arr)


