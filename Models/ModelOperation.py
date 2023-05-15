import torchvision
import torch


# Method 1
innerModel = torchvision.models.vgg16(weights=None)
torch.save(innerModel, './BetaModel/vgg16_method_1st.pth')

# Method 2
torch.save(innerModel.state_dict(), './BetaModel/vgg16_method_2nd.pth')
