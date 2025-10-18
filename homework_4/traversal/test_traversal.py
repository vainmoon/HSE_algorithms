import pytest
import sys
import os
sys.path.append(os.getcwd())

from traversal.traversal import (
    preorder,
    postorder,
    inorder,
    reverse_preorder,
    reverse_postorder,
    reverse_inorder,
)
from BST import BST


@pytest.fixture
def sample_bst():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    return bst


def test_preorder(sample_bst):
    result = preorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [5, 3, 2, 4, 7, 6, 8]
    assert result_key == expected_key


def test_postorder(sample_bst):
    result = postorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [2, 4, 3, 6, 8, 7, 5]
    assert result_key == expected_key


def test_inorder(sample_bst):
    result = inorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [2, 3, 4, 5, 6, 7, 8]
    assert result_key == expected_key


def test_reverse_preorder(sample_bst):
    result = reverse_preorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [5, 7, 8, 6, 3, 4, 2]
    assert result_key == expected_key


def test_reverse_postorder(sample_bst):
    result = reverse_postorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [8, 6, 7, 4, 2, 3, 5]
    assert result_key == expected_key


def test_reverse_inorder(sample_bst):
    result = reverse_inorder(sample_bst.root)
    result_key = [node.key for node in result]
    expected_key = [8, 7, 6, 5, 4, 3, 2]
    assert result_key == expected_key
