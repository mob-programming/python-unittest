from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_when_ProjectMain_is_made_get_greeting_returns_default_greeting(self) -> None:
        main = ProjectMain()
        expected = f'Hello user!'
        actual = main.get_greeting()
        self.assertEqual(expected, actual, 'Not the greeting I was expecting')
    def test_if_division(self):
        main = ProjectMain()
        expected = False
        actual = main.is_number('f')
        self.assertEqual(expected, actual, 'Not a number')

    def test_fizz_if_three(self):
        main = ProjectMain()
        expected = "Fizz"
        actual = main.fizzbuzz(3)
        self.assertEqual(expected, actual, 'Not fizz')

