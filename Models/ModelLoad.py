import torchvision
import torch

# from BetaModel import MyBetaModel

# Method 1
model_1st = torch.load('./BetaModel/vgg16_method_1st.pth')
# print(model_1st)

# Method 2
model_2nd = torch.load('./BetaModel/vgg16_method_2nd.pth')
# print(model_2nd)  # 直接输出字典
vgg16_model = torchvision.models.vgg16(pretrained=False)
vgg16_model.load_state_dict(model_2nd)
print(vgg16_model)  # 输出模型

# snare: need to import NNModel Class definition
model_3rd = torch.load('./BetaModel/myBetaModel.pth')
print(model_3rd)
