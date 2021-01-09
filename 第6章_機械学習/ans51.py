import pathlib

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"
# データを読み出す
train = pd.read_csv(data_folder / "train.txt", sep="\t", header=None)
valid = pd.read_csv(data_folder / "valid.txt", sep="\t", header=None)
test = pd.read_csv(data_folder / "test.txt", sep="\t", header=None)

columns = ["CATEGORY", "TITLE"]
train.columns = columns
valid.columns = columns
test.columns = columns

# データを一つにする
train["TVT"] = "train"
valid["TVT"] = "valid"
test["TVT"] = "test"
df = pd.concat([train, valid, test]).reset_index(drop=True)

# コンバータ作成
bow_converter = CountVectorizer(token_pattern="(?u)\\b\\w+\\b")
bow_converter.fit(train["TITLE"])

# 禁止語作成
train_feature = bow_converter.transform(train["TITLE"])
train_feature = pd.DataFrame(train_feature.toarray(), columns=bow_converter.get_feature_names())
word_list = train_feature.sum().sort_values(ascending=False).index
length = len(word_list)
stop_words = [word for ind, word in enumerate(word_list) if (ind <= 20) or (ind >= 0.2 * length)]

df_feature = bow_converter.transform(df["TITLE"])
df_feature = pd.DataFrame(df_feature.toarray(), columns=bow_converter.get_feature_names())
df_feature.drop(stop_words, inplace=True, axis=1)
df = pd.concat([df, df_feature], axis=1)

# データ分割
train = df[df["TVT"] == "train"].drop(["TITLE", "TVT"], axis=1)
valid = df[df["TVT"] == "valid"].drop(["TITLE", "TVT"], axis=1)
test = df[df["TVT"] == "test"].drop(["TITLE", "TVT"], axis=1)

# データを書き出す
train.to_csv(data_folder / "train.feature.txt", sep="\t", index=False)
valid.to_csv(data_folder / "valid.feature.txt", sep="\t", index=False)
test.to_csv(data_folder / "test.feature.txt", sep="\t", index=False)

