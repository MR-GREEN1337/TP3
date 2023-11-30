'''
File: gestion_combat.py
Created Date: Thu Sep 22 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 23 2022
Modified By: Ammar MBian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''
#import Pokemon
import random
import time
import requests

class FightManager():
    """
    Class used to manage the battle between two given (or random) pokemons
    """
    # ------------------------------------------------------------------------ #
    # 4.7 : Faire le constructeur
    # ------------------------------------------------------------------------ #
    def __init__(self, pok1 = None, pok2 = None, base_url = "https://pokeapi.co/api/v2/") -> None:
        """
        Initialization

        @input pok1 :           Player 1 pokemon (if None, random pokemon is selected) - default : None
        @input pok2 :           Player 2 pokemon (if None, random pokemon is selected) - default : None
        @input base_url :       URL where to find all data (not specific to the list of pokemons)
        """
        
        self.base_url = base_url

        self.pokemon1 = self.choose_random_pokemon()
        self.pokemon2 = self.choose_random_pokemon()

        
    def choose_random_pokemon(self):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000')  # L'API limite souvent à 1000 pour éviter des réponses trop grandes
        data = response.json()

        # Extraire les noms des Pokémon de la réponse
        liste_names = [pokemon['name'] for pokemon in data['results']]
        # ----------------------------------------------- #  
        # 4.2 : Tirer aléatoirement avec une proba uniforme
        # ----------------------------------------------- #  
        i = random.randint(0, len(liste_names))
        pokemon_choisi = liste_names[i]

        return pokemon_choisi

    # ------------------------------------------------------------------------ #
    # 4.8 : Formule de calcul de dégats
    # ------------------------------------------------------------------------ #
    def calculate_damage(self, attack, defense):
        """
        Simplified function for damage calculation

        @input attack :             Attacking power : attacking pokemon attack stat * move power
        @input defense :            Defensive pokemon defense stat

        @return :                   Damage points
        """
        total_damage = (3 * attack) / (50 * defense) + 2
        return total_damage
    


    # ------------------------------------------------------------------------ #
    # 4.9 : Gérer le combat
    # ------------------------------------------------------------------------ #
    def run_fight(self, latent_time = 2):

        print(f"Battle between {self.pokemon1} and {self.pokemon2}")

        while True:
            attack_power1 = self.pokemon1.attackMove()
            defense_stat2 = self.pokemon2.get_def()
            damage1 = self.calculate_damage(attack_power1, defense_stat2)
            self.pokemon2.take_damage(damage1)

            print(f"{self.pokemon1} attacks {self.pokemon2} with power {attack_power1}")
            print(f"{self.pokemon2}'s health: {self.pokemon2.get_HP()}")
            print()

            if self.pokemon2.get_HP() <= 0:
                print(f"{self.pokemon2} has fainted. {self.pokemon1} wins!")
                break

            time.sleep(latent_time)

            attack_power2 = self.pokemon2.attackMove()
            defense_stat1 = self.pokemon1.get_def()
            damage2 = self.calculate_damage(attack_power2, defense_stat1)
            self.pokemon1.take_damage(damage2)

            print(f"{self.pokemon2} attacks {self.pokemon1} with power {attack_power2}")
            print(f"{self.pokemon1}'s health: {self.pokemon1.get_HP()}")
            print()

            if self.pokemon1.get_HP() <= 0:
                print(f"{self.pokemon1} has fainted. {self.pokemon2} wins!")
                break

            time.sleep(latent_time)