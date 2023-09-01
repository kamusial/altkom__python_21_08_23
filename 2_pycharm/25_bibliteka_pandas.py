import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
print(type(df))
print(df)
print(df.columns)

print(df.iloc[ [0, 3, 5, 12]  ,  1:4  ]  )   #po indexach
df.petallength += 100
print(df.loc[:,'petallength'])
print(df.sepalwidth)
print(df['sepalwidth'])

print(df['class'].value_counts())

df['nowa'] = (df.sepallength * 2 - df.petalwidth)


df2 = pd.read_csv('otodom.csv')
print(df2)







