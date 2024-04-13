"""  Ce fichier contient les fonctions pour le jeu Quixo """
def formater_légende(joueurs):
    return f"Légende: X={joueurs[0]}, O={joueurs[1]}"

def formater_plateau(plateau):
    rows = []
    for i, row in enumerate(plateau):
        rows.append("".join([" " + cell + " " + ("|" if j < 4 else "") for j, cell in enumerate(row)]))
        if i < 4:
            rows.append("--|---|---|---|---|")
    return "\n".join(rows) + "\n  | 1   2   3   4   5"

def formater_jeu(joueurs, plateau):
    return formater_légende(joueurs) + "\n" + formater_plateau(plateau)

def formater_les_parties(parties):
    formatted_parties = []
    for partie in parties:
        id_partie = partie["id"]
        date = partie["date"]
        joueurs = " vs ".join(partie["joueurs"])
        gagnant = f", gagnant: {partie['gagnant']}" if partie['gagnant'] else ""
        formatted_parties.append(f"{id_partie} : {date}, {joueurs}{gagnant}")
    return "\n".join(formatted_parties)

def récupérer_le_coup():
    origine_str = input("Donnez la position d'origine du bloc (x,y) : ")
    direction = input("Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') : ")
    origine = [int(x) for x in origine_str.split(",")]
    return origine, direction

def analyser_commande():
    import argparse

    parser = argparse.ArgumentParser(description='Quixo')
    parser.add_argument('idul', help='IDUL du joueur')
    parser.add_argument('-p', '--parties', action='store_true', help='Lister les parties existantes')

    return parser.parse_args()

from plateau import Plateau
from quixo_error import QuixoError

class Quixo:
    def __init__(self):
        """
        Initialise une nouvelle partie de Quixo.
        """
        self.joueurs = ['X', 'O']
        self.plateau = Plateau()

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de la partie.
        """
        return f"Légende: X={self.joueurs[0]}, O={self.joueurs[1]}\n{self.plateau}"

    def déplacer_pion(self, joueur, origine, direction):
        """
        Déplace un pion sur le plateau.

        Args:
            joueur (str): Le joueur qui déplace le pion.
            origine (tuple): La position d'origine du pion sur le plateau.
            direction (str): La direction du déplacement.

        Raises:
            QuixoError: Si le joueur est invalide ou si le déplacement est impossible.
        """
        if joueur not in self.joueurs:
            raise QuixoError("Joueur invalide.")
        self.plateau.insertion(joueur, origine, direction)

    def récupérer_le_coup(self):
        """
        Récupère le coup à jouer par le joueur.

        Returns:
            tuple: La position d'origine du pion et la direction du déplacement.
        """
        position = input("Entrez la position du pion à déplacer (format: x,y) : ")
        direction = input("Entrez la direction du déplacement (haut, bas, gauche, droite) : ")
        return position, direction

