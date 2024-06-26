import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_valid = pd.read_csv('data_source/51/feature_valid.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model: LogisticRegression = joblib.load('data_source/52/model.joblib')
pred_proba = model.predict_proba(feature_test)

pred = pd.DataFrame(pred_proba, columns=model.classes_)

pred.to_csv('data_source/53/pred.txt', sep='\t', index=False)
