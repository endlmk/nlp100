with open("popular-names.txt") as file:
    lines = [line.strip().split('\t') for line in file]

lines.sort(key=lambda x: int(x[2]))

for l in lines:
    print('\t'.join(l))

