from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_fizz_if_three(self):
        main = ProjectMain()
        expected = "Fizz"
        actual = main.fizzbuzz(3)
        self.assertEqual(expected, actual, 'Not fizz')

    def test_buzz_if_five(self):
        main = ProjectMain()
        expected = "Buzz"
        actual = main.fizzbuzz(5)
        self.assertEqual(expected, actual, 'Not buzz')

    def test_if_fizzbuzz(self):
        main = ProjectMain()
        expected = "FizzBuzz"
        actual = main.fizzbuzz(15)
        self.assertEqual(expected, actual, 'Not fizzbuzz')

    def test_if_other(self):
        main = ProjectMain()
        expected = 1
        actual = main.fizzbuzz(expected)
        self.assertEqual(expected, actual, 'Not 1')

