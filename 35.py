
with open('neko.txt.mecab') as file:
    result = []
    line_m =[]
    for line in file:
        if line == 'EOS\n':
            if len(line_m) > 0:
                result.append(line_m)
                line_m =[]
            continue
        
        features = line.split('\t')
        pos = features[4].split('-')
        mapping = {
            'surface': features[0],
            'base': features[3],
            'pos': pos[0],
            'pos1': pos[1] if len(pos) > 1 else ''
        }
        line_m.append(mapping)

frequency = {}
for l in result:
    for m in l:
        word = m['surface']
        val = frequency.get(word)
        if val == None:
            frequency[word] = 1
        else:
            frequency[word] = frequency[word] + 1

frequency_ranking = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

print(frequency_ranking[:10])
