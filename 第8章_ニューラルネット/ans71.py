import pathlib

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self, in_units, out_units):
        super(Net, self).__init__()
        self.l1 = nn.Linear(in_units, out_units)
        self.a1 = nn.Softmax()

    def forward(self, x):
        y = self.a1(self.l1(x))
        return y


# データ読み込み
folder_path = pathlib.Path(__file__).resolve().parent
X_train = pd.read_csv(folder_path / "X_train.csv")
X_train = torch.from_numpy(X_train.values.astype(np.float32))

X_1to4 = X_train[0:4]
x_1 = X_train[0]

# NN作成
net_1to4 = Net(X_1to4.size()[1], 4)
net_1 = Net(x_1.size()[0], 4)

y_1to4 = net_1to4(X_1to4)
y_1 = net_1(x_1)

print(y_1to4)
print(y_1)
