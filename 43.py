
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

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
        chunk.morphs.append(Morph(surface, base, pos, pos1))

dependencies = [ch.text() + '\t' + l[ch.dst].text() for l in lines for ch in l 
                if any(m.pos == '名詞' for m in ch.morphs) and any(m.pos == '動詞' for m in l[ch.dst].morphs)]
print(dependencies)
