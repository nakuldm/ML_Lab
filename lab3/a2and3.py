import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def label_encoder(df,column):
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df


def onehot(df,column):
    df = df.join(pd.get_dummies(df[column],prefix=column,dtype=int))
    df.drop(column,axis=1,inplace=True)
    return df


df = pd.read_excel(r"C:\College\5th sem\machine learning lab\lab3\Lab Session Data.xlsx",sheet_name='marketing_campaign')

print("before encoding:", df.shape)

df = label_encoder(df,"Education")
print(df.head())


df = onehot(df,"Marital_Status")
print(df.head())


print("after encoding:", df.shape)