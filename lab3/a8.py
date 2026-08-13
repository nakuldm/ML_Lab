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

def dataset_statistics(data):
    means = []
    variances = []
    stds = []

    for j in range(data.shape[1]):
        x = data.iloc[:,j].tolist()
        means.append(mean(x))
        variances.append(variance(x))
        stds.append(standard_deviation(x))

    return means, variances, stds

df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

numeric_df = df.select_dtypes(include=['int64', 'float64']).dropna()

means, variances, stds = dataset_statistics(numeric_df)

print("Mean:", means)
print("Variance:", variances)
print("Standard Deviation:", stds)