import torch
import numpy as np
from torchvision import transforms


x = torch.rand(2, 1, 3, 3)
c = x[:, 0, ...]
print(x.shape)
print(x)
print(c)

