from sklearn.metrics import roc_auc_score



def metric():
    return roc_auc_score([1,1,0,1],[1,1,0,1])