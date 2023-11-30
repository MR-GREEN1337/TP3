'''
File: 5_pokemon_aleatoire.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 23 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

import requests
import random
from src.pokemon import Pokemon

if __name__ == "__main__":

        # ----------------------------------------------- #  
        # 4.1 : Liste de tous les pokémons
        # ----------------------------------------------- #   
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000')  # L'API limite souvent à 1000 pour éviter des réponses trop grandes
        data = response.json()

        # Extraire les noms des Pokémon de la réponse
        liste_names = [pokemon['name'] for pokemon in data['results']]
        print(liste_names)

        # ----------------------------------------------- #  
        # 4.2 : Tirer aléatoirement avec une proba uniforme
        # ----------------------------------------------- #  
        i = random.randint(0, len(liste_names))
        pokemon_choisi = liste_names[i]
        print("Le pokemon choisi est :")
        print(pokemon_choisi)


