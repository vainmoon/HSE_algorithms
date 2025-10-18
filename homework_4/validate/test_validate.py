import pytest
from validate import validate
from BST import BST, Node


@pytest.mark.parametrize(
    "values", [[20, 10, 30, 5, 15, 25, 35], [50, 30, 70, 20, 40, 60, 80], [1, 0, 2]]
)
def test_validate_correct_bst(values):
    bst = BST()
    for v in values:
        bst.insert(v)
    assert validate(bst.root) is True


def test_validate_incorrect_bst():
    root = Node(10)
    root.left = Node(15)
    root.right = Node(5)
    assert validate(root) is False


def test_validate_empty_bst():
    assert validate(None) is True


def test_validate_single_node():
    root = Node(10)
    assert validate(root) is True


def test_validate_nested_violation():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(12)
    assert validate(root) is False


def test_validate_right_skewed_tree():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    assert validate(root) is True


def test_validate_left_skewed_tree():
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    assert validate(root) is True
