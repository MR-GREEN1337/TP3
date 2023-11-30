'''
File: classes_combat.py
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

# ------------------------------------------------------------------------ #
# 4.5 : Faire la classe Move
# ------------------------------------------------------------------------ #
class Move():
    """
    Specific class for move data stockage
    """

    def __init__(self, url) -> None:
        """
        Initialization function
        @input url : url of the move
        """
        response = requests.get(url)
        data = response.json()

        self.name = data.get('name', 'Unknown Move')
        self.power = data.get('power', 0)
    
    def getPower(self) -> int:
        return self.power
    
    def __str__(self) -> str:
        return f"Move: {self.name}, Power: {self.power}"

    def __eq__(self, moveB : object) -> bool:
        """
        Test the equality with another class Move
        """
        if isinstance(moveB, Move):
            return self.name == moveB.name and self.power == moveB.power
        return False
    
    def __eq__(self, moveB : str) -> bool:
        """
        Test the equality only with the name of the move
        """
        if isinstance(moveB, str):
            return self.name == moveB
        return False