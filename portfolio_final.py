import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Kansayb data kbira...")
n = 1000
df = pd.DataFrame({
    "ID": range(1, n+1),
    "Ville": np.random.choice(["Rabat","Casa","Sale"], n),
    "Matiere": np.random.choice(["Math","Info","Anglais"], n),
    "Note": np.round(np.random.normal(11.5, 3.5, n).clip(0, 20), 2),
    "Ventes": np.random.randint(100, 2000, n)
})

# Ndiro khawi
df.loc[np.random.choice([True, False], n, p=[0.08, 0.92]), "Note"] = None

# Nne9i
df["Note"] = df.groupby("Matiere")["Note"].transform(lambda x: x.fillna(x.mean()))

# Mention
df["Resultat"] = df["Note"].apply(lambda x: "Naja7" if x >= 10 else "Rassib")

# Rapport
print(df.groupby("Matiere")["Note"].mean())
print(df["Resultat"].value_counts())

# Graph
df.groupby("Matiere")["Note"].mean().plot(kind="bar")
plt.title("Portfolio Safaa - 1000 etudiants")
plt.savefig("graph.png")

# Final
df.to_excel("BIG_FINAL.xlsx", index=False)
print("✅ Sala l projet! 3 fichiers tsaybo: graph.png + BIG_FINAL.xlsx")