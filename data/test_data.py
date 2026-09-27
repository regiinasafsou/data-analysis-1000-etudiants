import pandas as pd

df = pd.read_csv('data/ventes.csv')
print(df)
print(df['Ventes'].sum())
print("Moyenne:")
print(df['Ventes'].mean())

print("Akbar vente:")
print(df['Ventes'].max())
