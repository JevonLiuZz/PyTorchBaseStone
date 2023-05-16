"""
WorkFlow of complete DNN beta case
"""

import torch
import torchvision
from torch import nn
from torch.utils import data


class WorkFlowModel(nn.Module):
    def __init__(self):
        super(WorkFlowModel, self).__init__()
        self.conv1st = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1, stride=2),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1, stride=2),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride=2),
            nn.MaxPool2d(2),
        )
        self.flatten1st = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64*4*4, 64, bias=True),
        )
        self.outputs1st = nn.Sequential(
            nn.Linear(64, 10, bias=True),
        )

    def forward(self, inputs):
        temp = self.conv1st(inputs)
        temp = self.flatten1st(temp)
        outputs = self.outputs1st(temp)
        return outputs


class WorkFlowDataSet(data.Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
