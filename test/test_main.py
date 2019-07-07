from unittest import TestCase

from src.project_main import ProjectMain


class TestMain(TestCase):

    def test_get_fizz_from_six(self) -> None:
        #given
        current_integer = 6
        #when
        result = ProjectMain.process_integer(current_integer)
        #expect
        self.assertEqual("Fizz", result)

    def test_get_buzz_from_five(self) -> None:
        #given
        current_integer = 5

        # when
        result = ProjectMain.process_integer(current_integer)

        # expect
        self.assertEqual("Buzz", result)

    def test_get_fizz_buzz_from_fifteen(self) -> None:
        #given
        current_integer = 15

        # when
        result = ProjectMain.process_integer(current_integer)

        # expect
        self.assertEqual("FizzBuzz", result)

    def test_get_int_from_seven(self) -> None:
        #given
        current_integer = 7

        # when
        result = ProjectMain.process_integer(current_integer)

        # expect
        self.assertEqual(current_integer, result)


    def test_print_1_100(self):

     for x in range(1,101):
        print(ProjectMain.process_integer(x))
