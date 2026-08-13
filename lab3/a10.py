import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

x = df['Income'].dropna().tolist()

freq,bins = np.histogram(x,bins=10)

print("Mean:", mean(x))
print("Variance:", variance(x))
print("Frequency:", freq)
print("Bins:", bins)

plt.hist(x,bins=10)
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.title("Histogram of Income")
plt.show()