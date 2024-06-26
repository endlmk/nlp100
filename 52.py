import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('data_source/50/train.txt', sep='\t')
valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_train = pd.read_csv('data_source/51/feature_train.txt', sep='\t')
feature_valid = pd.read_csv('data_source/51/feature_valid.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model = LogisticRegression()

model.fit(feature_train, train['CATEGORY'])

joblib.dump(model, 'data_source/52/model.joblib')