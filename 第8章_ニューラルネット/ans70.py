import pathlib

import numpy as np
import pandas as pd
import gensim


def cal_title2vec(data, model):
    words = [title.split(" ") for title in data]
    words_vec = []
    for title in words:
        tmp = [np.array(model[word]) if word in model.vocab.keys() else np.zeros(shape=(model.vector_size,)) for word in title]
        words_vec.append(np.mean(np.array(tmp), axis=0))
    words_vec = pd.DataFrame(words_vec)
    return words_vec

# モデル読み込み
file_path = pathlib.Path(__file__).resolve().parent.parent / "第7章_単語ベクトル/GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

# データ読み込み
folder_path = pathlib.Path(__file__).resolve().parent.parent / "第6章_機械学習/NewsAggregatorDataset"
train = pd.read_csv(folder_path / "train.txt", sep="\t", header=None)
valid = pd.read_csv(folder_path / "valid.txt", sep="\t", header=None)
test = pd.read_csv(folder_path / "test.txt", sep="\t", header=None)

columns = ["CATEGORY", "TITLE"]
train.columns = columns
valid.columns = columns
test.columns = columns

# 特徴量行列作成
X_train = cal_title2vec(train["TITLE"], model)
X_valid = cal_title2vec(valid["TITLE"], model)
X_test = cal_title2vec(test["TITLE"], model)

# ラベルベクトル作成
y_train = train["CATEGORY"].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
y_valid = valid["CATEGORY"].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
y_test = test["CATEGORY"].map({'b': 0, 't': 1, 'e': 2, 'm': 3})

# 出力
folder_path = pathlib.Path(__file__).resolve().parent

X_train.to_csv(folder_path / "X_train.csv", index=False, header=None)
X_valid.to_csv(folder_path / "X_valid.csv", index=False, header=None)
X_test.to_csv(folder_path / "X_test.csv", index=False, header=None)

y_train.to_csv(folder_path / "y_train.csv", index=False, header=None)
y_valid.to_csv(folder_path / "y_valid.csv", index=False, header=None)
y_test.to_csv(folder_path / "y_test.csv", index=False, header=None)
