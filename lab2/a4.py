import pandas as kungfupanda
import numpy as np

df = kungfupanda.read_excel(r"C:\College\5th sem\machine learning lab\lab2\Lab Session Data.xlsx",sheet_name="thyroid0387_UCI")

num = df.select_dtypes(include=np.number)

mean = num.mean()
print(mean)

var = num.var()
print(var)

stdv = num.std()
print(stdv)