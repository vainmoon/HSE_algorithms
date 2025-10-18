import sys
import os
sys.path.append(os.getcwd())

from check_balance import check_balance
from BST import Node


def test_empty_tree():
    assert check_balance(None) is True


def test_single_node():
    root = Node(1)
    assert check_balance(root) is True


def test_two_nodes():
    root = Node(1)
    root.left = Node(2)
    assert check_balance(root) is True


def test_unbalanced_chain():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    assert check_balance(root) is False


def test_balanced_full_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    assert check_balance(root) is True


def test_unbalanced_deep_leaf():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    assert check_balance(root) is False


def test_balanced_with_asymmetric_structure():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    assert check_balance(root) is True
