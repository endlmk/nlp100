
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self) -> str:
        return f"({", ".join(f"{key}={value}" for key, value in self.__dict__.items())})"

    def __repr__(self):
        return self.__str__()
    
lines = []
with open('ai.ja.txt.parsed') as f:
    line = []
    for l in f.readlines():
        if l == 'EOS\n':
            if line:
                lines.append(line)
                line = []
            continue
        if l.startswith('*') or l == '\n':
            continue
        sp = l.split('\t')
        surface = sp[0]
        props = sp[1].split(',')
        base = props[6]
        pos = props[0]
        pos1 = props[1]
        line.append(Morph(surface, base, pos, pos1))

print(lines[1])

