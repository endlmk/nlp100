#%%
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('data_source/60/GoogleNews-vectors-negative300.bin', binary=True)

#%%
print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']))
