class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return True

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            while self.head.next is not None:
                self.head.next = node

