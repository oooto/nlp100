import pathlib

import japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pylab

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

res_blocks = []
for sentence in blocks:
    contain_neko = False
    sentence_append = sentence
    for word in sentence:
        if word["base"] == "猫":
            contain_neko = True
            sentence_append.remove(word)
    if contain_neko:
        res_blocks.append(sentence_append)

word_list = []
for sentence in res_blocks:
    for word in sentence:
        word_list.append(word["base"])
series = pd.Series(word_list)
series_top10 = series.value_counts().head(11)

fig = plt.figure()
series_top10.plot(kind="bar")
plt.title("猫と共起頻度が高い10語の出現頻度")
plt.xlabel("単語(原型)")
plt.ylabel("出現頻度")
plt.show()
