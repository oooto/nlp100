import pathlib

import pandas as pd
import gensim
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

folder_path = pathlib.Path(__file__).resolve().parent

df = pd.read_pickle(folder_path / "analogy_data.pkl")

file_path = folder_path / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

country_list = list(set(df[df["category"] == "capital-common-countries"]["w2"].to_list()))

word_vec = pd.DataFrame()
for country in country_list:
    word_vec[country] = model[country]
word_vec = word_vec.T

result = linkage(word_vec, metric="euclidean", method="ward")

dendrogram(result, labels=word_vec.index)
plt.title("Dedrogram")
plt.ylabel("Threshold")
plt.show()
