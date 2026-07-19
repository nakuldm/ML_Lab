import pandas as kungfupanda
import numpy as np

df = kungfupanda.read_excel(r"C:\College\5th sem\machine learning lab\lab2\Lab Session Data.xlsx",sheet_name = "Purchase data")

X = df[["Candies (#)", "Mangoes (Kg)","Milk Packets (#)"]]
Y = df["Payment (Rs)"]

rank = np.linalg.matrix_rank(X)
print(rank)

xinv = np.linalg.pinv(X)
cost = xinv @ Y
print(cost)