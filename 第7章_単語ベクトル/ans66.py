import pathlib

import pandas as pd
import numpy as np
import gensim
from scipy.stats import spearmanr

folder_path = pathlib.Path(__file__).resolve().parent

file_path = folder_path / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

file_path = folder_path / "wordsim353/combined.csv"
word_similarity = pd.read_csv(file_path)

tmp = []
for word1, word2 in zip(word_similarity["Word 1"], word_similarity["Word 2"]):
    tmp.append(model.similarity(word1, word2))
word_similarity["cos"] = tmp
word_similarity["human_rank"] = word_similarity["Human (mean)"].rank(method="min", ascending=False)
word_similarity["cos_rank"] = word_similarity["cos"].rank(method="min", ascending=False)

ans, pvalue = spearmanr(word_similarity["human_rank"], word_similarity["cos_rank"])
print("単語ベクトルの類似度と人間の類似度のスピアマン相関係数: {}".format(ans))
