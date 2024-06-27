import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_valid = pd.read_csv('data_source/51/feature_valid.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model: LogisticRegression = joblib.load('data_source/52/model.joblib')

pred_test = model.predict(feature_test)
accuracy_test = confusion_matrix(test['CATEGORY'], pred_test)
print('Confusion Matirx test:\n', accuracy_test)

pred_valid = model.predict(feature_valid)
accuracy_valid = confusion_matrix(valid['CATEGORY'], pred_valid)
print('Confusion Matirx valid:\n', accuracy_valid)