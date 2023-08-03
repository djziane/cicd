import pytest
from joblib import load
from sklearn import svm, datasets
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

from src import lib

@pytest.fixture(scope="session")
def load_model():
    path_model = "../src/models/"
    return load(path_model+'model_svm.joblib')

@pytest.fixture(scope="session")
def load_data():
    iris = datasets.load_iris()
    X = iris.data[:, [3, 1]]
    y = iris.target
    y[y == 2] = 1
    X_trafo = SelectKBest(chi2, k=2).fit_transform(X, y)
    return train_test_split(X_trafo, y, test_size=0.33, random_state=42)

def test_conn(load_model,load_data):
    _,X_test,_,y_test=load_data
    model=load_model
    assert model.score(X_test,y_test)==1.0