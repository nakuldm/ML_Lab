import pandas as kungfupanda
import numpy as np

def mean(x):
    return sum(x)/len(x)

def var(x):
    m = mean(x)
    total = 0

    for n in x:
        total += (n-m) ** 2

    return total / len(x)

df = kungfupanda.read_excel(r"C:\Users\ishaa\Downloads\Lab Session Data (1).xlsx",sheet_name = "IRCTC Stock Price")
price = df["Price"]

print(price)

meanpack = np.mean(price)
meanme = mean(price)

varpack = np.var(price)
varme = var(price)

print(f"{meanpack:.50f}")
print(f"{meanme:.50f}")

print(f"{varpack:.50f}")
print(f"{varme:.50f}")