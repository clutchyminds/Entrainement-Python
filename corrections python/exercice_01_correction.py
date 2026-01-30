'''
EXERCICE 01 : CALCULATEUR D'ÉCHÉANCE
- Consigne : Demander l'âge de l'utilisateur. Calculer et afficher l'année précise à laquelle il fêtera ses 100 ans.
- Notions : input(), conversion de types (int), opérations arithmétiques, f-strings.
- Données : Utiliser l'année actuelle comme variable.
- Temps : 5 min.
'''

age = int( input("donnez votre age : ")) #demmande l'age
calcule = 100 - age #calcule dans combien de temp il aura 100 ans

if calcule<0 : #vérifie si l'age est négatif ou pas
    print(f"vous avez déja {100-calcule} ans !")
else:
    print(f"vous avez {calcule} ans avant d'avoir 100 ans !")