import torch
import matplotlib.pyplot as plt
import os
import argparse
import yaml

from utils.myBetaFuncSignal import my_utils_print
from utils.myBetaFuncAll import *


def yaml_and_function_inputs():
    cfg = open('./CFG/train.yaml', 'r', encoding='utf-8').read()  # 读全部文件
    data_conf = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法把读到的yaml文件内容转换成字典类型, Loader不可省略
    print(data_conf)
    print('--- learning rate ---\n', data_conf['learning rate'], '\nImport functions from directory:')
    my_utils_print()
    my_utils_all_print()
    my_utils_all_print2()


def main():
    yaml_and_function_inputs()
    # pass


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(prog='Classification Beta Stone', description='PyTorch realization')
    # parser.add_argument('--data', required=True, help='Raw data directory need to be added!')
    # parser.add_argument('--Directory for saving outputs', type=str, default="./outputs/")
    # parser.add_argument('--use_cuda', default=False, help="using CUDA for training")
    # args = parser.parse_args()

    main()
