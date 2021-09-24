import math
from sklearn.metrics import  mean_squared_error, mean_absolute_error, r2_score


def score_(y, pred):
    print('RMSE : ',  math.sqrt(mean_squared_error(y, pred)))
    print('MAE : ',  mean_absolute_error(y, pred))
    print('R2 : ', r2_score(y, pred) * 100)