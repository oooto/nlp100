import pathlib
import pickle

import pandas as pd

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"

# モデル読み込み
filename = "LogisticRegression.sav"
lr = pickle.load(open(data_folder / filename, 'rb'))

train_feature = pd.read_csv(data_folder / "train.feature.txt", sep="\t")
cols = list(train_feature.columns)
cols.remove("CATEGORY")
categories = ["b", "e", "t", "m"]

coef = pd.DataFrame(lr.coef_)
coef.columns = cols
coef = coef.T
coef.columns = categories

for cat in categories:
    print("category {}: 重みの高い特徴量トップ10".format(cat))
    print(coef[cat].sort_values(ascending=False).head(10))
    print("category {}: 重みの低い特徴量トップ10".format(cat))
    print(coef[cat].sort_values(ascending=True).head(10))