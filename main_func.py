from random import *
import turtle as tortue
import time
from termcolor import colored, cprint 
from draw_des import *
from ia_crisc import *
#from ia_gemini import *

def calcul_score_final(player):
    score = (player.Co1 + player.Co2 + player.Co3 + player.Co4 +
             player.Co5 + player.Co6 + player.Mini + player.Maxi + 
             player.Co1*(player.Maxi-player.Mini))
    if player.Bonus: score += 30
    if player.Brelan: score += 20
    if player.Full: score += 30
    if player.Carre: score += 40
    if player.Yam: score += 50
    if player.PS: score += 20
    if player.GS: score += 20
    return score

def print_board(self):
        
        if self.IsABot: return

        print(f"Voici votre tableau de bord :\n")
        
        if self.Brelan:
            print("Vous avez déjà fait : Un brelan.")
        if self.Full:
            print("Vous avez déjà fait : Un full.")
        if self.PS:
            print("Vous avez déjà fait : Une petite suite.")
        if self.GS:
            print("Vous avez déjà fait : Une grande suite.")
        if self.Carre:
            print("Vous avez déjà fait : Un carré.")
        if self.Yam:
            print("Vous avez déjà fait : Un yam.")

        print(f"\nScores actuels :")
        print(f"1: {self.Co1}, 2: {self.Co2}, 3: {self.Co3}, 4: {self.Co4}, 5: {self.Co5}, 6: {self.Co6}")
        print(f"Bonus: {self.Bonus}")
        print(f"Mini: {self.Mini}")
        print(f"Maxi: {self.Maxi}")
        
        print(f"Total des points : {self.Total} \n")




def IsA(des):
    '''Regarde s'il y a un Brelan, Full, Carré ou Yam avec les dés.'''
    result = {
        "Brelan": False,
        "Full": False,
        "Carré": False,
        "Yam": False
    }

    # Dictionnaire pour compter combien de fois chaque numéro de dé apparaît
    compte = {}
    for de in des:
        compte[de] = compte.get(de, 0) + 1

    brelan_count = 0
    full_count = 0

    # On regarde combien de fois chaque dé est présent pour voir si on a des combinaisons
    for valeur in compte.values():
        if valeur >= 3:
            result["Brelan"] = True
            brelan_count += 1
        if valeur >= 4:
            result["Carré"] = True
        if valeur >= 5:
            result["Yam"] = True

        # Compte pour le Full
        if valeur >= 2:
            full_count += 1

    # Un Full est valide si on a au moins un brelan et un autre dé qui apparaît au moins 2 fois
    if brelan_count >= 1 and full_count >= 2:
        result["Full"] = True

    return result, compte

def IsAPS(des):
    '''Regarde s'il y a une petite suite (1 à 5) dans les dés.'''
    suite = 1  # On commence par chercher le 1
    restart = 1

    while restart == 1:
        restart = 0
        for de in des:
            if de == suite:
                suite += 1
                restart = 1
                break
    

    return suite == 6  # Si on a trouvé tous les numéros jusqu'à 5

def IsAGS(des):
    '''Regarde s'il y a une grande suite (2 à 6) dans les dés.'''
    suite = 2
    restart = 1

    while restart == 1:
        restart = 0
        for de in des:
            if de == suite:
                suite += 1
                restart = 1

    return suite == 7  # Si on a trouvé tous les numéros jusqu'à 6

def MiniAndMaxi(des):

    all_des = sum(des)
    mini_sum = 0
    maxi_sum = 0
    if all_des < 10 : mini_sum = all_des
    if all_des > 20 : maxi_sum = all_des

    return mini_sum, maxi_sum

def Choice(des, User, IsABot, mini_sum, maxi_sum):

    # Fonctions pour savoir les actions possible avec ce set de des
    DesBE, compte = IsA(des)
    PS = IsAPS(des)
    GS = IsAGS(des)
    total_sum = sum(des)

    if not IsABot:
        print(colored("D'après tes dés, tu pourrais choisir :", "green", attrs=["bold"]))

    Elements = []

    # Tout ça va simplement Afficher ce que tu peux faire en enlevant ce que tu as deja fait

    for num in range(1, 7):
        IsDone = getattr(User, f"Co{num}", None)
        if num in compte and compte[num] > 1 and IsDone == 0:  # Vérifie si le dé est présent et a été lancé plusieurs fois
            Elements.append("Les " + str(num))
            if not IsABot:
                print(f"- Les {num} ({compte[num] * num} points)")

    if DesBE["Brelan"] and not User.Brelan:
        Elements.append("Brelan")
        if not IsABot:
            print("- Brelan (20 points)")
    if DesBE["Full"] and not User.Full:
        Elements.append("Full")
        if not IsABot:
            print("- Full (30 points)")
    if DesBE["Carré"] and not User.Carre:
        Elements.append("Carre")
        if not IsABot:
            print("- Carre (40 points)")
    if DesBE["Yam"] and not User.Yam:
        Elements.append("Yam")
        if not IsABot:
            print("- Yam (50 points)")
    if PS and not User.PS:
        Elements.append("Petite suite")
        if not IsABot:
            print("- Petite suite (20 points)")
    if GS and not User.GS:
        Elements.append("Grande suite")
        if not IsABot:
            print("- Grande suite (30 points)")
    if mini_sum > 0 and not User.Mini:
        Elements.append("Mini")
        if not IsABot:
            print(f"- Mini ({mini_sum} points)")
    if maxi_sum > 4 and not User.Maxi:
        Elements.append("Maxi")
        if not IsABot:
            print(f"- Maxi ({maxi_sum} points)")

    return Elements, compte

def relance():
    # Génère les 5 dés initiaux avec des valeurs aléatoires entre 1 et 6
    des = [randint(1, 6) for i in range(5)] 
    relance = 2 

    # Boucle principale pour gérer les relances
    while relance > 0:  # Boucle tant qu'il reste des relances disponibles
        
        drawdes(des)

        # Affiche les dés actuels et demande à l'utilisateur quels dés il souhaite relancer
        dac = input(colored(f"Ecrivez 0 ou 'exit' pour conserver les dés actuels et terminer \n"
                    f"Quels dés voulez-vous relancer (ex: '543' pour dés 5, 4 et 3) ? ({relance} relances restantes) \n ", "light_magenta", attrs=["bold"]))

        # Si l'utilisateur est d'accord avec les dés actuels, on termine la boucle
        if dac == "0" or dac.lower() == "exit":  # .lower() transforme toutes les lettres en minuscules au cas ou
            break  # Sort de la boucle

        # Liste des indices des dés à relancer
        rdes = []

        # Remplit rdes avec les dés à relancer en vérifiant que chaque caractère est un chiffre
        for char in dac:  # Boucle sur chaque caractère entré par l'utilisateur
            if char.isdigit():  # Si le caractère est un chiffre
                if 1 <= int(char) <= 5:
                    rdes.append(int(char) - 1)
                else:
                    print(colored(f"Nombre incorrect : {int(char)}", "red"))

        # Relance les dés sélectionnés
        for i in rdes:  # Parcourt chaque index des dés à relancer
            des[i] = randint(1, 6)  # Génère une nouvelle valeur pour le dé à cet index

        relance -= 1  # Diminue le nombre de relances restantes

    # Affiche les dés finaux après les relances
    drawdes(des)

    return des

def relanceIA(UserBot, wait):
    # Génère les 5 dés initiaux avec des valeurs aléatoires entre 1 et 6
    des = [randint(1, 6) for i in range(5)]  # Génération plus lisible avec une compréhension de liste
    relance = 2
    for i in range(relance):
        drawdes(des)
        time.sleep(wait)
        print(colored("En attente de l'IA...", "blue"))
        DesRelance = RelanceIAFile(des, relance, UserBot)
        print(colored(f"IA Relance : {DesRelance}", "blue"))
        if DesRelance == [0] : break
        for i in DesRelance:  # Parcourt chaque index des dés à relancer
            des[i-1] = randint(1, 6)  # Génère une nouvelle valeur pour le dé à cet index
    return des
