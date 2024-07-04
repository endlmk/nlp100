#%%
with open('data_source/64/answers-words.txt') as file:
    ans = file.readlines()

semantic_count = 0
semantic_correct = 0
grammer_count = 0
grammer_correct = 0

for l in ans:
    if l.startswith(':'):
        grammer = l.startswith(': gram')
        continue

    s = l.split(' ')
    correct = s[3] == s[4]
    if grammer:
        grammer_count = grammer_count + 1
        if correct:
            grammer_correct = grammer_correct + 1
    else:
        semantic_count = semantic_count + 1
        if correct:
            semantic_correct = semantic_correct + 1

print(f'semantic correct: {semantic_correct / semantic_count * 100}%')
print(f'grammer correct: {grammer_correct / grammer_count * 100}%')

        
