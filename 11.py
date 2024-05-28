with open("popular-names.txt") as file:
    for line in file:
        print(line.replace('\t', ' ').strip())
