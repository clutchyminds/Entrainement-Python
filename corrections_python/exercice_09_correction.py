# Correction de l'exercice 9
'''
EXERCICE 09 : COMPTEUR DE FRÉQUENCE DE CARACTÈRES
- Consigne : Demander une phrase. Créer un dictionnaire qui compte combien de fois chaque lettre apparaît dans la phrase.
- Notions : Itération sur chaîne, mise à jour de dictionnaire.
- Temps : 20 min.
'''

phrase = str( input("donnez moi une phrase : "))

nombre_lettre = {}

for i in phrase:
    if i in nombre_lettre:
        nombre_lettre[i] += 1
    else:
        nombre_lettre[i] = 1


print(f"vous avez ce nombre de lettre dans votre phrase : {nombre_lettre}")