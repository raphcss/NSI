import csv
import math

import matplotlib.pyplot as plt


# Mission 3 :
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mission 4:
def liste_distances(Xs, Ys, X, Y):
    return [dist(X, Y, x, y) for x, y in zip(Xs, Ys)]


# Création des listes pour stocker les données
TeckelX, TeckelY = [], []
SamoyedeX, SamoyedeY = [], []
BouvierBX, BouvierBY = [], []

# Ajout des chiens inconnus
chien_inconnu = [int(input('Taille de votre chien ? ')), int(input("Poids de votre chien ? "))]  # [taille, poids]

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

# Calculer les distances pour chaque chien
liste_Teckel = liste_distances(TeckelX, TeckelY, *chien_inconnu)
liste_Samoyede = liste_distances(SamoyedeX, SamoyedeY, *chien_inconnu)
liste_BouvierB = liste_distances(BouvierBX, BouvierBY, *chien_inconnu) 

# Création du graphique
plt.scatter(TeckelX, TeckelY, color='green', label='Teckel')
plt.scatter(SamoyedeX, SamoyedeY, color='blue', label='Samoyède')
plt.scatter(BouvierBX, BouvierBY, color='red', label='Bouvier Bernois')
plt.scatter(*chien_inconnu, color='black', label='Chien inconnu')

plt.title("Répartition des chiens")
plt.xlabel('Taille en cm')
plt.ylabel('Poids en kg')
plt.legend()

# Affichage du graphique
plt.show()

assert liste_distances([0,3,-1,-3,-4,20,19,21,20],[-20,-18,-21,-16,-19,5,4,6,7],7,-15)==[8.602325267042627, 5.0, 10.0, 10.04987562112089, 11.704699910719626, 23.853720883753127, 22.47220505424423, 25.238858928247925, 25.553864678361276] 

print(liste_distances([0,3,-1,-3,-4,20,19,21,20],[-20,-18,-21,-16,-19,5,4,6,7],7,-15))