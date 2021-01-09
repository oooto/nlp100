import pathlib
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

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
reg_list = [10**s for s in range(3,5)]
experiment_lr_list = []
experiment_gbm_list = []

for reg in reg_list:
    lr = LogisticRegression(C=reg, random_state=0)
    lr.fit(X_train, y_train)
    y_valid_pred = lr.predict(X_valid)
    y_test_pred = lr.predict(X_test)
    accuracy_list = [
        reg,
        accuracy_score(y_valid, y_valid_pred),
        accuracy_score(y_test, y_test_pred)
    ]
    experiment_lr_list.append(accuracy_list)

    gbm = GradientBoostingClassifier(learning_rate=reg, random_state=0)
    gbm.fit(X_train, y_train)
    y_valid_pred = gbm.predict(X_valid)
    y_test_pred = gbm.predict(X_test)
    accuracy_list = [
        reg,
        accuracy_score(y_valid, y_valid_pred),
        accuracy_score(y_test, y_test_pred)
    ]
    experiment_gbm_list.append(accuracy_list)

experiment_lr = pd.DataFrame(experiment_lr_list)
experiment_lr.columns = ["regular_coef", "valid_accuracy", "test_accuracy"]
idxmax_lr = experiment_lr["valid_accuracy"].idxmax()
max_lr = experiment_lr["valid_accuracy"].max()

experiment_gbm = pd.DataFrame(experiment_gbm_list)
experiment_gbm.columns = ["regular_coef", "valid_accuracy", "test_accuracy"]
idxmax_gbm = experiment_gbm["valid_accuracy"].idxmax()
max_gbm = experiment_gbm["valid_accuracy"].max()

print("検証データ上の正解率が最も高くなる")
if max_lr <= max_gbm:
    print("学習アルゴリズム: GradientBoostingClassifier")
    print("learning_rate: {}".format(experiment_gbm.at[idxmax_gbm, "regular_coef"]))
    print("評価データの正解率: {}".format(experiment_gbm.at[idxmax_gbm, "test_accuracy"]))
else:
    print("学習アルゴリズム: LogisticRegression")
    print("C: {}".format(experiment_lr.at[idxmax_lr, "regular_coef"]))
    print("評価データの正解率: {}".format(experiment_lr.at[idxmax_lr, "test_accuracy"]))



