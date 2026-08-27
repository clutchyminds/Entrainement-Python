# Correction de l'exercice 8
'''
EXERCICE 08 : ANNUAIRE DE CONTACTS
- Consigne : Créer un dictionnaire où les clés sont des noms et les valeurs des numéros de téléphone. Permettre à l'utilisateur de saisir un nom pour récupérer le numéro. Si le nom n'existe pas, afficher un message d'erreur.
- Notions : Dictionnaires, méthode .get() ou vérification in.
- Temps : 15 min.
'''

dico_nom = {"robot": "06060606", "test": "438432168", "chien": "964846321", "spike": "4341321", "shelly": "123456789", }

print("Noms disponibles:\n==robot==\n==test==\n==chien==\n==spike==\n==shelly==")


nom = str( input("entrez un nom pour obtenir un numéro de téléphhon : "))


if nom in dico_nom:
    print(f"le numéro de {nom} est {dico_nom.get(nom)}")
else:
    print(f"désoler {nom} n'a pas de numéro ici :/")