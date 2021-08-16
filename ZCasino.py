import os
from math import ceil
from random import randint

argent = 1000
continuer_partie = True

print("Bienvenue sur ZCasino ! Es-tu prêt à encaisser un max ?!")

while continuer_partie:
    nombre_mise = -1 # On le met exprès à -1 afin que la boucle se repète tant que l'utilisateur n'a pas choisi de numéro correct
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Choisis un nombre entre 0 et 49 ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Veuillez saisir un entier !")
            nombre_mise = -1
            continue
        
        if nombre_mise < 0:
            print("Le nombre saisi est négatif")
        if nombre_mise > 49:
            print("Le nombre saisi est supérieur à 49")
        
    mise = 0 # On le met exprès à 0 afin que la boucle se repète tant que l'utilisateur n'a pas choisi de mise correct
    while mise <= 0 or mise > argent:
        mise = input("Combien voulez vous misez ? ")
        try:
            mise = int(mise)
        except ValueError:
            print("Veuillez saisir un entier !")
            mise = 0
            continue
        
        if mise <= 0:
            print("La mise saisie est négative ou nulle. ")
        if mise > argent:
            print("Vous ne pouvez pas miser autant, vous n'avez que", argent, "$. ")
    
    numero_gagnant = randint(0, 49)
    print("La roulette tourne... Et le numéro est...", numero_gagnant, "! ")
    
    if numero_gagnant == nombre_mise:
        print("Wouuaaww la veine ! les numéros correspondent ! Vous obtenez", mise * 3, "$ !")
        argent += mise
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise = ceil(mise * 0.5)
        print("Les couleurs correspondent ! Vous remportez 50% de votre mise soit", mise, "$ !")
        argent += mise
    else:
        print("Pas de bol ! Vous venez de perdre vos", mise, "$.. ")
        argent -= mise
   
    if argent == 0:
        print("Vous êtes ruiné ! Vous ne pouvez plus jouer.. ")
        continuer_partie = False
    else:
        print("Vous avez à présent", argent, "$. ")
        recommencer = input("Voulez-vous continuer ? (o/n)")
        if recommencer == "o" or recommencer == "O":
            continuer_partie = True
        else:
            continuer_partie = False
            
os.system("pause")
        
            