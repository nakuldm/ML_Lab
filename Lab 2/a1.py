import pandas as kungfupanda
import numpy as np

df = kungfupanda.read_excel(r"C:\Users\ishaa\Downloads\Lab Session Data (1).xlsx",sheet_name = "Purchase data")

X = df[["Candies (#)", "Mangoes (Kg)","Milk Packets (#)"]]
Y = df["Payment (Rs)"]

rank = np.linalg.matrix_rank(X)
print(rank)

xinv = np.linalg.pinv(X)
cost = xinv @ Y
print(cost)