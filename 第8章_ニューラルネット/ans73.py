import pathlib

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

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
y_train = pd.read_csv(folder_path / "y_train.csv", header=None)
y_train = torch.tensor(y_train[0].to_list())

x = X_train[0:4]
y = y_train[0:4]

net = Net(x.size()[1], 4)
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

for i in range(100):
    optimizer.zero_grad()
    output = net(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
