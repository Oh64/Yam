from random import *
import google.generativeai as genai
import os

# Configurer la bibliothèque avec la clé API
genai.configure(api_key="")


def RelanceIAFile(des, relance, UserBot):
    # Préparer le prompt
    prompt = f"""
    Bonjour, tu es un expert du YAM.
    Ne fait que la réponse demandée, aucune explication n'est demandée.
    Ton objectif est de viser ce qui pourrait te donner le plus de points pour gagner la partie.
    Voici la liste des dés que tu as à disposition : {des}
    Voici ce que tu as déjà coché sur ta feuille de score : 
    1: {UserBot.Co1}, 2: {UserBot.Co2}, 3: {UserBot.Co3}, 4: {UserBot.Co4}, 5: {UserBot.Co5}, 6: {UserBot.Co6}, 
    Mini: {UserBot.Mini}, Maxi: {UserBot.Maxi}, Brelan: {UserBot.Brelan}, Full: {UserBot.Full}, 
    Petite Suite: {UserBot.PS}, Grande Suite: {UserBot.GS}, Carré: {UserBot.Carre}, Yam: {UserBot.Yam}
    Relances restantes après celle-ci : {relance}
    Rends uniquement les indices des dés à relancer (par exemple : "1,3,5").
    """

    try:
        # Appel de l'API pour générer du contenu
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Traiter la réponse pour extraire les indices des dés
        choix = response.text.strip()  # Supprimer les espaces inutiles
        DesARelancer = list(map(int, choix.split(',')))  # Convertir en liste d'entiers
        return DesARelancer
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API : {e}")
        return []  # Retourne une liste vide en cas d'erreur

# Fonction de choix pour l'IA
def IAChoice(Elements, BI, compte, des):
    return Elements[0]
