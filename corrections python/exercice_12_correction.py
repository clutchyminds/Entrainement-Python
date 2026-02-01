# Correction de l'exercice 12
'''
EXERCICE 12 : CALCULATRICE MODULAIRE
- Consigne : Créer quatre fonctions (addition, soustraction, multiplication, division). Créer une cinquième fonction qui prend deux nombres et un opérateur en argument et appelle la bonne fonction.
- Notions : Appel de fonctions, passage d'arguments.
- Temps : 20 min.
'''

def addition(nbr1, nbr2):
    return nbr1+nbr2

def soustraction(nbr1, nbr2):
    return nbr1-nbr2
    
def multiplication(nbr1, nbr2):
    return nbr1*nbr2
   
def division(nbr1, nbr2):
    return nbr1/nbr2
   
def calcul(nbr1, nbr2, opérateur):
    if opérateur=="+" :
        return addition(nbr1, nbr2)
    elif opérateur=="-" :
        return addition(nbr1, nbr2)
    elif opérateur=="*" :
        return multiplication(nbr1, nbr2)
    elif opérateur=="/" :
        return division(nbr1, nbr2)
    else:
        print(f"Désoler je ne reconnais pas l'opérateur {opérateur}")

print("je vais vous demmander deux nombres puis un opérateur pour pouvoir réaliser un calcul :")
print("")

nombre_1 = int( input("donnez moi le premier nombre : "))
nombre_2 = int( input("donnez moi le deuxiemme nombre : "))
opé = input("donnez moi l'opérateur : ")

print(calcul(nombre_1, nombre_2, opé))