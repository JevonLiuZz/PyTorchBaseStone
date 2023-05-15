import os
from PIL import Image

"""
solution strategy: 1
"""


def dir_cat(file_dir, img_name):
    file_path = file_dir + img_name
    return file_path


file_dir = './p1/p2'
img_name = '/Chopper.jpg'
img = Image.open(dir_cat(file_dir, img_name))
print(dir_cat(file_dir, img_name))
img.show()

"""
solution strategy: 2
"""
image_path_1st = './p1/p2/Chopper.jpg'
img_1st = Image.open(image_path_1st)
img_1st.show()

"""
solution strategy: 3
"""
root_dir = './p1/p2'
file_dir = './Chopper.jpg'
image_path_2nd = os.path.join(root_dir, file_dir)
img_2nd = Image.open(image_path_2nd)
img_2nd.show()

"""
solution strategy: 4
"""
first_dir = './p1'
second_dir = './p2'  # './p2'会影响label的命名，
# 由于采用os.path.join()函数，可以换成 second_dir = 'p2'，
# 当不采用os.path.join()函数，可以修改 first_dir = './p1/'和 second_dir = 'p2'
image_dir = os.path.join(first_dir, second_dir)
img_dir_path = os.listdir(image_dir)  # 获取所有的图片的str信息
rank_pic = 1
img_name = img_dir_path[rank_pic]
image_item_path = os.path.join(first_dir, second_dir, img_name)
img_3rd = Image.open(image_item_path)
label = second_dir
print(image_item_path, '\nlabel:', label)
img_3rd.show()
