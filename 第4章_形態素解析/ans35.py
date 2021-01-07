import pathlib
import pandas as pd

file_path = pathlib.Path(__file__).resolve().parent / 'neko.txt.mecab'
with open(file_path, encoding="utf-8") as f:
    strs = f.read().split("EOS\n")

strs = [s for s in strs if s != ""]
blocks = []
for sentences in strs:
    sentence_list = [s for s in sentences.split("\n") if s != ""]
    expand_sentence_list = []
    for sentence in sentence_list:
        name, attr = sentence.split("\t")
        attr = attr.split(",")
        sentence_dict = {
            "surface": name,
            "base": attr[6],
            "pos": attr[0],
            "pos1": attr[1]
        }
        expand_sentence_list.append(sentence_dict)
    blocks.append(expand_sentence_list)

word_list = []
for sentence in blocks:
    for word in sentence:
        word_list.append(word["base"])
series = pd.Series(word_list)

print(series.value_counts())