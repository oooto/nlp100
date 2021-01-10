import pathlib

import numpy as np
import gensim

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

file_path = pathlib.Path(__file__).resolve().parent / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)
ans = cos_sim(model["United_States"], model["U.S."])
print(ans)