# Correction de l'exercice 4
'''
EXERCICE 04 : GÉNÉRATEUR DE SIGLES
- Consigne : Demander trois mots à l'utilisateur (ex: Réseau, National, SNCF). Extraire la première lettre de chaque mot pour créer et afficher un sigle en majuscules.
- Notions : Indexation de chaînes [0], méthode .upper(), concaténation.
- Temps : 10 min.
'''
print("je vais vous demmander 3 mots : ")
mot1 = str( input("premier mot   :"))
mot2 = str( input("deuxieme mot  :"))
mot3 = str( input("troisieme mot :"))

mot1 = mot1[0]
mot2 = mot2[0]
mot3 = mot3[0]

print(f"voici vos mots siglés : {mot1.upper()}.{mot2.upper()}.{mot3.upper()}")