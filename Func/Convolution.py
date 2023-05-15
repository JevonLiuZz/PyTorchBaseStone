import numpy as np
import torch
from torch.nn import functional as f


shuRu = torch.tensor([[1, 2, 0, 3],
                      [5, 0, 6, 8],
                      [0, 2, 4, 7],
                      [1, 0, 1, 0]])
# shuRu = input.resize(1, 1, 4, 4)
shuRu = torch.reshape(shuRu, (1, 1, 4, 4))
kernel = torch.tensor([[1, 0],
                       [0, 1]])
# kernel = kernel.resize(1, 1, 2, 2)
kernel = torch.reshape(kernel, (1, 1, 2, 2))
shuChu = f.conv2d(shuRu, kernel, stride=1, dilation=(1, 2))
print(shuChu.size())
print(np.shape(shuChu))
print(shuChu)
