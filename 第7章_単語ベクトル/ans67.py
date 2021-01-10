import pathlib

import pandas as pd
import gensim
from sklearn.cluster import KMeans

folder_path = pathlib.Path(__file__).resolve().parent

df = pd.read_pickle(folder_path / "analogy_data.pkl")

file_path = folder_path / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

country_list = list(set(df[df["category"] == "capital-common-countries"]["w2"].to_list()))

word_vec = pd.DataFrame()
for country in country_list:
    word_vec[country] = model[country]
word_vec = word_vec.T

kmeans_model = KMeans(n_clusters=5, random_state=0).fit(word_vec)
word_vec["label"] = kmeans_model.labels_

print(word_vec["label"])
