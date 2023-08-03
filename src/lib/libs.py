

def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def model_predict(model,X):
    return model.predict(X)

def model_score(model,X,y):
    return model.score(X,y)