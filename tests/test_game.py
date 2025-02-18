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


    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # check is not an empty string
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched


    def test_is_invalid_if_alternate_character(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'S2NDWICH'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False


    def test_is_valid_if_no_alternate_character(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'KWAKE'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True


    def test_is_invalid_if_excess_characters(self):
        # setup (example has 2 'G' - Input has 3 'G')
        new_game = Game()
        test_grid = 'AOGREEATGSA'
        test_word = 'AGGREGATE'
        # exercise
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False

