'''
File: 4_tri_selection.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

from src.pokemon import Pokemon
from src.triselection import Tri, Selection, CompositionTriSelection, print_liste_pandas
import time
from tqdm import tqdm

import os
import pickle

def check_pickle(path:str, pokemon_names:list):
    """Check if a file of the pokemon read already exist so that
    we do not have to request the API again."""
    if not os.path.exists(path):
        return False, None

    with open(path, "rb") as f:
        data = pickle.load(f)
        liste_pokemon_names = [pokemon.pokemon for pokemon in data]
        if liste_pokemon_names == pokemon_names:
            return True, data

    return False, None

    
if __name__ == "__main__":

    fichier_stockage_pokemon = "liste_pokemon.pkl"
    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.1 : Lecture de pokémons dans une liste.
    # ------------------------------------------------------------------------------------------------------------------------- #
    pokemon_names = ["charizard", "charmeleon", "charmander", "bulbasaur", "squirtle",
                     "wartortle", "blastoise", "pikachu", "raichu", "pichu", "eevee",
                     "vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon",
                     "ninetales", "lugia", "mewtwo", "mew"]

    print("Lecture des pokémons :")
    print(pokemon_names)
    t_beginning = time.time()
    check, list_pokemon = check_pickle(fichier_stockage_pokemon, pokemon_names)
    if not check:
        print("Fichier non trouvé, requête API en cours...")
        list_pokemon = [Pokemon(name) for name in tqdm(pokemon_names)]
        with open(fichier_stockage_pokemon, 'wb') as f:
            pickle.dump(list_pokemon, f)

        print("Lecture effectuee en ", time.time()-t_beginning, " s.\n")
    else:
        print("Fichier trouvé, pas de requête API nécessaire.")

    # Affichage de la liste sans tri
    print("Liste de base :")
    print_liste_pandas(list_pokemon, liste_attributs=["id", "pokemon", "height", "weight", "color"])
    print("\n\n\n")

    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.7 : Crière de sélection simple sur la taille.
    # ------------------------------------------------------------------------------------------------------------------------- #
    def critere_taille(pokemon) -> bool:
        return pokemon.height > 9
    selection = Selection(critere_taille)
    liste_filtree = selection.run(list_pokemon)
    print("Liste filtree de pokemon de taile > 0.7m :")
    print_liste_pandas(liste_filtree, liste_attributs=["id", "pokemon", "height", "weight", "color"])
    print("\n\n\n")
    # ------------------------------------------------------------------------------------------------------------------------- #
    # /\ Appeler le prof pour valider une fois que ça marche. On vous demandera alors un autre critère de Sélection.
    # ------------------------------------------------------------------------------------------------------------------------- #



    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.8 : Composition Tri/Sélection : À FAIRE SI VOUS ÊTES EN AVANCE.
    # ------------------------------------------------------------------------------------------------------------------------- #
    # def critere_couleur(pokemon):
    #     return pokemon.color == "red" or pokemon.color == "yellow"
    # liste_selection = [Selection(critere_taille), Selection(critere_couleur)]
    # liste_tri = [Tri("weight", "ascendant")]
    # liste_filtree_triee = CompositionTriSelection(liste_tri, liste_selection).run(list_pokemon)
    # print("Liste filtree de pokemon de taile > 0.7m, de couleur jaune ou rouge et triee par poids ascendant :")
    # print_liste_pandas(liste_filtree_triee, liste_attributs=["id", "name", "height", "weight", "color"])
    # print("\n\n\n")
    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # Appeler le prof pour valider.
    # # ------------------------------------------------------------------------------------------------------------------------- #
