import torch
import torchvision
from torch import nn


class MyBetaModel(nn.Module):
    def __init__(self):
        super(MyBetaModel, self).__init__()
        self.convModel = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
        )
        self.convFlatten = nn.Sequential(
            nn.Flatten(),
            nn.Linear(1024, 64, bias=True),
            nn.Linear(64, 10, bias=True),
        )

    def forward(self, inputs):
        temp = self.convModel(inputs)
        outputs = self.convFlatten(temp)
        return outputs


if __name__ == '__main__':
    processModel = MyBetaModel()
    torch.save(processModel, './BetaModel/myBetaModel.pth')  # save model

# process validation
    x = torch.rand(1, 3, 32, 32)
    processVAL = torch.Tensor(x)
    result = processModel(processVAL)
    print(result.shape)
    print(result.size)
    print(result)

