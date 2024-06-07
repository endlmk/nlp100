import gzip, json, re, requests

def remove_emphasis(text:str) -> str:
    return re.sub(r'\'{2,5}', '', text)

def replace(match):
    return match.group(2) if match.group(2) else match.group(1)

def replace_internal_link(text:str) -> str:
    return re.sub(r'\[\[(?!ファイル)([^\|\]]+)(?:\|([^\]]+))?\]\]', replace, text)

with gzip.open("jawiki-country.json.gz", 'rt') as file:
    for line in file:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            contents = data['text']

template = re.findall(r'^\{\{基礎情報.*?\n(.*?)\}\}\n$', contents, re.MULTILINE + re.VERBOSE + re.DOTALL)[0]
# print(re.findall(r'\[\[(?!ファイル)(?:[^\|]+?\|)??([^\|]+?)\]\]', template, re.MULTILINE))
fields = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template, re.MULTILINE + re.VERBOSE + re.DOTALL)

dict = {k:replace_internal_link(remove_emphasis(v)) for k, v in fields}
print(dict['国旗画像'])

mediawiki_api_endpoint = 'https://en.wikipedia.org/w/api.php'
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f'File:{dict['国旗画像'].replace(' ', '_')}',
    "iiprop": 'url'
}

response = requests.session().get(url=mediawiki_api_endpoint, params=params)
data = response.json()
_, val = next(iter(data['query']['pages'].items()))
print(val['imageinfo'][0]['url'])