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
    tmp = []
    for ind, word in enumerate(sentence):
        if word["pos"] == "名詞":
            tmp.append(word["surface"])
        else:
            if tmp != []:
                sentence_list.append(tmp)
                tmp = []
    if tmp != []:
        sentence_list.append(tmp)
    ans.append(sentence_list)

print(ans[13])