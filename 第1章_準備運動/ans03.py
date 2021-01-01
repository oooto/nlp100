import re

org_sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
split_list = re.split(r'\s|,|\.', org_sentence)
cnt_list = [len(_str) for _str in split_list if len(_str) > 0]

print(cnt_list)