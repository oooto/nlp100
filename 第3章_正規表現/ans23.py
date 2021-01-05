import gzip
import json
import pathlib
import re

file_path = pathlib.Path(__file__).resolve().parent / "jawiki-country.json.gz"

with gzip.open(file_path, 'r') as f:
    for line in f:
        obj = json.loads(line)
        if obj["title"] == "イギリス":
            text = obj["text"]

find_content = r"={2,}.*={2,}"
find_content2 = r"(={2,}).*={2,}"
ans = {}
for section in re.findall(find_content, text):
    for equal in re.findall(find_content2, section):
        ans[section] = len(equal) - 1

print(ans)