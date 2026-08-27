# Correction de l'exercice 14
'''
EXERCICE 14 : GÉNÉRATEUR DE MOTS DE PASSE
- Consigne : Créer une fonction qui génère un mot de passe de longueur n (passée en argument) contenant des lettres et des chiffres aléatoires.
- Notions : Module random, module string.
- Temps : 20 min.
'''

from random import choice
import string


mdp_liste = []

def mdp(n):
    caractere = string.ascii_letters + string.digits + string.punctuation
    for i in range(0, n):
        a = choice(caractere)
        mdp_liste.append(a)
    return "".join(mdp_liste)


long_mdp = int( input("entrez la longueure que vous voulez pour vottre mot de passe : "))
print(f"votre mot de passe de longueure {long_mdp} est : {mdp(long_mdp)}")
