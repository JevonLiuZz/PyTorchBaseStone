import torch
import random
import numpy as np

num = 101
dim = 10
dimSize = num // dim
print(dimSize)

a = np.random.rand(4, 1, 3, 2)
# a = torch.as_tensor(a)
print(a)
np.random.shuffle(a)
print("\n************\n")
print(a)
