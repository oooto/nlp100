import pathlib

import pandas as pd
import numpy as np
import gensim
from pprint import pprint

folder_path = pathlib.Path(__file__).resolve().parent
file_path = folder_path / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

file_path = folder_path / "questions-words.txt"
tmp_list = []
cnt = 0
with open(file_path, "r") as f:
    for line in f:
        line = line.split()
        if line[0] == ":":
            category = line[1]
        else:
            word, cos = model.most_similar(positive=[line[1], line[2]], negative=[line[0]], topn=1)[0]
            tmp = [category, line[0], line[1], line[2], line[3], word, cos]
            tmp_list.append(tmp)
            cnt = cnt + 1
            print("{} / 19544".format(cnt))

df = pd.DataFrame(tmp_list)
df.columns = [
    "category",
    "w1",
    "w2",
    "w3",
    "w4",
    "word",
    "cos"
]
df.to_pickle(folder_path / "analogy_data.pkl")
