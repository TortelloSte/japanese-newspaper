import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./data/japanese_news.csv', sep= '\t')
# print(df.head())

df = df.drop(['title', 'author'], axis = 1)
print(df.head())

if not os.path.exists('grafici'):
    os.makedirs('grafici')
# grafico 1 

df['year'] = pd.to_datetime(df['date']).dt.year

articles_per_year = df['year'].value_counts().sort_index()

plt.figure(figsize=(12, 8))
sns.barplot(x=articles_per_year.index, y=articles_per_year.values, color='skyblue')
plt.xlabel('Anno') # divisione per anni
plt.ylabel('Numero di articoli')
plt.title('Distribuzione degli articoli per anno')

plt.savefig('grafici/distribuzione_articoli_anno.png')
plt.close()

# grafico 2
articles_per_source = df['source'].value_counts()

plt.figure(figsize=(12, 8))
sns.barplot(x=articles_per_source.index, y=articles_per_source.values, color='skyblue')
plt.xlabel('Fonte')
plt.ylabel('Numero di articoli')
plt.title('Numero di articoli per fonte')
plt.xticks(rotation=45)
plt.savefig('grafici/numero_articoli_fonte.png')
plt.close()
