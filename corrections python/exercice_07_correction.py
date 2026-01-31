# Correction de l'exercice 7
'''
EXERCICE 07 : RECHERCHE DE MAXIMUM MANUEL
- Consigne : Créer une liste de 10 nombres. Trouver le nombre le plus grand de la liste en utilisant une boucle, sans utiliser la fonction max().
- Notions : Itération, comparaison itérative.
- Temps : 15 min.
'''


liste = [12, 45, 1, 1000, 6, 159, 95, 1, 897, 2,23 ]
x = 0

for i in range(0, len(liste)):
    if liste[i]>x:
        x = liste[i]

print(x)
