import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"]="SimHei"


def f(x):
    return (x + 1)**(1/3)


x = np.arange(0, 2, 0.001)
y = f(x)
fig, ax = plt.subplots()
# ax.plot(x, y, label="y=(x+1)^1/3")
# ax.plot(x, x, color='r', label="y=x")
# ax.set_xticks(np.linspace(0, 2, 10))
# ax.set_yticks(np.linspace(0, 2, 10))
# ax.legend(loc=3,labelspacing=1,handlelength=2,fontsize=10,shadow=True)
# plt.show()

x = [0, 2 ,3, 2, 0]
y = [1, 2,1,0, 1]
ax.plot(x,y, color='b')
plt.show()

def plot_decision_boundary(model, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)
    plt.show()