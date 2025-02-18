"""
This module contains the Game class for a word validation game.

The Game class allows you to generate a randomised grid of 9 uppercase letters
and validate whether an input word can be formed.

Test validation is in tests/test_game.py
"""

import random
import string
import requests

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        # Leverages 'random' and 'string' to provide the randomised uppercase letter.
        self.grid = [random.choice(string.ascii_uppercase) for letter in range(9)]


    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid

        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']

game = Game()
print(game.grid) # --> OQUWRBAZE
MY_WORD = "BAROQUE"
game.is_valid(MY_WORD) # --> True
