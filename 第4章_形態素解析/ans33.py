import pathlib

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

ans = []
for sentence in blocks:
    sentence_list = []
    word_cnd = len(sentence)
    for ind, word in enumerate(sentence):
        if (ind > 0) and (ind < word_cnd - 1):
            pre_word = sentence[ind - 1]
            next_word = sentence[ind + 1]
            if (pre_word["pos"] == "名詞") and (word["surface"] == "の") and (next_word["pos"] == "名詞"):
                a_no_b = pre_word["surface"] + word["surface"] + next_word["surface"]
                sentence_list.append(a_no_b)
    ans.append(sentence_list)


print(ans)