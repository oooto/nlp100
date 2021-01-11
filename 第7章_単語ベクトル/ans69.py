import pathlib

import pandas as pd
import gensim
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

folder_path = pathlib.Path(__file__).resolve().parent

df = pd.read_pickle(folder_path / "analogy_data.pkl")

file_path = folder_path / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

country_list = list(set(df[df["category"] == "capital-common-countries"]["w2"].to_list()))

word_vec = pd.DataFrame()
for country in country_list:
    word_vec[country] = model[country]
word_vec = word_vec.T

tsne = TSNE(n_components=2, random_state = 0)
word_vec_embedded = tsne.fit_transform(word_vec)

plt.figure(figsize=(30,30))
for ind, col in enumerate(word_vec.index.to_list()):
    plt.scatter(word_vec_embedded[ind][0], word_vec_embedded[ind][1], label=col)
plt.legend()
plt.show()

