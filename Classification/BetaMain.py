"""
WorkFlow of complete DNN beta case
"""

import torch
import torchvision
from torch import nn
from torch.utils import data
from torch.utils.tensorboard import SummaryWriter


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
            nn.Linear(64 * 4 * 4, 64, bias=True),
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
        beta_data = torch.rand(1, 3, 64, 64)
        beta_main_compose = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Resize((32, 32))
        ])
        self.beta_data_processed = beta_main_compose(beta_data)

        pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass


def main():
    str_beta_main = 'BetaMain Text'
    epochs = 0
    img_beta_main = torch.rand(1, 3, 64, 64)
    value_beta_main = 0

    writer = SummaryWriter(log_dir='./log/BetaMainLog')
    writer.add_image('LogImg', img_tensor=img_beta_main, global_step=epochs)
    writer.add_scalar('LogCurve', value_beta_main, global_step=epochs)
    writer.add_text('LogText', str_beta_main, global_step=epochs)

    writer.close()


if __name__ == '__main__':
    main()
