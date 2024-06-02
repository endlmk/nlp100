import gzip, json, re

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            contents = data['text']

sections = re.findall(r'^=.*=$', contents, re.MULTILINE)

for section in sections:
    section_name = section.replace("=", "")
    level = (len(section) - len(section_name)) // 2 - 1
    print(section_name, level)
