from sklearn.metrics import roc_auc_score




#db = load_diabetes()
#X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models.
#rf = RandomForestClassifier(n_estimators=100, max_depth=6, max_features=3)
#rf.fit(X_train, y_train)
#train_acc=rf.score(X_train,y_train)
# Use the model to make predictions on the test dataset.
#predictions = rf.predict(X_test)
def metric():
    return roc_auc_score([1,1,0,1],[1,1,0,0])