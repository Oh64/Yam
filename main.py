# pip install google.generativeai asyncio termcolor

# Libs
import turtle as Tortue
from random import *
import asyncio
from time import *
import sys
from termcolor import colored, cprint # https://pypi.org/project/termcolor/

# Funcs 
from ia_crisc import *
#from ia_gemini import *
from draw_des import *
from main_func import *
from draw_grid import *

tortue.setup()
tortue_reset()
tortue.write("Ne jamais fermer cette fenetre le programme s'en occupera | Loading...", font=("arial", 10, 'normal'))

# Variable du jeu
class GameBoard:
    def __init__(Player, Name, Co1, Co2, Co3, Co4, Co5, Co6, Bonus, Mini, Maxi, Brelan, Full, PS, GS, Carre, Yam, Bot, Total):
        # Attributs pour stocker le score et les combinaisons
        Player.Name = Name # Une idée, bonne mais mouais
        Player.Co1 = Co1  # Score pour les 1
        Player.Co2 = Co2  # Score pour les 2
        Player.Co3 = Co3  # Score pour les 3
        Player.Co4 = Co4  # Score pour les 4
        Player.Co5 = Co5  # Score pour les 5
        Player.Co6 = Co6  # Score pour les 6
        Player.Bonus = Bonus  # Bonus
        Player.Mini = Mini  # Score mini
        Player.Maxi = Maxi  # Score maxi
        Player.Brelan = Brelan  # Brelan fait ou non
        Player.Full = Full  # Full fait ou non
        Player.PS = PS  # Petite suite faite ou non
        Player.GS = GS  # Grande suite faite ou non
        Player.Carre = Carre  # Carré fait ou non
        Player.Yam = Yam  # Yam fait ou non
        Player.IsABot = Bot # bot ou non
        Player.Total = Total # TOTAL COMPLET DES POINTS

players = []
num_players = 0 
while num_players <= 1: # Nombre de joueur supperieur a 1 
    num_players = int(input(colored("Combien de joueurs vont jouer ? (>1): ", "light_magenta", attrs=["bold"])))
#num_players = 2

for i in range(num_players):
    is_bot = ""
    while is_bot not in ["Oui", "Non"]:
        is_bot = input(colored(f"Le joueur {i + 1} est un bot ? Oui/Non \n", "blue"))
        if is_bot not in ["Oui", "Non"]:
            print(colored("Réponse invalide. Veuillez répondre par 'Oui' ou 'Non'.", "red"))
    Name = "Abandoned"
    players.append(GameBoard(Name, 0, 0, 0, 0, 0, 0, False, 0, 0, False, False, False, False, False, False, is_bot == "Oui", 0))
    # On ajoute l'objet dans la liste pour chaque joueurs

aw = "UwU"
while aw not in ["Oui", "Non"]:
    aw = input(colored(f"Par defaut les bot vous laissent 0.3s pour voir leurs dés voulez vous changer ce temps Oui/Non ? \n", "blue"))

if aw == "Oui":
    wait = float(input(colored("Entrez le temps en seconde : ", "light_magenta", attrs=["bold"])))
else: 
    wait = 0.3

Numbers = ["Les 1", "Les 2", "Les 3", "Les 4", "Les 5", "Les 6"]
Txt = ["Brelan", "Full", "Carre", "Yam", "Petite suite", "Grande suite"]
MiniMaxi = ["Mini", "Maxi"]

Player = 1

tours_max = 13
total_tours = tours_max * num_players  # Nombre total de tours
tours_joueur = [0] * num_players  # Initialisation du compteur de tours pour chaque joueur

# Jeu
def main():
    for tour in range(total_tours):
        print("\n")

        player_index = tour % num_players  # Déterminer le joueur actuel
        player = players[player_index] # Récuperer les information du joueur depuis la liste d'objets

        if player.IsABot : print(colored(f">    Au tour de [Bot N{player_index}]", "green", attrs=["bold"]))
        else : print(colored(f">    Au tour de [Joueur N{player_index}]", "green", attrs=["bold"]))

        print_board(player)
    
        des = relance() if not player.IsABot else relanceIA(player, wait)

        mini_sum, maxi_sum = MiniAndMaxi(des)
        Elements, compte = Choice(des, player, player.IsABot, mini_sum, maxi_sum)

        # Voila ce qu'il a a ce stade : Elements (ce que tu peux faire), des, points avec maxi/mini, ton tableau de score

        if len(Elements) > 0:
            if not player.IsABot:
                UserC = "0"

                while UserC not in Elements:
                    UserC = input(colored(f"[Joueur N{player_index}] : Que choisissez-vous ? ", "light_magenta", attrs=["bold"]))
                    if UserC not in Elements:
                        print(colored(f"[Joueur N{player_index}] : Choix incorrect", "red"))

                if UserC in Numbers:
                    # Extraire le nombre à partir de la chaîne "Les X" en prenant la partie après "Les "
                    number = int(UserC.split(" ")[1])  # Récupère le numéro après "Les"
                    setattr(player, f'Co{number}', compte[number] * number)
                    
                elif UserC in Txt:
                    if UserC == "Petite suite":
                        setattr(player, 'PS', True)
                    elif UserC == "Grande suite":
                        setattr(player, 'GS', True)
                    else:
                        setattr(player, UserC, True)

                elif UserC in MiniMaxi:
                    if UserC == "Mini" : setattr(player, UserC, mini_sum)
                    if UserC == "Maxi" : setattr(player, UserC, maxi_sum)

                else:
                    print(colored(f"[Joueur N{player_index}] : Erreur attra : {UserC} n'est pas un choix valide.", "red"))
                    break

            else:

                BI = False
                BotC = "0"

                while BotC not in Elements:
                    BotC = IAChoice(Elements, BI, compte, des)
                    print(f"[Bot N{player_index}] : IA Choix : {BotC}")
                    BI = True

                if BotC in Numbers:
                    number = int(BotC.split(" ")[1])
                    setattr(player, f'Co{number}', compte[number] * number)
                elif BotC in Txt:
                    if BotC == "Petite suite":
                        setattr(player, 'PS', True)
                    elif BotC == "Grande suite":
                        setattr(player, 'GS', True)
                    else:
                        setattr(player, BotC, True)
                elif BotC in MiniMaxi:
                    if BotC == "Mini" : setattr(player, BotC, mini_sum)
                    if BotC == "Maxi" : setattr(player, BotC, maxi_sum)
                else:
                    print(colored(f"[Bot N{player_index}] : Erreur attrb : {BotC} n'est pas un choix valide (Erreur de l'IA).", "red"))
        else:
            if player.IsABot : print(colored(f"[Bot N{player_index}] : Rien à faire :/ \n[Bot N{player_index}] : Un de perdu, zero de retrouvé !", "green", attrs=["bold"]))
            else : print(colored(f"[Joueur N{player_index}] : Rien à faire :/ \n[Joueur N{player_index}] : Un de perdu, zero de retrouvé !", "green", attrs=["bold"]))
            time.sleep(wait*1)

        if player.Co1+player.Co2+player.Co3+player.Co4+player.Co5+player.Co6 > 60: player.Bonus = True
        player.Total = calcul_score_final(player)
        players[player_index] = player

        # Incrémenter le compteur de tours pour le joueur actuel
        tours_joueur[player_index] += 1

    # Fin du jeu
    print(colored("Tous les tours ont été joués.", "magenta", attrs=["bold"]))

    # Calculer le nombre total de pages
    num_pages = (num_players + 2 - 1) // 2  # Division arrondie au supérieur
    page = 0

    while True:
        # Afficher la page actuelle
        print(colored(f"Page {page + 1}/{num_pages}", "blue"))
        debut = page * 2
        fin = min(debut + 2, num_players)

        # Afficher les scores pour chaque joueur de la page actuelle
        tortue_reset()
        tortue.tracer(0)
        colonne1()
        ecriture()
        for i in range(debut, fin):
            players[i].Total = calcul_score_final(players[i])

            if i == debut : name(1, players[i].IsABot, i)
            else : name(2, players[i].IsABot, i)
            tortue.up()
            if i == debut : 
                colonne2()
                tortue.goto(-225,200)
            else : 
                colonne3()
                tortue.goto(-150,200)
            colonne_joueur(players[i])
            tortue.right(4*90)
        tortue.update()
        #tortue.done()
        # Gestion de la navigation
        print(colored("\nOptions:", "red"))
        if page > 0:
            print(colored("1: Page précédente", "red"))
        if page < num_pages - 1:
            print(colored("2: Page suivante", "red"))
        print(colored("3: Quitter", "red"))

        choix = input(colored("Choisissez une option (1, 2, 3) : ", "blue"))

        if choix == '1' and page > 0:
            page -= 1  # Aller à la page précédente
        elif choix == '2' and page < num_pages - 1:
            page += 1  # Aller à la page suivante
        elif choix == '3':
            print("Merci d'avoir joué !")
            tortue.bye()
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Thread error / Don't use asyncio.run(main())
main()
