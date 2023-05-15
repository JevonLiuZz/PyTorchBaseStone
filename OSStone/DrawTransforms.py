import cv2
import numpy as np
from torchvision import transforms
from PIL import Image


img_path_PIL = './FileRead/p1/OnePiece/Robin.jpg'
img_PIL = Image.open(img_path_PIL)
# img_PIL.show()
print(type(img_PIL))
print(img_PIL.size)
img_PIL_trans = transforms.Resize((512, 240))(img_PIL)
# img_PIL_trans.show()
print(type(img_PIL_trans))
print(img_PIL_trans.size)

img_path_cv = './FileRead/p1/OnePiece/Kozuki_Hiyori.jpg'
img_cv = cv2.imread(img_path_cv)
# cv2.imshow('name', img_cv)
# cv2.waitKey()
print(np.shape(img_cv))
img_cv_trans = transforms.ToTensor()(img_cv)
print(type(img_cv_trans))
print(img_cv_trans.size)

MyCompose = transforms.Compose([
    transforms.ToTensor(),
    # transforms.Normalize([125, 125, 125], [25, 25, 25], inplace=False),  # ★ 查看ToTensor后data的range
    transforms.Resize((512, 360)),
    # transforms.CenterCrop(10),
])
img_transforms = MyCompose(img_cv)
zxc = transforms.ToPILImage()(img_transforms)
zxc.show()
# cv2.imshow('transformed', np.array(img_transforms))
# cv2.imshow('transformed', zxc)
# cv2.waitKey()
