'''
EXERCICE 02 : SYSTÈME DE VALIDATION D'ACCÈS
- Consigne : Créer un programme qui demande un identifiant et un mot de passe. Si l'identifiant est "admin" et le mot de passe "12345", afficher "Accès autorisé", sinon "Échec de connexion".
- Notions : Conditions if / else, opérateurs de comparaison (==), opérateurs logiques (and).
- Temps : 10 min.
'''

identifiant = input("identifiant   : ")
mot_de_passe = input("mot de passe : ")

if identifiant=="admin" and mot_de_passe=="12345":
    print("-===Accès autorisé===-")
else:
    print("X_Échec de connexion_X")