import pandas as pd
import numpy as np
df=pd.read_csv('Iris.csv')
# print(df.head(10)) #question 1

# print(df.tail(15)) #question 2

# print(df.columns.tolist()) #question 3

# print(df.describe()) #question 5

# print(df.iloc[10,-1]) #question 6

print(df.iloc[9,-2]) #question 7

print(df.to_string())