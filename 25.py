from collections import OrderedDict
import gzip, json, re

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            contents = data['text']

template = re.findall(r'^\{\{基礎情報.*?\n(.*?)\}\}\n$', contents, re.MULTILINE + re.VERBOSE + re.DOTALL)[0]

dict = OrderedDict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template, re.MULTILINE + re.VERBOSE + re.DOTALL))
print(dict)