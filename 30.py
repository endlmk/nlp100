# # Create Mecab output.
# import MeCab

# tagger = MeCab.Tagger()

# with open('neko.txt') as file:
#     lines = file.readlines()
#     with open('neko.txt.mecab', "w") as output:
#         for l in lines:
#             result = tagger.parse(l)
#             output.write(result)


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

print(result)
