import numpy as np
import cv2
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms


writer = SummaryWriter(log_dir="./TensorBoardLog")
# 可查看函数描述，删除 log_dir 参数，将会有对应的log文件夹，并且附带有comment以及时间信息，e.g.:
# writer = SummaryWriter(comment="LR0.01_WD0.01")
# 这将生成 runs/**CURRENT_DATETIME_HOSTNAME** 文件夹


#  cv solution
img_dir_cv = '../../OSStone/FileRead/p1/p2/Luffy.jpg'
img_cv = cv2.imread(img_dir_cv)
cv2.imshow('img_cv', img_cv)
cv2.waitKey()


#  PIL.Image solution
img_dir_PIL = '../../OSStone/FileRead/p1/p2/Nami.jpeg'
img_PIL = Image.open(img_dir_PIL)
# img_PIL.show()

"""
solution case 1: np.array
"""
img_array = np.array(img_PIL)
# print(type(img_array))
# print(img_array.shape)

writer.add_image(tag='One Piece array', img_tensor=img_array, global_step=1, dataformats='HWC')
# 这边修改了 dataformats 参数， 不是采取的默认值
# 在训练过程中可以通过修改 global_step 来展示训练过程中的一些图片

"""
solution case 2: np.tensor
convert jpg type to tensor type for add_image() function use
"""
img_dir_PIL_2 = '../../OSStone/FileRead/p1/p2/Chopper.jpg'
img_PIL_2 = Image.open(img_dir_PIL_2)
PILToTensor = transforms.PILToTensor()  # instantiation实例化
img_tensor_C = PILToTensor(img_PIL_2)
# print(img_PIL_2)
# print(type(img_PIL_2))
# print(type(img_tensor_C))
# print(img_tensor_C.shape)

img_dir_PIL_3 = '../../OSStone/FileRead/p1/p2/Luffy.jpg'
img_PIL_3 = Image.open(img_dir_PIL_3)
img_tensor_L = transforms.PILToTensor()(img_PIL_3)

writer.add_image(tag='One Piece tensor', img_tensor=img_tensor_C, global_step=1)
writer.add_image(tag='One Piece tensor', img_tensor=img_tensor_L, global_step=2)


# curve
for x in range(10):
    y = x**2 + 5
    writer.add_scalar("Function y = x^2 + 5", y, x)
writer.close()
