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

def chunk_replace_norm_text(ch: Chunk, replace_text: str) -> str:
    return ''.join([replace_text if m.pos == '名詞' else m.surface for m in ch.morphs])

results = []

for line in lines:
    paths = []
    for no, ch in enumerate(line):
        if any((m.pos == '名詞' for m in ch.morphs)):
            path = [no]
            ch_tmp = ch
            while ch_tmp.dst > 0:
                path.append(ch_tmp.dst)
                ch_tmp = line[ch_tmp.dst]
            paths.append(path)
    for i in range(0, len(paths)):
        for j in range(i + 1, len(paths)):
            ch_i = set(paths[i])
            ch_j = set(paths[j])
            common = ch_i.intersection(ch_j)
            concat = set(ch_j)
            concat.add(list(ch_i)[0])
            if concat == ch_i:
                results.append(' -> '.join([
                    chunk_replace_norm_text(line[list(ch_i)[0]], 'X'), 
                    chunk_replace_norm_text(line[list(ch_j)[0]], 'Y')
                    ]) + '\n')
            else:
                ch_i_diff = ch_i.difference(common)
                ch_i_diff_text = ' -> '.join([chunk_replace_norm_text(line[ch_index], 'X') if index == 0 else line[ch_index].text() for index, ch_index in enumerate(ch_i_diff)])
                ch_j_diff = ch_j.difference(common)
                ch_j_diff_text = ' -> '.join([chunk_replace_norm_text(line[ch_index], 'Y') if index == 0 else line[ch_index].text() for index, ch_index in enumerate(ch_j_diff)])
                common_text = ' -> '.join([line[index].text() for index in common])
                results.append(' | '.join([ch_i_diff_text, ch_j_diff_text, common_text]) + '\n')


with open('path_49.txt', mode='w') as f:
    f.writelines(results)