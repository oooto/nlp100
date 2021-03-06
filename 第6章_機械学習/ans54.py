import pathlib
import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

def predict_data(df, model, bow_converter, stop_words):
    # 説明変数作成
    df_feature = bow_converter.transform(df["TITLE"])
    df_feature = pd.DataFrame(df_feature.toarray(), columns=bow_converter.get_feature_names())
    df_feature.drop(stop_words, inplace=True, axis=1)
    df = pd.concat([df, df_feature], axis=1)
    X = df.drop(["CATEGORY", "TITLE"], axis=1)

    # 予測
    prediction = pd.DataFrame(model.predict_proba(X))
    prediction["prediction"] = lr.predict(X)

    return prediction

data_folder = pathlib.Path(__file__).resolve().parent / "NewsAggregatorDataset"

# モデル読み込み
filename = "LogisticRegression.sav"
lr = pickle.load(open(data_folder / filename, 'rb'))

# コンバータ作成
train = pd.read_csv(data_folder / "train.txt", sep="\t", header=None)
columns = ["CATEGORY", "TITLE"]
train.columns = columns
bow_converter = CountVectorizer(token_pattern="(?u)\\b\\w+\\b")
bow_converter.fit(train["TITLE"])

# 禁止語作成
train_feature = bow_converter.transform(train["TITLE"])
train_feature = pd.DataFrame(train_feature.toarray(), columns=bow_converter.get_feature_names())
word_list = train_feature.sum().sort_values(ascending=False).index
length = len(word_list)
stop_words = [word for ind, word in enumerate(word_list) if (ind <= 20) or (ind >= 0.2 * length)]

file_names = ["train", "test"]
for name in file_names:
    # データ読み込み
    df = pd.read_csv(data_folder / "{}.txt".format(name), sep="\t", header=None)
    columns = ["CATEGORY", "TITLE"]
    df.columns = columns

    # 予測
    prediction = predict_data(df, lr, bow_converter, stop_words)
    y_true = df["CATEGORY"].map({'b': 0, 'e': 1, 't': 2, 'm': 3})
    y_pred = prediction["prediction"]

    print("{} data accuracy: {}".format(name, accuracy_score(y_true, y_pred)))