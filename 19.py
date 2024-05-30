
from collections import Counter

with open("popular-names.txt") as file:
    col1 = [line.strip().split('\t')[0] for line in file]

frequency = Counter(col1)

for (s, f) in frequency.most_common():
    print('\t'.join([str(f), s]))