from unittest import TestCase
from src.linkedList import LinkedList
from src.node import Node


class TestLinkedList(TestCase):

    def test_list_initializes_as_empty(self):
        ll = LinkedList()
        self.assertFalse(ll.get_head())

    def test_append_node_to_linked_list(self):
        ll = LinkedList()
        node = Node(5)
        ll.append(node)
        self.assertTrue(ll.get_head() == node)
        self.assertFalse(ll.get_head().next)
