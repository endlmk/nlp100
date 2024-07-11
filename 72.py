
# %%
from math import log
import torch
from torch import nn

x_train_tensor = torch.load('data_source/70/train_feature.pt')
# %%
w = torch.randn(300, 4)
# %%
softmax = nn.Softmax(dim=1)
x1 = (softmax(torch.matmul(x_train_tensor[:1], w)))
x1_4 =  (softmax(torch.matmul(x_train_tensor[:4], w)))

# %%
y_train_tensor = torch.load('data_source/70/train_label.pt')
l1 = -log(x1[0, y_train_tensor[0].item()].item())
print(l1)
# %%
sum1_4 = 0
for i in range(4):
    sum1_4 += -log(x1_4[i, y_train_tensor[i].item()].item())
l1_4 = sum1_4 / 4
print(l1_4)
# %%
loss = nn.CrossEntropyLoss()
X = torch.matmul(x_train_tensor, w)
X = torch.tensor(X, requires_grad=True)
o = loss(X, y_train_tensor)

# %%
o.backward()
print(X.grad)
