import numpy as np
import pandas as pd

data = pd.read_csv("./data/entries.csv")

X = data[["x1", "x2"]]
Y = data["y"]

print(X)
print(Y)

def train_test_split_data(X, Y, ratio=0.8):
    
    X_train = X[]
    X_test = X[]
    y_test = y[]
    y_tain = y[]

    return X_train, Y_train, X_test, Y_test