mini = 0
maxi = int(input("chiffre maximal"))
counter = 0
rep = " "
while rep != "=":
    x = (maxi + mini)//2
    print(x)
    rep = input("=/+/-")
    if rep == "+":
        mini=x+1
    elif rep == "-":
        maxi=x-1
    counter += 1
print(counter)