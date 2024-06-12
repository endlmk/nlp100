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

neko_cooccurence = {}
for l in result:
    if not any(m['surface'] == '猫' for m in l):
        continue

    for m in l:
        if m['surface'] == '猫':
            continue
        
        word = m['surface']
        val = neko_cooccurence.get(word)
        if val == None:
            neko_cooccurence[word] = 1
        else:
            neko_cooccurence[word] = neko_cooccurence[word] + 1

neko_cooccurence_ranking = sorted(neko_cooccurence.items(), key=lambda item: item[1], reverse=True)

words = [k for k, _ in neko_cooccurence_ranking[:10]]
counts = [v for _, v in neko_cooccurence_ranking[:10]]

plt.bar(range(0, len(words)), counts)

font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc'
font_prop = fm.FontProperties(fname=font_path)
plt.xticks(range(0, len(words)), words, fontproperties = font_prop)

plt.show()