import pandas as pd
from scipy.spatial.distance import minkowski

def minkowski_dist(x,y,p):
    distance = 0
    for i in range(len(x)):
        distance += abs(x[i] -y[i]) ** p
    return distance ** (1/p)

df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

numeric_df = df.select_dtypes(include=['int64', 'float64'])

x = numeric_df.iloc[0].tolist()
y = numeric_df.iloc[1].tolist()

distance=[]

for p in range(1,11):
    mydist = minkowski_dist(x, y, p)
    scidist = minkowski(x, y, p)
    distance.append(mydist)
    print(p, mydist, scidist)