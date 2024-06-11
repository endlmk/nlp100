import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

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

words = [k for k, _ in frequency_ranking[:10]]
counts = [v for _, v in frequency_ranking[:10]]

plt.bar(range(0, len(words)), counts)

font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
font_prop = fm.FontProperties(fname=font_path)
plt.xticks(range(0, len(words)), words, fontproperties = font_prop)

plt.show()