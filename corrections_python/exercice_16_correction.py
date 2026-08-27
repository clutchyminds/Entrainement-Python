# Correction de l'exercice 16
'''
EXERCICE 16 : CRÉATION DE LOGS
- Consigne : Créer un script qui demande à l'utilisateur de saisir du texte et l'enregistre dans un fichier notes.txt sans écraser le contenu précédent.
- Notions : with open(), mode append ('a').
- Temps : 15 min.
'''

print("je vais vous demmander du text que j'enregistrerais dans un fichier en .txt")
texte = input("entrez votre texte : ")

with open('fichier.txt', 'a') as fichier:
    fichier.write(texte)

