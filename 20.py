import gzip, json

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            print(data['text'])
