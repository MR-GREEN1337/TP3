'''
File: 1_requetes_http.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Wed Oct 05 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
Essai de l'utilisation d'une requête HTTP sur la pokéAPI
'''

import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.image import imread

if __name__ == '__main__':
    
    # 1.1 : Requête basique pour obtenir une réponse sur le pokémon de son choix
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon = "ninetales"

    print("Données obtenues :")
    print("------------------")
    # Afficher ici le texte brut du JSON

    # 1.2 : Transformer la chaine de caractère JSON en dictionnaire
    print("Données sous forme de dictionnaire :")
    print("--------------------------------------")


    # 1.3 : Afficher l'image du pokémon choisi
    # print("Affichage de l'image du pokemon : " + pokemon)
    # image_url = "" # <- récupérer ici l'url de l'image à partir du dictionnaire
    # response = requests.get(image_url, stream=True)
    # img = imread(BytesIO(response.content))
    
    # plt.figure()
    # plt.imshow(img, aspect='auto')
    # plt.xticks([], [])
    # plt.yticks([], [])
    # plt.show()

    # 1.4 : Aller chercher la couleur du pokémon

    # print(f"Le pokémon {pokemon} est de couleur {couleur}")

    # ------------------------------------------------------------------------------------------------------------------------- #
    # Appeler le prof après avoir fini les tâches pour valider.
    # ------------------------------------------------------------------------------------------------------------------------- #
