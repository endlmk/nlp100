# %%
import torch
from torch import nn

x_train_tensor = torch.load('data_source/70/train_feature.pt')
# %%
w = torch.randn(300, 4)
# %%
softmax = nn.Softmax(dim=1)
print(softmax(torch.matmul(x_train_tensor[:1], w)))
print(softmax(torch.matmul(x_train_tensor[:4], w)))

