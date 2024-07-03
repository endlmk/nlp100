#%%
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('data_source/60/GoogleNews-vectors-negative300.bin', binary=True)

#%%
with open('data_source/64/questions-words.txt') as file:
    q = file.readlines()

#%%
ans = []
for l in q:
    if l.startswith(':'):
        ans.append(l)
        continue
    
    l = l.strip('\n')
    words = l.split(' ')
    s = model.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)[0]
    ans.append(' '.join([l, s[0], str(s[1])]) + '\n')

with open('data_source/64/answers-words.txt', mode='w') as file:
    file.writelines(ans)

