
import sys

line_count = int(sys.argv[1])
with open("popular-names.txt") as file:
    for n in range(0, line_count):
        print(file.readline().strip())
