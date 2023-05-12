from random import randint


def triInsertion(liste):
    """
    cette fonction trie une liste de nombre par insertion
    parametres :
    - liste : une liste de nombre à trier
    return :
    - liste : la liste triée
    """
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i-1
        while j >=0 and cle < liste[j] :
                liste[j+1] = liste[j]
                j -= 1
        liste[j+1] = cle
    return liste

list = [3,18,4,19,25,7]
assert(triInsertion(list)==[3, 4, 7, 18, 19, 25])

print("*****************")
print("*****************")

list = [randint(0,100) for x in range(0,100)]
print(list)
print("*****************")
print(triInsertion(list))