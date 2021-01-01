import re

org_sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
split_list = [_str for _str in re.split(r'\s|,|\.', org_sentence) if len(_str) > 0]

def extract_chars(i, word):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0], i)
    else:
        return (word[:2], i)

ans = [extract_chars(i, w) for i, w in enumerate(split_list, 1)]
print(dict(ans))

