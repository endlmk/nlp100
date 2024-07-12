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
