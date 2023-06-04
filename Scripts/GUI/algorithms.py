import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


data = pd.read_csv('Mexico.csv')
print(data.columns)
