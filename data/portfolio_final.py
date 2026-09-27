import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATA  1000 eleves
print("Kansayb data")

n = 1000
df = pd.DataFrame({
    "ID": range(1, n+1),
    "Nom": [f"Etudiant_{i}" for i in range(1, 1001)],
    "Ville": np.random.choice(["Rabat","Casa","Marrakech","Tanger","Fes","Sale"], n),
    "Niveau": np.random.choice(["S1","S2","S3","S4"], n),
    "Matiere": np.random.choice(["Math","Physique","Info","Anglais","Francais","Economie"], n),
    "Note": np.round(np.random.normal(11.5, 3.5, n).clip(0, 20), 2),
    "Heures_Etude": np.random.randint(1, 20, n),
    "Absences": np.random.randint(0, 10, n)
})

# 8% vide
df.loc[np.random.choice([True, False], n, p=[0.08, 0.92]), "Note"] = None
df.to_csv("big_data_notes.csv", index=False)
print(f"✅ 1- Fichier CSV tsayb: {df.shape[0]} tilmid")

# nettoyage
df["Note"] = df.groupby("Matiere")["Note"].transform(lambda x: x.fillna(x.mean()))
print("✅ 2- N9it data - 3emert lkhawi b mo3adal dyal kola matiere")

# MENTION 
def n3ti_mention(note):
    if note >= 16: return "Momtaz"
    elif note >= 12: return "Mzyan"
    elif note >= 10: return "Ma9boul"
    else: return "Rassib"

df["Mention"] = df["Note"].apply(n3ti_mention)
df["Resultat"] = df["Note"].apply(lambda x: "Naja7" if x >= 10 else "Rassib")

#  RAPPORT 
rapport = df.groupby("Matiere")["Note"].mean().sort_values(ascending=False)
print("\n📊 Rapport:")
print(rapport)

# GRAPH 
rapport.plot(kind="bar", color="#6C5CE7")
plt.title("Projet Safaa - Mo3adal 7asab Matiere (1000 etudiants)")
plt.ylabel("Mo3adal")
plt.tight_layout()
plt.savefig("graph.png")
print("✅ 3- Graph tsayb: graph.png")

#  FINAL EXCEL
df.to_excel("BIG_FINAL.xlsx", index=False)
print("✅ 4- Excel final tsayb: BIG_FINAL.xlsx")
print("\n wajed!")