with open("col1col2.txt", 'w') as file:
    with open('col1.txt') as file_col1, open('col2.txt') as file_col2:
        for col1 in file_col1:
            col1 = col1.strip()
            col2 = file_col2.readline()
            file.write("\t".join([col1, col2]))
