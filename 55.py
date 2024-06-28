import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

train = pd.read_csv('data_source/50/train.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_train = pd.read_csv('data_source/51/feature_train.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model: LogisticRegression = joblib.load('data_source/52/model.joblib')

pred_train = model.predict(feature_train)
accuracy_train = confusion_matrix(train['CATEGORY'], pred_train)
print('Confusion Matirx train:\n', accuracy_train)

pred_test = model.predict(feature_test)
accuracy_test = confusion_matrix(test['CATEGORY'], pred_test)
print('Confusion Matirx test:\n', accuracy_test)
