# %%
import torch
from torch import nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset, DataLoader
import time

x_train_tensor = torch.load('data_source/70/train_feature.pt')
y_train_tensor = torch.load('data_source/70/train_label.pt')
x_valid_tensor = torch.load('data_source/70/valid_feature.pt')
y_valid_tensor = torch.load('data_source/70/valid_label.pt')
x_test_tensor = torch.load('data_source/70/test_feature.pt')
y_test_tensor = torch.load('data_source/70/test_label.pt')

batch_size = 8

train_dataset = TensorDataset(x_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

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
# GPU device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

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
epochs = range(1, num_epochs + 1)

x_train_tensor, x_valid_tensor = x_train_tensor.to(device), x_valid_tensor.to(device)
y_train_tensor, y_valid_tensor = y_train_tensor.to(device), y_valid_tensor.to(device)


for epoch in range(num_epochs):
    output_train = model(x_train_tensor)
    output_valid = model(x_valid_tensor)

    loss_train.append(criterion(output_train, y_train_tensor).item())
    loss_valid.append(criterion(output_valid, y_valid_tensor).item())

    correct_train.append(correct_rate(output_train, y_train_tensor))
    correct_valid.append(correct_rate(output_valid, y_valid_tensor))

    torch.save(model.state_dict(), f'data_source/77/model_{epoch + 1}.pth')

    start = time.time()
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        output = model(inputs)

        loss = criterion(output, targets)

        optimizer.zero_grad()

        loss.backward()
        optimizer.step()
    
    end = time.time()
    print(f'Epoch [{epoch+1}/{num_epochs}], Time: {(end - start):.2f} seconds')
    

plt.plot(epochs, loss_train)
plt.title('loss at train')
plt.show()

plt.plot(epochs, correct_train)
plt.title('correct rate at train')
plt.show()

plt.plot(epochs, loss_valid)
plt.title('loss at valid')
plt.show()

plt.plot(epochs, correct_valid)
plt.title('correct rate at valid')
plt.show()

# %%
