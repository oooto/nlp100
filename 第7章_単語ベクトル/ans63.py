import pathlib

import numpy as np
import gensim
from pprint import pprint


file_path = pathlib.Path(__file__).resolve().parent / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)

vec = model["Spain"] - model["Madrid"] + model["Athens"]
ans = model.similar_by_vector(vec, topn=10)
pprint(ans)