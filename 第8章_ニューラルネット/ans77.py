import pathlib
import pickle
from tqdm import tqdm
import time

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
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

dataset = TensorDataset(X_train, y_train)

net = Net(X_train.size()[1], 4)
optimizer = optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

epoc_num = 5
elapsed_time_list = []


batch_sizes = [1, 2, 4, 8, 16, 32]
for batch_size in batch_sizes:
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    start = time.time()

    for epoc in tqdm(range(epoc_num)):
        for x, y in data_loader:
            optimizer.zero_grad()
            output = net(x)
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()

    mean_elapsed_time = (time.time() - start) / epoc_num
    elapsed_time_list.append(mean_elapsed_time)

plt.plot(elapsed_time_list)
plt.title("1エポックの学習に要する平均時間({}エポックの平均)".format(epoc_num))
plt.xlabel("バッチサイズ(2の冪乗)")
plt.ylabel("平均時間(秒)")
plt.show()
