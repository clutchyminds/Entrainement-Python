# Correction de l'exercice 17
'''
EXERCICE 17 : CALCULATEUR DE MOYENNE SUR FICHIER
- Consigne : Lire un fichier contenant une liste de nombres (un par ligne) et calculer leur moyenne.
- Notions : Lecture de fichiers, conversion de données lues.
- Temps : 20 min.
'''

import csv


path = "corrections_python/ressources/exos_17.csv"

def moyenne(x):
    with open(x, "r") as mon_fichier:
        lecteur = csv.reader(mon_fichier, delimiter=';')
        """
        ouvre exos_17.py et le stoque dans lecteur sous forme de lignes

        """
        lignes = list(lecteur)
        x = 0
        nbr = 0
        for ligne in lignes:
            nbr = len(lignes) - (len(lignes) - x)
            x += 1
            result = lignes[i][nbr] 
            print(result)

        

moyenne(path)