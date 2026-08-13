import pandas as pd
import numpy as np

def mean(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total / len(x)

def variance(x):
    avg = mean(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - avg) ** 2
    return total / len(x)

def standard_deviation(x):
    return variance(x) ** 0.5

df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

numeric_df = df.select_dtypes(include=['int64', 'float64']).dropna()

data = numeric_df.to_numpy()

mymean = []
mystd = []

for j in range(data.shape[1]):
    x = data[:,j].tolist()
    mymean.append(mean(x))
    mystd.append(standard_deviation(x))

npmean = np.mean(data,axis=0)
npstd = np.std(data,axis=0)

print("My Mean:", mymean)
print("Numpy Mean:", npmean)

print("My Standard Deviation:", mystd)
print("Numpy Standard Deviation:", npstd)