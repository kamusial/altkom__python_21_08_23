import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('otodom.csv')
print(df.head(10).to_string())   #wyświetlenie 10 pierwszych wierszy
print(df.describe().to_string())   #wyświetl dane o danych
df = df.iloc[:, 1:]     #wycinam pierwszą kolumnę
print(df.corr())   #korelacja
# sns.heatmap(df.corr(), annot=True)    #mapa ciepla
# plt.show()     #wyswietl
#
# sns.histplot(df.cena)    #histogram
# plt.show()

_min = df.describe().loc['min','cena']  #wyciągam ceny
q1 = df.describe().loc['25%','cena']
q3 = df.describe().loc['75%','cena']

df1 = df[(df.cena >= _min) & (df.cena <= q3) & (df.rok_budowy < df.describe().loc['max','rok_budowy'])]  #bez njtańszych i bez najdrozszych
sns.histplot(df1.cena)    #histogram
plt.show()

plt.scatter(df.powierzchnia, df.cena)
plt.show()

df1.to_csv('nowy_plik.csv', index=False, encoding='utf-8')   #zapis do csv