import pathlib
import pickle
from tqdm import tqdm

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score


class Net(nn.Module):
    def __init__(self, in_units, hidden_units, out_units):
        super(Net, self).__init__()
        self.l1 = nn.Linear(in_units, hidden_units)
        self.a11 = nn.ReLU()
        self.a12 = nn.BatchNorm1d(hidden_units)
        self.l2 = nn.Linear(hidden_units, hidden_units)
        self.a21 = nn.ReLU()
        self.a22 = nn.BatchNorm1d(hidden_units)
        self.l3 = nn.Linear(hidden_units, out_units)

    def forward(self, x):
        x = self.a12(self.a11(self.l1(x)))
        x = self.a22(self.a21(self.l2(x)))
        x = self.l3(x)
        return x

dev = torch.device('cuda')

# データ準備
folder_path = pathlib.Path(__file__).resolve().parent

X_train = pd.read_csv(folder_path / "X_train.csv", header=None)
X_train = torch.from_numpy(X_train.values.astype(np.float32)).to(dev)

X_valid = pd.read_csv(folder_path / "X_valid.csv", header=None)
X_valid = torch.from_numpy(X_valid.values.astype(np.float32)).to(dev)

X_test = pd.read_csv(folder_path / "X_test.csv", header=None)
X_test = torch.from_numpy(X_test.values.astype(np.float32)).to(dev)

y_train = pd.read_csv(folder_path / "y_train.csv", header=None)
y_train = torch.tensor(y_train[0].to_list()).to(dev)

y_valid = pd.read_csv(folder_path / "y_valid.csv", header=None)
y_valid = torch.tensor(y_valid[0].to_list()).to(dev)

y_test = pd.read_csv(folder_path / "y_test.csv", header=None)
y_test = torch.tensor(y_test[0].to_list()).to(dev)

dataset = TensorDataset(X_train, y_train)

net = Net(X_train.size()[1], 100, 4).to(dev)
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

epoc_num = 100
batch_size = 128

data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

train_losses = []
train_accuracy = []
valid_losses = []
valid_accuracy = []

for epoc in tqdm(range(epoc_num)):
    for x, y in data_loader:
        optimizer.zero_grad()
        output = net(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()

    train_losses.append(criterion(net(X_train), y_train))
    _, y_train_pred = torch.max(net(X_train), 1)
    train_accuracy.append(accuracy_score(y_train_pred.to('cpu').numpy(), y_train.to('cpu').numpy()))

    valid_losses.append(criterion(net(X_valid), y_valid))
    _, y_valid_pred = torch.max(net(X_valid), 1)
    valid_accuracy.append(accuracy_score(y_valid_pred.to('cpu').numpy(), y_valid.to('cpu').numpy()))

plt.plot(train_losses, label='train loss')
plt.plot(valid_losses, label='valid loss')
plt.title("クロスエントロピー")
plt.xlabel("エポック")
plt.ylabel("クロスエントロピー")
plt.legend()
plt.show()

plt.plot(train_accuracy, label='train accuracy')
plt.plot(valid_accuracy, label='valid accuracy')
plt.title("正解率")
plt.xlabel("エポック")
plt.ylabel("正解率")
plt.legend()
plt.show()

_, y_train_pred = torch.max(net(X_train), 1)
train_acc = accuracy_score(y_train_pred.to('cpu').numpy(), y_train.to('cpu').numpy())
_, y_valid_pred = torch.max(net(X_valid), 1)
valid_acc = accuracy_score(y_valid_pred.to('cpu').numpy(), y_valid.to('cpu').numpy())
_, y_test_pred = torch.max(net(X_test), 1)
test_acc = accuracy_score(y_test_pred.to('cpu').numpy(), y_test.to('cpu').numpy())
print("学習データの正解率:{}".format(train_acc))
print("検証データの正解率:{}".format(valid_acc))
print("評価データの正解率:{}".format(test_acc))