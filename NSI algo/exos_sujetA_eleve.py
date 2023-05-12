# exercices_sujet A Fevrier 2021

######### EXO 1 #########

#Fonction permettant de pouvoir multiplier deux chiffres sans avoir a utiliser la fonction integrer dans python
#Définition de notre fonction avec les conditions n1 et n2 qui correspondent aux chiffres a multiplier
def multiplication(n1, n2):
    #Définition de "resultat" afin de pouvoir le modifier au cours de notre fonction
    resultat = 0
    #Début d'une boucle for qui répetera l'action autant de fois qu'elle est égale a n1, tout en rendant le chiffre absolu pour pouvoir lui donner son signe après
    for i in range(abs(n1)):
        #Addition de des chiffres au résultat sans supprimer la valeur précedente, pareil ici, nous rendons le chiffres absolu afin de lui rendre son signe plus tard
        resultat += abs(n2)
    #Vérification de si le calcul nous donnera un chiffre négatif, si oui modifier le résultat afin de lui ajouter un symbole "-" devant
    if ((n1 < 0) and (n2 > 0)) or ((n2 < 0) and (n1 > 0)):
        return -resultat
    #Si le chiffre n'est pas négatif nous retournons directement le chiffre tel qu'il est déjà
    return resultat
    
print(multiplication(-5,5))

######### EXO 2 #########

liste_eleves = ['a','b','c','d','e','f','g','h','i','j'] 
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    # Création d'une variable qui a comptera le nombre d'élève
    nb_eleves_note_maxi = 0
    # Création d'un tableau vide qui stockera le nom des élèves ayant la note maximale
    liste_maxi = []
    # Création d'une boucle for qui se répète autant de fois qu'il y a de notes
    for compteur in range(len(liste_notes)):
        # Si la note correspond a la note maximale nous ajoutons 1 a nb_eleves_note_maxi
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            #Ensuite nous ajoutons le nom de l'élève a la liste liste_maxi
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            # Nous redéfinissons le "compteur" d'élèves a 1
            nb_eleves_note_maxi = 1
            # Et nous redéfinissons la liste liste_maxi avec uniquement l'élève ayant eu la plus haute note
            liste_maxi = [liste_eleves[compteur]]
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)

print(meilleures_notes())

liste_eleves = ['er','gt','fv','gh','sx','ui','ji','hi','nj','op'] 
liste_notes = [14, 34, 9, 25, 87, 43, 43, 29, 16, 24]
assert meilleures_notes() ==(87, 1, ['sx'])