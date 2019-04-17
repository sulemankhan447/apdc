import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)
import numpy as np
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('./datasets/after_chi_sqr_0.01.csv')

df = df.iloc[:, np.array([-1,0,1,3,4,10,13,16]) + 1]
print (df.columns)

df['Dependent.Company.Status'] = pd.DataFrame(label_binarize(df['Dependent.Company.Status'], classes = ['FAILED','SUCCESS']))

train = df[df['Dependent.Company.Status'] == 1].head(115)
train = train.append(df[df['Dependent.Company.Status'] == 0].head(115))

test = pd.concat([df, train])
test = test.drop_duplicates(keep = False)

train = train.drop('Company_Name', axis = 1)
test = test.drop('Company_Name', axis = 1)

x_train, y_train = train.ix[:, 1:], train.ix[:, 0]
x_test, y_test = test.ix[:, 1:], test.ix[:, 0]
x_train.iloc[:, 1:] = x_train.iloc[:, 1:].apply(LabelEncoder().fit_transform)
x_test.iloc[:, 1:] = x_test.iloc[:, 1:].apply(LabelEncoder().fit_transform)

print (x_train.head(50))
print (y_train.head(50))

logit = LogisticRegression()
logit.fit(x_train, y_train)

print ('accuracy score: ', logit.score(x_test, y_test))
print ('precision:', precision_score(y_test, logit.predict(x_test), average='weighted'))
print ('recall:', recall_score(y_test, logit.predict(x_test), average='weighted'))
print ('mean cross validation score:', np.mean(cross_val_score(logit, pd.concat([x_train, x_test]), pd.concat([y_train, y_test]))))

for i in range(1, 20):
    clf = AdaBoostClassifier(n_estimators= i, base_estimator=logit)
    clf.fit(x_train, y_train)
    score = clf.score(x_test, y_test)
    precision = precision_score(y_test, clf.predict(x_test), average='weighted')
    recall = recall_score(y_test, clf.predict(x_test), average='weighted')
    cross_val_mean = np.mean(cross_val_score(clf, pd.concat([x_train, x_test]), pd.concat([y_train, y_test])))
    print (i, score , precision, recall, cross_val_mean)



