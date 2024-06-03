import gzip, json, re

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            contents = data['text']

files = re.findall(r'\[\[ファイル:([^\|]+)(?:\|[^(\])]*)?\]\]', contents)

for file in files:
    print(file)
