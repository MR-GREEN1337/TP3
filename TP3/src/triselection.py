'''
File: triselection.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
Ce fichier contient les classes et fonctions relatives au tri 
et à la sélection
'''

import pandas as pd
from pokemon import Pokemon

def print_liste(liste_pokemons):
    """Fonction qui affiche les noms des pokemons dans une liste de pokémons

    Parameters
    ----------
    liste_pokemons : list
        liste de pokémons
    """
    string = ""
    for pokemon in liste_pokemons:
        string += pokemon.name + " "
    print("-------------------------------------------------------------------------")
    print(string)


def print_liste_pandas(liste_pokemons, liste_attributs=["id", "name", "height", "weight"]):
    """Fonction qui affiche les informations sou forme de table d'une liste de pokémons

    Parameters
    ----------
    liste_pokemons : list
        liste de pokémons
    liste_attributs : list, optional
        liste d'attributs à afficher, by default ["id", "name", "height", "weight"]
    """    # Iterating through all the attributes and pokemons
    data = []
    for pokemon in liste_pokemons:
        data_pokemon = []
        for attribute in liste_attributs:
            pokemon.verify_attribute(attribute)
            data_pokemon.append( getattr(pokemon, attribute) )
        data.append(data_pokemon)

    # Constructing pandas dataframe to print the database
    data = pd.DataFrame(data)
    data.columns = liste_attributs
    print(data.to_string(index=False))


# ------------------------------------------------------------------------ #
# 3.2 : Réaliser le tri à bulle d'une liste
# ------------------------------------------------------------------------ #
def tri_bulle(tab) -> list:
    """Fonction qui implémente un tri à bulles

    Parameters
    ----------
    tab : list
        liste à trier

    Returns
    -------
    list
        liste triée
    """
    for i in [*range(1, len(tab))].reverse():
        for j in range(i):
            if tab[j+1] < tab[j]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

# ------------------------------------------------------------------------ #
# 3.3 : Réaliser la classe Tri
# ------------------------------------------------------------------------ #
class Tri():
    super(Pokemon).__init__()

    def __init__(self):
        self.attribut = None
        self.type = None
        self.tri = None

    def set_attribute(self, attribut):
        self.attribut = attribut

    def set_type(self, type: str):
        self.type = type
    # ------------------------------------------------------------------------ #
    # 3.4 : Réaliser la méthode run
    # ------------------------------------------------------------------------ #
    def run(self, list_pokemon) -> list:
        tri_bulle([pokemon.set_comparaison_attribute(self.attribut) for pokemon in list_pokemon])

# ------------------------------------------------------------------------ #
# 3.5 : Réaliser la classe CompositionTri avec la méthode run
# ------------------------------------------------------------------------ #
class CompositionTri():
    """Classe permettant de faire une composition de plusieurs Tris.
    """
    pass

# ------------------------------------------------------------------------ #
# 3.6 : Réaliser la classe Selection
# ------------------------------------------------------------------------ #
class Selection():
    """Classe implémentant un critère de sélection sur une liste de pokémons.
    """
    pass

    # ------------------------------------------------------------------------ #
    # 3.7 : Réaliser la méthode run
    # ------------------------------------------------------------------------ #
    def run(self, list_pokemon) -> list:
        pass

# ------------------------------------------------------------------------ #
# 3.5 : Réaliser la classe CompositionTriSelection avec la méthode run
# ------------------------------------------------------------------------ #
class CompositionTriSelection():
    """Classe faisant la composition entre des critères de tri et de sélection.
    """
    pass