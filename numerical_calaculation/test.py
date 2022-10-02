import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 9, 10)
y = [np.random.randint(0, 10) for i in range(10)]
print(x, y)

fig, ax = plt.subplots()
plt.scatter(x, y)
plt.show()
