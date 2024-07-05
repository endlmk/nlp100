#%%
import pandas as pd
from gensim.models import KeyedVectors

sim = pd.read_csv('data_source/66/combined.csv')
# %%
model = KeyedVectors.load_word2vec_format('data_source/60/GoogleNews-vectors-negative300.bin', binary=True)

# %%
def get_sim(row):
    return model.similarity(row['Word 1'], row['Word 2'])

model_sim = sim.apply(get_sim, axis=1)

print(sim['Human (mean)'].corr(model_sim, 'spearman'))

