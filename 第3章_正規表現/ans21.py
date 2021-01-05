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

text_list = text.split()
content = r".*\[\[Category:.*\]\].*"
ans = [text for text in text_list if bool(re.match(content, text))]
print(ans)