"""
Author: Jevon
Description: Simple regression implementation
Remark:
"""

import torch
from matplotlib import pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 200), dim=1)
y_hint = x.pow(2)
y = y_hint + 0.2 * torch.rand(x.size()) - 0.1


class MLPRegression(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_outputs):
        super(MLPRegression, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_outputs)

    def forward(self, input_data):
        input_data = torch.sigmoid(self.hidden(input_data))
        output_data = self.predict(input_data)
        return output_data


net = MLPRegression(n_feature=1, n_hidden=10, n_outputs=1)

optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
criteria = torch.nn.MSELoss()

batch_iteration = 3000
batch_size = 20
for batch in range(batch_iteration):
    if batch % batch_size == 0:
        print('Batch Process: %d/%d' % (1 + batch / batch_size, batch_iteration / batch_size))
    prediction = net(x)

    loss = criteria(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# validation
x_val = torch.unsqueeze(torch.linspace(-0.8, 0.8, 30), dim=1)
y_val = net(x_val)
x_val = x_val.detach().numpy()  # cannot plot variables in the form of tensor, need to be transferred into numpy
y_val = y_val.detach().numpy()
# plot
plt.plot(x, y_hint)  # hint function
plt.scatter(x, y)  # train data
plt.scatter(x_val, y_val)  # val data
plt.show()
