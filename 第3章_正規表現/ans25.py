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

pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}$'
extract_info = re.findall(pattern, text, re.MULTILINE + re.DOTALL)

# 下記の正規表現が理解できてない
pattern = r'^\|(.*?)=(.*?)((?=\n\|)|(?=\n$))'
resolve_info = re.findall(pattern, extract_info[0], re.MULTILINE + re.DOTALL)

ans = {tuple_[0].strip():tuple_[1].strip() for tuple_ in resolve_info}

print(ans)
