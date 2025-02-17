from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):

        # Checks our setup
        new_game = Game()

        # Checks our exercise
        grid = new_game.grid

        # Verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

        # Teardown

    def valid_input(self, word):
        new_game = Game()

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False



#        # Checks is a string, using isinstance to verify data type
  #      assert isinstance(word, str)
 #       # Checks there is at least one characters input
   #     assert len(word) > 0
        # Checks each character in a letter is a string and uppercase
    #    for letter in word:
     #       assert letter.isalpha()
      #      assert letter.isupper()
