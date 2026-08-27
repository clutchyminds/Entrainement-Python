# Correction de l'exercice 6
'''
EXERCICE 06 : EXTRACTEUR DE MULTIPLES
- Consigne : À partir d'une liste de nombres allant de 1 à 50, créer une nouvelle liste ne contenant que les multiples de 3.
- Notions : Listes, boucles, méthode .append().
- Temps : 15 min.
'''

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
liste_multiples_3 = []
x = 50

for i in range(0, len(liste)):
    if i%3 == 0:
        liste_multiples_3.append(liste[i])
    else:
        pass #optionel

print(liste_multiples_3)