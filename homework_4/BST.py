class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_rec(self.root, key, value)

    def _insert_rec(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_rec(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_rec(node.right, key, value)
