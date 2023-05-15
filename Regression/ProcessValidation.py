import torch
import matplotlib.pyplot as plt
import math
import numpy

pi = 3
x_train = numpy.arange(0, 2 * pi, pi / 4)
print(x_train)
print(type(x_train))
x_train = torch.tensor(x_train, dtype=torch.float64)
print(type(x_train))
x_train = torch.unsqueeze(x_train, dim=1)
print(x_train)

