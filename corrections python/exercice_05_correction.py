# Correction de l'exercice 5
'''
EXERCICE 05 : BOUCLE DE SOMME CUMULATIVE
- Consigne : Demander un nombre n. Calculer la somme de tous les entiers de 1 jusqu'à n (ex: pour 3, faire 1+2+3 = 6).
- Notions : Boucle for, fonction range(), accumulateur.
- Temps : 10 min.
'''

nombre = int( input("donnez moi un nombre : "))

for i in range(0, nombre):
    nombre += i

print(f"la somme de tous les entiers de 1 jusqu'à votre nombre est {nombre}")