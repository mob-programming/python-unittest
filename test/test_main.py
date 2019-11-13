from unittest import TestCase

from src.project_main import GameBoard


class TestMain(TestCase):

    def test_game_board_is_empty_on_initialization(self):
        game_board = GameBoard()
        actual = game_board.get_number_of_cells()
        expect = 0
        self.assertEqual(expect, actual)