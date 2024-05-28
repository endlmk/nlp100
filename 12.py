with open("popular-names.txt") as file:
    with open('col1.txt', 'w') as file_col1, open('col2.txt', 'w') as file_col2:
        for line in file:
            words = line.split()
            file_col1.write(words[0] + '\n')
            file_col2.write(words[1] + '\n')
