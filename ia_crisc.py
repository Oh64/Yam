from random import *

# Fonction de la relance pour l'IA
def RelanceIAFile(des, relance, UserBot):  # Le Robot doit-il relancer et si oui quels des ?
    DesARelancer = [1,2,3,4,5] # Ici par exemple il relance juste tout...
    # Vous pouvez rendre l'ia plus sigma smart en utilisant 'des' pour choisir quoi relancer en fonction des des 
    # utilisez UserBot.machin pour savoir ce que l'ia a deja fait c'est le tableau
    return DesARelancer # Il revoie la liste de ce qu'il veux relancer

# Fonction de choix pour l'IA
def IAChoice(Elements, BI, compte, des):
    return Elements[0]
