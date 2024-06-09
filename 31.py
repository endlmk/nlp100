
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

for l in result:
    for m in l:
        if m['pos'] == '動詞':
            print(m['surface'])