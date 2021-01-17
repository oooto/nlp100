import pathlib
import pickle

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

y_train = pd.read_csv(folder_path / "y_train.csv", header=None)
y_train = torch.tensor(y_train[0].to_list())

x = X_train
y = y_train

net = Net(x.size()[1], 4)
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

train_losses = []
train_accuracy = []
valid_losses = []
valid_accuracy = []

for epoc in range(10):
    optimizer.zero_grad()
    output = net(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

    with open(folder_path / "checkpoint/cp_{}.pkl".format(str(epoc)), "wb") as f:
        pickle.dump(net.state_dict(), f)
