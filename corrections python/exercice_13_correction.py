# Correction de l'exercice 13
'''
EXERCICE 13 : FORMATEUR DE TEXTE PROFESSIONNEL
- Consigne : Créer une fonction qui prend une liste de noms et retourne une seule chaîne de caractères où les noms sont séparés par des virgules, sauf le dernier qui doit être précédé de "et".
- Notions : Manipulation de listes, jointure, conditions de fin.
- Temps : 25 min.
'''

def prendre_liste(une_liste):
    return ", ".join(une_liste)

liste = ["spike", "shelly", "corbac", "leon", "ricochet", "rosa", "sans", "Technoblade", "steeve", ]

print(prendre_liste(liste))