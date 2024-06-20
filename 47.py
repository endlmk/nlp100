class Morph:
    def __init__(self, surface, base, pos, pos1, pos2):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self) -> str:
        return f"Morph({", ".join(f"{key}={value}" for key, value in self.__dict__.items())})"

    def __repr__(self):
        return self.__str__()

class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs =[]
    
    def __str__(self) -> str:
        return f"Chunk({", ".join(morph.__str__() for morph in self.morphs)})"

    def __repr__(self):
        return self.__str__()
    
    def text(self):
        return ''.join([w.surface for w in self.morphs if w.pos != '補助記号'])
    
lines = []
with open('ai.ja.txt.parsed') as f:
    line = []
    src_dict = {}
    chunk = None
    for l in f.readlines():
        if l == 'EOS\n':
            if chunk != None:
                line.append(chunk)
                chunk = None
            if line:
                for ch, srcs in src_dict.items():
                    line[ch].srcs = srcs
                lines.append(line)
                line = []
                src_dict = {}
            continue
        if l == '\n':
            continue
        if l.startswith('*'):
            if chunk != None:
                line.append(chunk)
                chunk = None
            ch = l.split(' ')
            dst = int(ch[2][:-1])
            chunk = Chunk(dst)
            if dst > 0:
                src_dict.setdefault(dst, []).append(int(ch[1]))
            continue
        sp = l.split('\t')
        surface = sp[0]
        props = sp[1].split(',')
        base = props[6]
        pos = props[0]
        pos1 = props[1]
        pos2 = props[2]
        chunk.morphs.append(Morph(surface, base, pos, pos1, pos2))

corpus = []

for line in lines:
    for ch in line:
        first_verb = next((m for m in ch.morphs if m.pos == '動詞'), None)
        if first_verb is None:
            continue
        channels = [line[i] for i in ch.srcs if line[i].morphs[-1].pos == '助詞']
        sahen = next((ch for ch in channels if ch.morphs[-2].pos2 == 'サ変可能' and ch.morphs[-1].surface == 'を'), None)
        if sahen == None:
            continue
        channels.remove(sahen)
        sorted_channels =  sorted(channels, key=lambda ch: ch.morphs[-1].base)
        pos = ' '.join([ch.morphs[-1].base for ch in sorted_channels])
        channel_text = ' '.join([ch.text() for ch in sorted_channels])
        c = '\t'.join([sahen.text() + first_verb.base, pos, channel_text]) + '\n'
        corpus.append(c)

with open('corpus_47.txt', mode='w') as f:
    f.writelines(corpus)
