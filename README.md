# Tictactoe Easi

## Prérequis

- Python 3.10 ou supérieur  
- `pytest` pour lancer les tests (optionnel) :

bash :
"pip install pytest"

## Lancer le jeu

- Lancer le jeu :
    "python -m tictactoe.main"


## Utilisation

- Une fois le jeu lancé suivrent les étapes :
    1. Choisir son symbole (X ou O)
    2. Si X, vous jouez en premeir sinon l'IA jouera en premier
    3. Choisir où placer votre pion (row, col). par exemple en 0,0

- Pour changer la taille de la grille :
    Changer le parametre de TicTacToeCLI dans main.py


## Lancer les tests

- Execution des tests à la racine du projet :
    "python -m pytest -v"