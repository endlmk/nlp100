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

frequency_histogram = {}

for frequency in frequency_ranking:
    count = frequency[1]
    kinds = frequency_histogram.get(count)
    if kinds == None:
        frequency_histogram[count] = 1
    else:
        frequency_histogram[count] = kinds + 1

counts = [item[0] for item in frequency_histogram.items()]
kinds = [item[1] for item in frequency_histogram.items()]

plt.bar(counts, kinds)

plt.show()