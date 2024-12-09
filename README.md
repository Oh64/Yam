# Projet Yam en Python

Ce projet de NSI est un jeu du Yam (ou Yahtzee) créé en Python.  
La partie graphique n'a pas été réalisée par moi, mais j'ai pris en charge la logique du jeu.  
Ce jeu se joue dans le terminal avec Turtle.

Quelques différences sont à noter par rapport au jeu original, mais bon, OSEF.

## Prérequis

Avant de pouvoir exécuter le jeu, assurez-vous d'avoir Python installé sur votre machine. Ce projet utilise également quelques dépendances qui doivent être installées via `pip`.

### Installation des dépendances

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Oh64/Yam.git
   cd Yam

2. Installez les dépendances nécessaires :

   ```bash
   pip install google.generativeai asyncio termcolor

3. Exécution du projet

Une fois les dépendances installées, vous pouvez exécuter le jeu en lançant le fichier `main.py` :

    python main.py

Le jeu démarrera directement dans votre terminal, et vous pourrez suivre les instructions pour jouer au Yam.

## Bonus

L'IA Crisc ne vous suffit pas ? Je comprends, vous pouvez utiliser Gemini pour jouer plus intelligemment !
Pour ce faire, vous aurez juste besoin de trois étapes :

1. Modifier `main.py`

Trouvez ces lignes :

    # Funcs 
    from ia_crisc import *
    #from ia_gemini import *

Modifiez les pour :

    # Funcs 
    #from ia_crisc import *
    from ia_gemini import *

2. Modifier `main_func.py`

Trouvez ces lignes :

    from ia_crisc import *
    #from ia_gemini import *

Modifiez les pour :

    #from ia_crisc import *
    from ia_gemini import *

3. Integrez votre clé API :

Dans `ia_gemini.py` vous trouverez cette ligne :

    genai.configure(api_key="")

Elle est très cool cette ligne ! Mais il manque un truc...
Vous devez avoir 18 ans (âge écrit dans votre compte Google) pour faire ça car... Google ? Mmm, ouais.

Si vous n'avez pas de projet Google Cloud, il faut en créer un. Suivez ceci : [Créer un projet Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=fr)

Allez sur [AIStudio Google API Key](https://aistudio.google.com/apikey)

Cliquez sur le GROS bouton "Créer une clé API"
Copiez la clé qu'il vous donne, par exemple : `AIzaSyCdNnxPFpyWBd2gy4Ah6_9nP1pPrPx0aZ5`

Et pour finir remplisez :

    genai.configure(api_key="[Votre clé API]")

Et voilà ! Executez `main.py` et hop !


## Auteurs :
Oh64 : Développement de la logique du jeu.
mthss23 et heqdshqker : Affichage graphique du jeu
