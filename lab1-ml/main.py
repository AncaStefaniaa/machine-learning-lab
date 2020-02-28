
def accuracy_score(y_true, y_pred, n):
    sum = 0
    for i in range(0, len(y_true)):
        if(y_pred[i] == y_true[i]):
            sum += 1
    accuracy = sum / n
    return accuracy

def precision_recall_score(y_true, y_pred, n):
    tp = 0; fp = 0; fn = 0
    for i in range(0, len(y_true)):
        if (y_pred[i] == y_true[i] == 1):
            tp += 1
        elif(y_pred[i] == 1 and y_true[i] == 0):
            fp += 1
        elif(y_pred[i] == 0 and y_true[i] == 1):
            fn += 1
    precizie = tp / (tp + fp)
    recall = tp / (tp + fn)
    #print(precizie)
    #print(recall)
    return precizie, recall

def mse(y_true, y_pred, n):
    sum = 0
    for i in range(0, len(y_true)):
        sum += (y_pred[i] - y_true[i]) ** 2
    mse = sum / n
    return mse

def mae(y_true, y_pred, n):
    sum = 0
    for i in range(len(y_true)):
        sum += abs(y_pred[i] - y_true[i])
    mae = sum / n
    return mae


if __name__ == '__main__':
    y_pred = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    y_true = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    n = len(y_true)
    print(accuracy_score(y_true, y_pred, n))
    print(precision_recall_score(y_true, y_pred, n))
    print(mse(y_true, y_pred, n))
    print(mae(y_true, y_pred, n))




