import pathlib

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

class Net(nn.Module):
    def __init__(self, in_units, out_units):
        super(Net, self).__init__()
        self.l1 = nn.Linear(in_units, out_units)

    def forward(self, x):
        y = self.l1(x)
        return y

# データ準備
folder_path = pathlib.Path(__file__).resolve().parent

X_train = pd.read_csv(folder_path / "X_train.csv", header=None)
X_train = torch.from_numpy(X_train.values.astype(np.float32))

X_valid = pd.read_csv(folder_path / "X_valid.csv", header=None)
X_valid = torch.from_numpy(X_valid.values.astype(np.float32))

y_train = pd.read_csv(folder_path / "y_train.csv", header=None)
y_train = torch.tensor(y_train[0].to_list())

y_valid = pd.read_csv(folder_path / "y_valid.csv", header=None)
y_valid = torch.tensor(y_valid[0].to_list())

x = X_train
y = y_train

net = Net(x.size()[1], 4)
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

train_losses = []
train_accuracy = []
valid_losses = []
valid_accuracy = []

for epoc in range(1000):
    optimizer.zero_grad()
    output = net(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

    train_losses.append(criterion(net(X_train), y_train))
    _, y_train_pred = torch.max(net(X_train), 1)
    train_accuracy.append(accuracy_score(y_train_pred.numpy(), y_train.numpy()))

    valid_losses.append(criterion(net(X_valid), y_valid))
    _, y_valid_pred = torch.max(net(X_valid), 1)
    valid_accuracy.append(accuracy_score(y_valid_pred.numpy(), y_valid.numpy()))

plt.plot(train_losses, label='train loss')
plt.plot(valid_losses, label='valid loss')
plt.legend()
plt.show()

plt.plot(train_accuracy, label='train accuracy')
plt.plot(valid_accuracy, label='valid accuracy')
plt.legend()
plt.show()
