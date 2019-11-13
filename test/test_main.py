from unittest import TestCase

from src.project_main import GameBoard


class TestMain(TestCase):

    def test_gameboard_is_empty_on_initialization(self):
        game_board = GameBoard()
        actual = game_board.get_number_of_cells()
        expect = 0