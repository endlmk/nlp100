#%%
from gensim.models import KeyedVectors
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

#%%
model = KeyedVectors.load_word2vec_format('data_source/60/GoogleNews-vectors-negative300.bin', binary=True)

#%%
with open('data_source/64/questions-words.txt') as file:
    q = file.readlines()
# %%
countries = set()
index = None
for l in q:
    if l.startswith(':'):
        if ': capital-common-countries' in l or ': capital-world' in l:
            index = 1
        elif ': currency' in l or ': gram6-nationality-adjective' in l:
            index = 0
        else:
            index = None
        continue
    
    if index is None:
        continue

    cols = l.split(' ')
    countries.add(cols[index])

# %%
countries = list(countries)
vec = [model[c] for c in countries]

# %%
tsne = TSNE(n_components=2)
c_tsne = tsne.fit_transform(np.array(vec))

#%%
plt.figure(figsize=(10, 10))
for p, c in zip(c_tsne, countries):
    plt.text(p[0], p[1], c)
plt.xlim([-15, 15])
plt.ylim([-15, 15])
plt.show()
# %%
