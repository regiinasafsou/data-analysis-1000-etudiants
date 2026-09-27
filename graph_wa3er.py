import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("BIG_FINAL.xlsx")
plt.figure(figsize=(8,5))
colors = ["#6C5CE7", "#00B894", "#FDCB6E"]
rapport = df.groupby("Matiere")["Note"].mean()
plt.bar(rapport.index, rapport.values, color=colors)
plt.title("Portfolio Safaa - 1000 etudiants")
plt.ylabel("Mo3adal")
plt.ylim(0, 13)
for i, v in enumerate(rapport.values):
    plt.text(i, v+0.2, f"{v:.2f}", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("graph_final_pro.png", dpi=200)
print("Graph pro tsayb!")