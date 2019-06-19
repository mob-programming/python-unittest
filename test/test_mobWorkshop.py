from unittest import TestCase
from src.main import MobWorkshop as Mob
from src.node import Node
from src.linkedList import LinkedList

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
#   -
#   - ensure that the list is self-sorting by alphanumeric order (by ASCII value)
#   -


class TestMobWorkshop(TestCase):
    def test_mob_can_make_a_test_pass(self):
        mob = Mob()
        self.assertTrue(mob.pass_initial_test(), "Do the smallest thing to make this pass.")


class TestNode(TestCase):
    def test_node_initializes_with_data(self):
        expected = 'A'
        node = Node(expected)
        actual = node.get_data()
        self.assertEqual(expected, actual)

        expected = 'B'
        node = Node(expected)
        actual = node.get_data()
        self.assertEqual(expected, actual)


class TestLinkedList(TestCase):
    def test_list_initializes_as_empty(self):
        ll = LinkedList()
        is_empty = ll.is_empty()
        self.assertTrue(is_empty)

    # def test_get_node_by_index(self):
    #     ll = LinkedList()
    #     node = Node(5)
    #     ll.append(node)

    def test_list_appends_node_to_list(self):
        ll = LinkedList()
        node = Node(5)
        ll.append(node)
        self.assertEqual(ll.head.next, None)
        node_2 = Node(7)
        ll.append(node_2)
        self.assertEqual(ll.head, node)
        self.assertEqual(ll.head.next, node_2)
        self.assertEqual(ll.head.next.next, None)
        node_3 = Node(3)
        ll.append(node_3)
        self.assertEqual(ll.head.next.next, node_3)
