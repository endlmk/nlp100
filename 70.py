#%%
from gensim.models import KeyedVectors
import numpy as np
import pandas as pd
import re

#%%
model = KeyedVectors.load_word2vec_format('data_source/60/GoogleNews-vectors-negative300.bin', binary=True)

train = pd.read_csv('data_source/50/train.txt', sep='\t')
valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

# %%
def average_word_vec(title:str):
    cleaned_text_with_spaces = re.sub(r'[^a-zA-Z\s]', '', title)
    words = cleaned_text_with_spaces.split()
    vec = [model[w] for w in words if w in model]
    return np.array(sum(vec) / len(vec))
average_word_vec('PRECIOUS-Gold ends flat as S&P 500 rises; platinum up')
# %%
x_train = train['TITLE'].apply(average_word_vec)
x_valid = valid['TITLE'].apply(average_word_vec)
x_test = test['TITLE'].apply(average_word_vec)

def convert_category(c:str):
    if c == 'b':
        return 0
    if c == 't':
        return 1
    if c == 'e':
        return 2
    if c == 'm':
        return 3

y_train = train['CATEGORY'].apply(convert_category)
y_valid = valid['CATEGORY'].apply(convert_category)
y_test = test['CATEGORY'].apply(convert_category)
# %%
import torch
x_train_tensor = torch.tensor(x_train)
x_valid_tensor = torch.tensor(x_valid)
x_test_tensor = torch.tensor(x_test)
y_train_tensor = torch.tensor(y_train)
y_valid_tensor = torch.tensor(y_valid)
y_test_tensor = torch.tensor(y_test)

torch.save(x_train_tensor, 'data_source/70/train_feature.pt')
torch.save(x_valid_tensor, 'data_source/70/valid_feature.pt')
torch.save(x_test_tensor, 'data_source/70/test_feature.pt')
torch.save(y_train_tensor, 'data_source/70/train_label.pt')
torch.save(y_valid_tensor, 'data_source/70/valid_label.pt')
torch.save(y_test_tensor, 'data_source/70/test_label.pt')


# %%
