s = set()
with open("popular-names.txt") as file:
    with open('col1.txt', 'w') as file_col1, open('col2.txt', 'w') as file_col2:
        for line in file:
            col1 = line.split()[0]
            s.add(col1)

print(len(s))