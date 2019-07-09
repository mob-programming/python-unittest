from unittest import TestCase
from src.main import MobWorkshop as Mob

# Mob Programming Challenge
# -------------------------
#
# Implement a singly linked-list.
# See https://en.wikipedia.org/wiki/Linked_list
#
# As a programmer, I should be able to use the LinkedList class to:
#   - append a node to the end of the list
#   - push a node to the front of the list
#   - print the list, in order
#   - remove nodes by data value
#   - pop nodes off the end of the list and receive the value of the popped node
#   - get a reversed list
#   - get a list from an existing linked list with duplicates removed (a linked set)
#
# Stretch goals
# -------------
#   - return a sorted version of the list as an array
#   - ensure that the list is self-sorting by alphanumeric order (by ASCII value)
#
# Guidelines
# ----------
#   - use TDD to implement the solution
#   - think more about what makes good mobbing than racing to complete the solution


class TestMobWorkshop(TestCase):
    def test_mob_can_make_a_test_pass(self):
        mob = Mob()
        self.assertTrue(mob.pass_initial_test(), "Do the smallest thing to make this pass.")


