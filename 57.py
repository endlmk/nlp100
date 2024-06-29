import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

train = pd.read_csv('data_source/50/train.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_train = pd.read_csv('data_source/51/feature_train.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model: LogisticRegression = joblib.load('data_source/52/model.joblib')

pred_train = model.predict(feature_train)
report_train = classification_report(train['CATEGORY'], pred_train)
print('Classification Report train:\n', report_train)

pred_test = model.predict(feature_test)
report_test = classification_report(test['CATEGORY'], pred_test)
print('Classification Report test:\n', report_test)


for index, c in enumerate(model.classes_):
    coef = model.coef_[index]
    coef_df = pd.DataFrame({'Feature': feature_train.columns, 'Coefficient': coef})
    coef_sorted = coef_df.sort_values(by='Coefficient', ascending=False)
    print(f'Class: {c}\n')
    print(coef_sorted.head(10))
    print(coef_sorted.tail(10).iloc[::-1])

