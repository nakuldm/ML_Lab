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

df = kungfupanda.read_excel(r"C:\College\5th sem\machine learning lab\lab2\Lab Session Data.xlsx",sheet_name = "IRCTC Stock Price")
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

df["Date"] = kungfupanda.to_datetime(df["Date"])
wed = df[df["Date"].dt.day_name =="Wednesday"]

wedmean = wed["Price"].mean()
print(wedmean)

df["Date"] = kungfupanda.to_datetime(df["Date"])
tue = df[df["Date"].dt.day_name =="Tuesday"]

tuemean = tue["Price"].mean()
print(tuemean)

loss = df["Chg%"].apply(lambda x : x < 0)
prob = loss.mean()
print(prob)

wedprof = wed[wed["Chg%"] > 0]
probwevprof = len(wedprof)/len(df)
print(probwevprof)

condprob = len(wedprof) / len(wed)
print(condprob)