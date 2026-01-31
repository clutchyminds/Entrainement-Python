# Correction de l'exercice 12
'''
EXERCICE 12 : CALCULATRICE MODULAIRE
- Consigne : Créer quatre fonctions (addition, soustraction, multiplication, division). Créer une cinquième fonction qui prend deux nombres et un opérateur en argument et appelle la bonne fonction.
- Notions : Appel de fonctions, passage d'arguments.
- Temps : 20 min.
'''

def addition(nbr1, nbr2):
    print(nbr1+nbr2)

def soustraction(nbr1, nbr2):
    print(nbr1-nbr2)
    
def multiplication(nbr1, nbr2):
    print(nbr1*nbr2)
   
def division(nbr1, nbr2):
    print(nbr1/nbr2)
   
def calcul(nbr1, nbr2, opérateur):
    if opérateur=="+" :
        return addition(nbr1, nbr2)
    elif opérateur==- :
        addition(nbr1, nbr2)
