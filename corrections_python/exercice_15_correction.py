# Correction de l'exercice 15
'''
EXERCICE 15 : VÉRIFICATEUR DE PALINDROMES
- Consigne : Écrire une fonction qui vérifie si un mot est un palindrome (se lit de la même façon dans les deux sens) en ignorant la casse.
- Notions : Slicing de chaînes [::-1], méthodes .lower().
- Temps : 15 min.
'''

def vérification(mot):
    mot.lower()
    if mot == mot[::-1]:
        return "est effectivement palindrome"
    else:
        return "n'est pas palindrome"

print("|================================================|")
print("|  je vais vérifier si votre mot est palindrome  |")
print("|================================================|")
print("")
mot = str( input("entrez votre mot : "))

print(f"votre mot '{mot}' {vérification(mot)}")   