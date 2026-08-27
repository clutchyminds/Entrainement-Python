# Correction de l'exercice 3
'''
EXERCICE 03 : ANALYSEUR DE PARITÉ ET DE GRANDEUR
- Consigne : Demander un nombre entier. Afficher s'il est pair ou impair, ET s'il est positif, négatif ou nul.
- Notions : Modulo %, conditions imbriquées elif.
- Temps : 10 min.
'''

nombre = int( input("donnez moi un nombre entier : "))

if nombre%2==0 :
    if nombre>0 :
        print("ce nombre est paire et positif")
    else:
        print("ce nombre est paire et négatif")
else:
    if nombre>0 :
        print("ce nombre est impaire et positif")
    else:
        print("ce nombre est impaire et négatif")
    
