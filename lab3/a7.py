import pandas as pd
import numpy as np

def dot_product(x,y):
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
    return result

def euclidean_norm(x):
    result = 0
    for i in range(len(x)):
        result += x[i] ** 2
    return result ** 0.5

df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

numeric_df = df.select_dtypes(include=['int64', 'float64'])

x = numeric_df.iloc[0].tolist()
y = numeric_df.iloc[1].tolist()

mydot = dot_product(x,y)
npdot = np.dot(x,y)

mynorm = euclidean_norm(x)
npnorm = np.linalg.norm(x)

print("Dot Product:", mydot, npdot)
print("Euclidean Norm:", mynorm, npnorm)