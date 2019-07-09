from unittest import TestCase

from src.node import Node


class TestNode(TestCase):
    def test_node_initializes_with_data(self):
        expected = 'A'
        node = Node(expected)
        actual = node.get_data()
        self.assertEqual(expected, actual)
