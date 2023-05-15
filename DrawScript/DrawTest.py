import numpy as np
from matplotlib import pyplot as plt

x = []
y = []

plt.ion()

for i in range(50):
    x.append(i)
    y.append(i ** 2)
    plt.cla()  # 清除之前画的图, plt.clf() 、 plt.clf() 和 plt.close()的区别
    plt.plot(x, y * np.array([-1]), 'b-', lw=3)
    plt.xlabel("Variable: x")
    plt.ylabel("Outputs")
    # plt.grid()
    plt.text(0, 5, 'Loss= Unknown', fontdict={'size': 10, 'color': 'gray'})
    plt.pause(0.01)

plt.ioff()
plt.show()
