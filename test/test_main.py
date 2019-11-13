from unittest import TestCase

from src.project_main import Gameboard



class TestMain(TestCase):

    def test_gameboard_is_empty_on_initialization(self):
        gameboard = Gameboard()
