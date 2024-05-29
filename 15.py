import sys

line_count = int(sys.argv[1])
with open("popular-names.txt") as file:
    lines = file.readlines()

for l in lines[-line_count:]:
    print(l.strip())
