import sys

split_count = int(sys.argv[1])
with open("popular-names.txt") as file:
    lines = file.readlines()

split_lines = (len(lines) + split_count - 1) // split_count

for i in range(0, split_count):
    with open(f'split_{i + 1}', 'w') as f:
        start = split_lines * i
        end = len(lines) if i == (split_count - 1) else split_lines * (i + 1)
        f.writelines(lines[start:end])

