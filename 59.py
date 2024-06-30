import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

train = pd.read_csv('data_source/50/train.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_train = pd.read_csv('data_source/51/feature_train.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

model = LogisticRegression()
params = {
    'C': [0.5, 1, 2, 4]
}

gs = GridSearchCV(model, params, cv=5, verbose=2)
gs.fit(feature_train, train['CATEGORY'])

best_model = gs.best_estimator_
print('Accuracy test: ', best_model.score(feature_test, test['CATEGORY']) )

