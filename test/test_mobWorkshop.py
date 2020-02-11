from unittest import TestCase
from src.main import Mob as Mob

"""
# February Mob Programming Challenge

You are given an integer matrix representing a plot of land, where the value at 
that location represents the height above sea level.

- A value of zero indicates water.
- A pond is a region of water connected vertically, horizontally or diagonally.
- The size of the pond is the total number of connected water cells..

Write a program that computes the sizes of all ponds in the matrix.

## Example

Input:

0 2 1 0
0 1 0 1
1 1 0 1
0 1 0 1

Output:
2, 4, 1 (in any order)
"""


class TestMob(TestCase):

    def test_mob_can_make_a_test_pass(self):
        mob = Mob()
        self.assertTrue(
            mob.can_make_this_test_pass(),
            "Do the smallest thing to make this pass."
        )
