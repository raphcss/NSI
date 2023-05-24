import csv

import matplotlib.pyplot as plt

# Création des listes pour stocker les données
TeckelX, TeckelY = [], []
SamoyedeX, SamoyedeY = [], []
BouvierBX, BouvierBY = [], []

# Ajout des chiens inconnus
chien_inconnu = [int(input('Taille de votre chien ? ')), int(input("Poids de votre chien ? "))]  # [taille, poids]

# Ajout des chiens inconnus au graphique
plt.scatter(*chien_inconnu, color='black', label='Chien inconnu')

# Récupération des données du fichier CSV
with open('knn/chien.csv', newline='') as csvfile:
    fieldnames = ['Teckel', 'Samoyede', 'Bouvier Bernois']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)

    for row in reader:
        if row['Teckel'] != 'Teckel':  # Skip the header row
            TeckelX.append(float(row['Teckel'].split(',')[0]))
            TeckelY.append(float(row['Teckel'].split(',')[1]))
            SamoyedeX.append(float(row['Samoyede'].split(',')[0]))
            SamoyedeY.append(float(row['Samoyede'].split(',')[1]))
            BouvierBX.append(float(row['Bouvier Bernois'].split(',')[0]))
            BouvierBY.append(float(row['Bouvier Bernois'].split(',')[1]))

# Création du graphique
plt.scatter(TeckelX, TeckelY, color='green', label='Teckel')
plt.scatter(SamoyedeX, SamoyedeY, color='blue', label='Samoyède')
plt.scatter(BouvierBX, BouvierBY, color='red', label='Bouvier Bernois')

plt.title("Répartition des chiens")
plt.xlabel('Taille en cm')
plt.ylabel('Poids en kg')
plt.legend()

# Affichage du graphique
plt.show()