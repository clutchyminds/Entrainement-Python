# Correction de l'exercice 6
'''
EXERCICE 06 : EXTRACTEUR DE MULTIPLES
- Consigne : À partir d'une liste de nombres allant de 1 à 50, créer une nouvelle liste ne contenant que les multiples de 3.
- Notions : Listes, boucles, méthode .append().
- Temps : 15 min.
'''

liste = list(range(1, 50))
liste_multiples_3 = []

for i in range(1, len(liste)):
    if liste[i]/3==0 :
        liste_multiples_3.append(liste[i])


print(liste_multiples_3)