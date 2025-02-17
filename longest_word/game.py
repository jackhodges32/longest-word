import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        # Leverages 'random' and 'string' to provide the randomised uppercase letter.
        self.grid = [random.choice(string.ascii_uppercase) for letter in range(9)]
        pass

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        word = my_word
        pass


game = Game()
print(game.grid) # --> OQUWRBAZE
my_word = "BAROQUE"
game.is_valid(my_word) # --> True
