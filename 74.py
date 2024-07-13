# %%
import torch
from torch import nn
import torch.optim as optim

x_train_tensor = torch.load('data_source/70/train_feature.pt')
y_train_tensor = torch.load('data_source/70/train_label.pt')

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
num_epochs = 100
for epoch in range(num_epochs):
    output = model(x_train_tensor)

    loss = criterion(output, y_train_tensor)

    optimizer.zero_grad()

    loss.backward()
    optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


# %%
out_train = model(x_train_tensor)
y_pred_train = torch.softmax(out_train, dim=1)
result_train = torch.max(y_pred_train, dim=1).indices
print('Train correct rate: ', result_train.eq(y_train_tensor).sum().numpy() / len(y_train_tensor))
# %%
x_test_tensor = torch.load('data_source/70/test_feature.pt')
y_test_tensor = torch.load('data_source/70/test_label.pt')

out_test = model(x_test_tensor)
y_pred_test = torch.softmax(out_test, dim=1)
result_test = torch.max(y_pred_test, dim=1).indices
print('Test correct rate: ', result_test.eq(y_test_tensor).sum().numpy() / len(y_test_tensor))