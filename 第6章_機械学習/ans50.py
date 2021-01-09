import pathlib

import pandas as pd
from sklearn.model_selection import train_test_split

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"

# ファイル読み込み
columns = ["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
df = pd.read_csv(data_folder / "newsCorpora.csv", sep="\t", header=None, names=columns)

# publisherを絞り込み、カテゴリ名と記事見出しのみにする
df = df[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"])]
df = df[["CATEGORY", "TITLE"]]

# データを分割する
train, test = train_test_split(df, test_size=0.2, shuffle=True, random_state=42)
valid, test = train_test_split(test, test_size=0.5, shuffle=True, random_state=42)

# データを書き出す
train.to_csv(data_folder / "train.txt", sep="\t", index=False, header=None)
valid.to_csv(data_folder / "valid.txt", sep="\t", index=False, header=None)
test.to_csv(data_folder / "test.txt", sep="\t", index=False, header=None)
