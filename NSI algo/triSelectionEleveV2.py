from random import randint

'''
On recherche le plus petit élément et on positionne à sa place en l'échangeant avec le premier
On recherche le second plus petit élément et on le positionne à sa place en l'échangeant avec le second

i=0 # position du plus petit élement
tant que i < longueur de la liste = N
    On cherche le plus petit des éléments entre i et N
    Il se situe à la valeur j
    On le place en list[j] dans temp
    On place list[i] dans list[j]
    On place temp dans list[i]
    i=i+1
'''


def triSelection(liste):
    """
    cette fonction trie une liste de nombre par selection
    parametres :
    - liste : une liste de nombre à trier
    return :
    - liste : la liste triée
    """
    for i in range(len(liste)):
        cle = i
        for j in range(i+1, len(liste)):
            if liste[cle] > liste[j]:
                cle = j 
        liste[i], liste[cle] = liste[cle], liste[i]
    return liste

list = [3,18,4,19,25,7]
assert(triSelection(list)==[3, 4, 7, 18, 19, 25])

print("*****************")
print("*****************")

list = [randint(0,100) for x in range(0,100)]
print(list)
print("*****************")
print(triSelection(list))

