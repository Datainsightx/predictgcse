import pandas as pd
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
#=============================================================================================================================
# Import Data
#=============================================================================================================================

train = pd.read_csv("c:/python34/Scripts/Y112015fulldataAddSci.csv")

#Features to be used for training

train = train.drop('Name', 1)
train = train.drop('CoreSciGCSE',1)
train = train.drop('AddSciGCSE',1)

#train = train.drop('Y11 AM4',1)
#train = train.drop('Y11 AM3',1)
#train = train.drop('Y11 AM2',1)
#train = train.drop('Y11 Mock1',1)
#train = train.drop('Y11 AM1',1)


train = train.drop('Attendance',1)
train = train.drop('CAT',1)
train = train.drop('KS2',1)
train = train.drop('Target',1)
train = train.drop('Y10 Mock',1)
train = train.drop('Group',1)
train = train.drop('SEN',1)
train = train.drop('PP',1)
train = train.drop('AM3',1)
train = train.drop('AM4',1)
train = train.drop('AM5',1)
train = train.drop('AM6',1)

y = train['Class'] #Target to use for training algorithm. Change this, depending on what you want to predict
del train['Class']

x = train

#===============================================================================================================
#Load test data for predictions

test = pd.read_csv("c:/python34/Scripts/2017AddSci.csv")
test2 = pd.read_csv("c:/python34/Scripts/11u1data.csv")
test1 = pd.concat([test, test2], axis=0)

test_id = test1['Name']
test1 = test1.drop('Name', 1)

#Year 11 features
#test1 = test1.drop('Y11 AM4',1)
#test1 = test1.drop('Y11 AM3',1)
#test1 = test1.drop('Y11 AM2',1)
#test1 = test1.drop('Y11 Mock1',1)
#test1 = test1.drop('Y11 AM1',1)

#Year 10 features

test1 = test1.drop('Attendance',1)
test1 = test1.drop('CAT',1)
test1 = test1.drop('KS2',1)
test1 = test1.drop('Target',1)
test1 = test1.drop('Y10 Mock',1)

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC

lsvc = LinearSVC(C=0.2, penalty="l1", dual=False).fit(x, y)

model = SelectFromModel(lsvc, prefit=True)

X_new = model.transform(x)
new_data = model.transform(test1)


#====================================================================================================================
# Split data into train and validation sets

X_train, X_val, y_train, y_val = cross_validation.train_test_split(X_new, y, train_size=0.80, random_state=42)
#===========================================================================================================================
#Algorithm will train a model using the training data

clf = GaussianNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_val)

from sklearn.externals import joblib
from sklearn.metrics import classification_report

print(classification_report(y_val, y_pred))
print(y_val)
print(y_pred)


GCSE_pred = clf.fit(X_train, y_train).predict(new_data)

#pd.DataFrame({"Student": test_id, "Predictions": GCSE_pred}).to_csv('NB_predictionscorescijuly25.csv',index=False)

print("Dumping webmodel and webmodel_columns...")

webmodel_columns = list(x.columns)
joblib.dump(webmodel_columns, 'webmodel_columns.pkl')
joblib.dump(clf, 'webmodel.pkl')

