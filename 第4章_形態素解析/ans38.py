import pathlib

import japanize_matplotlib
import matplotlib.pyplot as plt
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
series_cnt = series.value_counts()

series_cnt_cnt = series_cnt.value_counts().sort_index()
max_cnt_cnt = max(series_cnt_cnt.to_list())

fig = plt.figure()
series_cnt_cnt.plot(kind="bar")

plt.title("単語の出現頻度のヒストグラム")
plt.xlabel("単語の異なり数")
plt.ylabel("出現頻度")

plt.ylim(1, max_cnt_cnt)

plt.show()
