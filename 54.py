import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_valid = pd.read_csv('data_source/51/feature_valid.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model: LogisticRegression = joblib.load('data_source/52/model.joblib')

pred_test = model.predict(feature_test)
accuracy_test = accuracy_score(test['CATEGORY'], pred_test)
print('Accuracy test: ', accuracy_test)

pred_valid = model.predict(feature_valid)
accuracy_valid = accuracy_score(valid['CATEGORY'], pred_valid)
print('Accuracy valid: ', accuracy_valid)