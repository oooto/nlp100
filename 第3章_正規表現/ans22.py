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

find_content = r".*\[\[Category:(.*)\]\].*"
ans = re.findall(find_content, text)
print(ans)
