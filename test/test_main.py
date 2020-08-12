from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_make_a_game(self) -> None:
        #Create a game of Life board
        # set (1,1) to be alive
        # dead next cycle
        board = Board(3, 3)
        cellState = True
        self.assertEqual(cellState, False, 'Cell should be dead')
