# Yam
from random import *


des = [randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
relance = 3
desachanger = str(input(f"Voici tes 5 dés : \n - Dés 1 : {des[0]} \n - Dés 2 : {des[1]} \n - Dés 3 : {des[2]} \n - Dés 4 : {des[3]} \n - Dés 5 : {des[4]}  \n Voulez vous en relancer ({relance} restant) ? \n"))
rdes = []
for i in range(len(desachanger)): # Taille de "543"
    rdes.append(desachanger[i-1:i]) # Ajoute un element dans la liste 

for i in range(len(rdes)):
    des[(rdes[i-1]-1)] = randint(1,6)
desachanger = str(input(f"Voici tes 5 dés : \n - Dés 1 : {des[0]} \n - Dés 2 : {des[1]} \n - Dés 3 : {des[2]} \n - Dés 4 : {des[3]} \n - Dés 5 : {des[4]}  \n Voulez vous en relancer ({relance} restant) ? \n"))

