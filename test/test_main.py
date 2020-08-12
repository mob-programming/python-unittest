from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_make_a_game(self) -> None:
        #Create a game of Life board
        # set (1,1) to be alive
        # dead next cycle

        main = ProjectMain()

        expected = f'Hello user!'
        actual = main.get_greeting()
        self.assertEqual(expected, actual, 'Not the greeting I was expecting')
