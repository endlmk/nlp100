# %%
import torch
from torch import nn
import torch.optim as optim
import matplotlib.pyplot as plt

x_train_tensor = torch.load('data_source/70/train_feature.pt')
y_train_tensor = torch.load('data_source/70/train_label.pt')
x_valid_tensor = torch.load('data_source/70/valid_feature.pt')
y_valid_tensor = torch.load('data_source/70/valid_label.pt')
x_test_tensor = torch.load('data_source/70/test_feature.pt')
y_test_tensor = torch.load('data_source/70/test_label.pt')

# %%
class SimpleLinear(nn.Module):
    def __init__(self, input_size, output_size) -> None:
        super().__init__()
        self.linear = nn.Linear(input_size, output_size, bias=False)

    def forward(self, x):
        x = self.linear(x)
        return x

# %%    
model = SimpleLinear(300, 4)

# %%
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# %%
def correct_rate(out, y):
    y_pred = torch.softmax(out, dim=1)
    result = torch.max(y_pred, dim=1).indices
    return result.eq(y).sum().numpy() / len(y)

# %%
num_epochs = 100
loss_train = []
loss_valid = []
correct_train = []
correct_valid = []

for epoch in range(num_epochs):
    output = model(x_train_tensor)
    output_valid = model(x_valid_tensor)

    loss = criterion(output, y_train_tensor)
    loss_train.append(loss.item())
    loss_valid.append(criterion(output_valid, y_valid_tensor).item())

    correct_train.append(correct_rate(output, y_train_tensor))
    correct_valid.append(correct_rate(output_valid, y_valid_tensor))

    optimizer.zero_grad()

    loss.backward()
    optimizer.step()

plt.plot(range(1, 101), loss_train)
plt.title('loss at train')
plt.show()

plt.plot(range(1, 101), correct_train)
plt.title('correct rate at train')
plt.show()

plt.plot(range(1, 101), loss_valid)
plt.title('loss at valid')
plt.show()

plt.plot(range(1, 101), correct_valid)
plt.title('correct rate at valid')
plt.show()

# %%
