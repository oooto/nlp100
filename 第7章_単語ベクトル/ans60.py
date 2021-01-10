import pathlib
import gensim

file_path = pathlib.Path(__file__).resolve().parent / "GoogleNews-vectors-negative300.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)
us = model["United_States"]
print(us)