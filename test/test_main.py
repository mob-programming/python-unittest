from unittest import TestCase

from src.project_main import Board


class TestMain(TestCase):

    def test_make_a_game(self) -> None:
        # Create a game of Life board
        board = Board(3, 3)
        # set (1,1) to be alive
        board.set_alive(1, 1)
        # next cycle
        board.move()
        # cell now dead
        cell_state = board.get_state(1, 1)
        self.assertEqual(cell_state, False, 'Cell should be dead')
