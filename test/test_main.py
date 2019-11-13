from unittest import TestCase

from src.project_main import GameBoard


class TestMain(TestCase):

    def test_game_board_is_empty_on_initialization(self):
        game_board = GameBoard()
        actual = game_board.get_number_of_cells()
        expect = 0
        self.assertEqual(expect, actual)

    def test_game_board_is_not_empty_on_initialization(self):
        game_board = GameBoard()
        game_board.add_cells((1,1))
        actual = game_board.get_number_of_cells()
        expect = 1
        self.assertEqual(expect, actual)