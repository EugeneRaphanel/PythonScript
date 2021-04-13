#Read a file and print it 
import pandas as pd
df = pd.read_csv (r'culvert_data.csv')
#mean value
print("Le diametre moyen est :", df['diameter'].mean())


count_per_type = df["type"].value_counts()
# On crée un camembert pour montrer la répartition des culverts par type
ax = count_per_type.plot.pie()
fig = ax.get_figure()
# Et on l'enregistre
fig.savefig("culvert_per_type.png")
