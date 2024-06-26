
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess(x: str):
    return x

train = pd.read_csv('data_source/50/train.txt', sep='\t')
valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')
combined = pd.concat([train, valid, test])

preprocessed = combined['TITLE'].map(lambda x: preprocess(x))
vectorizer = TfidfVectorizer()
feature = vectorizer.fit_transform(combined['TITLE'])
feature_df = pd.DataFrame(feature.toarray(), columns=vectorizer.get_feature_names_out())

feature_train = feature_df.iloc[:len(train)].reset_index(drop=True)
feature_valid = feature_df.iloc[len(train):len(train)+ len(test)].reset_index(drop=True)
feature_test = feature_df.iloc[len(train)+ len(test):].reset_index(drop=True)

feature_train.to_csv('data_source/51/feature_train.txt', sep='\t', index=False)
feature_valid.to_csv('data_source/51/feature_valid.txt', sep='\t', index=False)
feature_test.to_csv('data_source/51/feature_test.txt', sep='\t', index=False)
