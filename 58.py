import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('data_source/50/train.txt', sep='\t')
valid = pd.read_csv('data_source/50/valid.txt', sep='\t')
test = pd.read_csv('data_source/50/test.txt', sep='\t')

feature_train = pd.read_csv('data_source/51/feature_train.txt', sep='\t')
feature_valid = pd.read_csv('data_source/51/feature_valid.txt', sep='\t')
feature_test = pd.read_csv('data_source/51/feature_test.txt', sep='\t')

accuracy_train = []
accuracy_valid = []
accuracy_test = []
x = np.arange(0.2, 1.2, 0.2)
for c in x:
    model = LogisticRegression(C=c)

    model.fit(feature_train, train['CATEGORY'])

    pred_train = model.predict(feature_train)
    accuracy_train.append(accuracy_score(train['CATEGORY'], pred_train))

    pred_valid = model.predict(feature_valid)
    accuracy_valid.append(accuracy_score(valid['CATEGORY'], pred_valid))

    pred_test = model.predict(feature_test)
    accuracy_test.append(accuracy_score(test['CATEGORY'], pred_test))

plt.plot(x, accuracy_train, label='train')
plt.plot(x, accuracy_valid, label='valid')
plt.plot(x, accuracy_test, label='test')

plt.legend()

plt.show()

