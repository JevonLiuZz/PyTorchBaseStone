import torch
import glob
import os
import numpy as np
from torch.utils import data as data


class MyBetaDataset(data.Dataset):

    def __int__(self, rootPath, cropSize, mode='train'):
        self.dataFilesList = [x for x in glob.glob(os.path.join(rootPath, '*.jpg'))]
        self.cropSize = cropSize
        self.mode = mode
        if self.mode == 'betaTest':
            print('----- Mode: betaTest -----\nDescriptions: Could add other operations\n')

    def __getitem__(self, index):
        # code L begin

        # # case 1
        self.data = self.dataFilesList[index]
        self.dataSample = self.data[0]
        self.labelSample = self.data[1]

        # # case 2
        # self.dataSample = self.dataFilesList[index][0]
        # self.labelSample = self.dataFilesList[index][1]

        # code L end

        if self.mode == 'betaTest':
            print('----- Mode: betaTest -----\nDescriptions: Could add other operations\n')
        elif self.mode == 'val':
            print('----- Mode: validation -----\nDescriptions: Could add other operations\n')

        return (torch.from_numpy(self.dataSample).float(),
                torch.from_numpy(self.labelSample).long())

    def __len__(self):
        return len(self.dataFilesList)
