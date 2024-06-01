import gzip, json, re

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            contents = data['text']

categories = re.findall(r'^\[\[Category:(.*)\]\]$', contents, re.MULTILINE)

for line in categories:
    print(line)
