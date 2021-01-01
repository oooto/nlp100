import re

def ngram(seq, n):
    return [seq[i: i+n] for i in range(len(seq)-n+1)]

org_sentence = "I am an NLPer"

split_list = [_str for _str in re.split(r'\s|,|\.', org_sentence) if len(_str) > 0]
print("単語bi-gram: {}".format(ngram(split_list, 2)))

print("文字bi-gram: {}".format(ngram(org_sentence, 2)))