from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_make_a_game(self) -> None:
        main = ProjectMain()

        expected = f'Hello user!'
        actual = main.get_greeting()
        self.assertEqual(expected, actual, 'Not the greeting I was expecting')
