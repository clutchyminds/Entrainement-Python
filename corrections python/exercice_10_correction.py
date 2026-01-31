# Correction de l'exercice 10
'''
EXERCICE 10 : NETTOYAGE DE DOUBLONS
- Consigne : Soit une liste contenant des doublons. Créer une version "propre" de la liste sans aucune répétition, tout en conservant l'ordre initial des éléments.
- Notions : Listes, opérateurs d'appartenance not in.
- Temps : 20 min.
'''

liste = ["test", "yo", "bjr", "test", "bjr", "yo"]

liste_propre = []

for i in range(0, len(liste)):
    if liste[i] in liste_propre :
        pass
    else:
        liste_propre.append(liste[i])

print(f"voici la liste sans doublons : {liste_propre}")