import pathlib
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"

# データの読み込み
train = pd.read_csv(data_folder / "train.feature.txt", sep="\t")
y = train["CATEGORY"].map({'b': 0, 'e': 1, 't': 2, 'm': 3})
X = train.drop(["CATEGORY"], axis=1)

# モデル作成
lr = LogisticRegression()
lr.fit(X, y)

# モデル出力
filename = "LogisticRegression.sav"
pickle.dump(lr, open(data_folder / filename, 'wb'))
