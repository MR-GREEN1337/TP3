'''
File: pokemon.py
Created Date: Wed Sep 14 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
Ce fichier contient la définition de la classe Pokemon
'''

import requests
import random
import json 

from .classes_combat import Move
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.image import imread

class Pokemon():
    """
    Class for a specific pokemon
    """
    # ------------------------------------------------------------------------ #
    # 2.1 : Faire la méthode init
    # ------------------------------------------------------------------------ #
    def __init__(self, name, base_url="https://pokeapi.co/api/v2/") -> None:
        """
        Initialization function

        @input name :           Name of the pokemon to generate
        @input base_url :       URL where to find all data (not specific to the list of pokemons)
        """
        # Initialize comparaison attribute
        self.comparison_attribute = None

        #Collect data
        self.pokemon = name
        self.base_url = base_url

        self.url_pokemon = base_url + "pokemon/" + name
        json_dump = requests.get(self.url_pokemon, stream=True)
        json_dump = json_dump.json()
        #Extract id
        self.id = json_dump["id"]
        #Extract height
        self.height = json_dump["height"]
        #Extract weight
        self.weight = json_dump["weight"]

        #Call methods
        self.get_color()


    # ------------------------------------------------------------------------ #
    # 2.2 : Faire la méthode __str__
    # ------------------------------------------------------------------------ #
    def __str__(self) -> str:
        return f"Name: {self.pokemon}\nWeight: {self.weight} kg\nHeight: {self.height} m"

    # ------------------------------------------------------------------------ #
    # 2.3 : Faire la méthode get_color
    # ------------------------------------------------------------------------ #
    def get_color(self) -> None:
        json_dump = requests.get(self.url_pokemon, stream=True).json()
        couleur_url_url = json_dump["species"]["url"]
        couleur_url = requests.get(couleur_url_url).json()
        couleur = couleur_url["color"]["name"]
        self.color= couleur
        print(f"Le pokémon {self.pokemon} est de couleur {self.color}")
    # ------------------------------------------------------------------------ #
    # 2.4 : Faire la méthode plot_sprite
    # ------------------------------------------------------------------------ #
    def plot_sprite(self) -> None:
        json = requests.get(self.url_pokemon, stream=True).json()
        image_url = json["sprites"]["front_default"] # <- récupérer ici l'url de l'image à partir du dictionnaire
        response = requests.get(image_url, stream=True)
        img = imread(BytesIO(response.content))
        plt.figure()
        plt.imshow(img, aspect='auto')
        plt.xticks([], [])
        plt.yticks([], [])
        plt.show()


    # ------------------------------------------------------------------------ #
    # 2.5 : Faire les méthodes reset_comparison_attribute et 
    #       set_comparison_attribute
    # ------------------------------------------------------------------------ #

    def set_comparaison_attribute(self, attribute):
        self.comparison_attribute = attribute

    def reset_comparaison_attribute(self):
        self.comparison_attribute = None

    # Surcharge des opérateurs ==
    def __eq__(self, other):
        if self.comparison_attribute == None:
            raise AttributeError(
                "comparaison attribute does not exist !"
            )
        return getattr(self, self.comparison_attribute) == other
    
    # Surcharge des opérateurs >
    def __gt__(self, other):
        if self.comparison_attribute == None:
            raise AttributeError(
                "comparaison attribute does not exist !"
            )
        return getattr(self, self.comparison_attribute) > other

    # Surcharge des opérateurs <
    def __lt__(self, other):
        if self.comparison_attribute is None:
            raise AttributeError(
                "comparaison attribute does not exist ! "
        )
        return getattr(self, self.comparison_attribute) < other

    # Surcharge des opérateurs >=
    def __ge__(self, other):
        if self.comparison_attribute is None:
            raise AttributeError(
                "comparaison attribute does not exist !"
            )
#        return getattr(self, self.comparison_attribute) >= other
        return getattr(self, self.comparison_attribute) >= other

    # Surcharge des opérateurs <=
    def __le__(self, other):
        if self.comparison_attribute is None:
            raise AttributeError(
                "comparaison attribute does not exist !"
            )
        return getattr(self, self.comparison_attribute) <= other


    # A LAISSER, utile pour afficher le tableau de plusieurs pokémons
    def verify_attribute(self, attribute=None):
        if attribute == None:
            attribute = self.comparison_attribute

        if attribute is  None:
            raise AttributeError(
                f"No comparison attribute set"
            )
        else:
            if attribute not in self.__dict__.keys():
                raise AttributeError(
                    f"Attribute {attribute} does not exist !"
                )
    # ------------------------------------------------------------------------ #
    # 2.6 : Faire les méthodes pour surcharger les comparaisons
    # ------------------------------------------------------------------------ #

    # ------------------------------------------------------------------------ #
    # 4.3 : Infos nécéssaires pour les combats
    # ------------------------------------------------------------------------ #
    def get_stats(self) -> None:
        """
        Collect stats usefull for the fight
        """

        pass

    # ------------------------------------------------------------------------ #
    # 4.6 : Afficher la santé
    # ------------------------------------------------------------------------ #
    def choose_moves(self) -> None:
        """
        Select the 4 moves which the pokemon can use in battle
        """
        pass
    
    # ------------------------------------------------------------------------ #
    # 4.4 : Afficher la santé et la perdre au besoin
    # ------------------------------------------------------------------------ #
    def display_health(self):
        """
        Used to display the actual health level of the pokemon
        """
        pass
    
    def get_HP(self):
        pass
    
    def take_damage(self, HP):
        pass

    def get_def(self):
        pass
    
    def attackMove(self):
        """
        Select a move to use during the battle round

        @return :   Attacking power : move power * pokemon attack
        """
        #Move selection
        pass

