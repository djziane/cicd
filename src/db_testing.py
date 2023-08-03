from sklearn import svm, datasets
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
import pytest
from statistics import mean,stdev
from joblib import dump, load


from src import lib

iris = datasets.load_iris()
# #
X = iris.data[:,[3,1]]
y = iris.target
y[y == 2] = 1



# print(mean(X[1]))
# print(stdev(X[1]))
#
#
X_trafo = SelectKBest(chi2, k=2).fit_transform(X, y)
#
#
X_train, X_test, y_train, y_test = train_test_split(X_trafo, y, test_size=0.33, random_state=42)
#
# model_svm = svm.SVC(kernel='linear')
# # model_lr=LogisticRegression().fit(X_train,y_train)
# #
# model_svm.fit(X_train, y_train)
#
# path_model="models/"
# dump(model_svm, path_model+'model_svm.joblib')

# model_lr.fit(X_train,y_train)
#
path_model = "models/"
model=load(path_model + 'model_svm.joblib')
print(model.score(X_test,y_test))
# print(model_lr.score(X_test,y_test))

#print(lib.model_score(model_svm,X_test,y_test))



# def test_return_mean_data():
#     assert mean(X[1])==1.6





# def return_format_iris_data():
#     iris = datasets.load_iris()
#     X,y = iris.data,iris.target
#     y[y == 2] = 1
#     X_trafo= SelectKBest(chi2, k=2).fit_transform(X, y)
#     return X_trafo,y
#
#
# def model_train(model,X_train,y_train):
#     return model.fit(X_train,y_train)
#
# @pytest.fixture(scope="session")
# def return_split_data():
#     X_trafo,y=return_format_iris_data()
#     return train_test_split(X_trafo, y, test_size=0.33, random_state=42)
#
#
# def test_model(return_split_data):
#     X_train, X_test, y_train, y_test=return_split_data
#     model=model_train(svm.SVC(kernel='linear'),X_train,y_train)
#     assert lib.model_score(model,X_test,y_test)>0.9
