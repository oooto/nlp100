import pathlib
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import japanize_matplotlib

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"

# データの読み込み
train = pd.read_csv(data_folder / "train.feature.txt", sep="\t")
valid = pd.read_csv(data_folder / "valid.feature.txt", sep="\t")
test = pd.read_csv(data_folder / "test.feature.txt", sep="\t")

X_train = train.drop(["CATEGORY"], axis=1)
y_train = train["CATEGORY"].map({'b': 0, 'e': 1, 't': 2, 'm': 3})
X_valid = valid.drop(["CATEGORY"], axis=1)
y_valid = valid["CATEGORY"].map({'b': 0, 'e': 1, 't': 2, 'm': 3})
X_test = test.drop(["CATEGORY"], axis=1)
y_test = test["CATEGORY"].map({'b': 0, 'e': 1, 't': 2, 'm': 3})

# 正解率の実験
reg_list = [10**s for s in range(-5,5)]
experiment_list = []

for reg in reg_list:
    lr = LogisticRegression(C=reg)
    lr.fit(X_train, y_train)
    y_train_pred = lr.predict(X_train)
    y_valid_pred = lr.predict(X_valid)
    y_test_pred = lr.predict(X_test)
    accuracy_list = [
        reg,
        accuracy_score(y_train, y_train_pred),
        accuracy_score(y_valid, y_valid_pred),
        accuracy_score(y_test, y_test_pred)
    ]
    experiment_list.append(accuracy_list)

experiment = pd.DataFrame(experiment_list)
experiment.columns = ["regular_coef", "train_accuracy", "valid_accuracy", "test_accuracy"]

# グラフの描写
plt.plot(experiment["regular_coef"], experiment["train_accuracy"], label="train")
plt.plot(experiment["regular_coef"], experiment["valid_accuracy"], label="valid")
plt.plot(experiment["regular_coef"], experiment["test_accuracy"], label="test")

plt.title("正則化項ごとの正解率")
plt.xlabel("正則化項")
plt.ylabel("正解率")

plt.xscale('log')
plt.legend()

plt.show()