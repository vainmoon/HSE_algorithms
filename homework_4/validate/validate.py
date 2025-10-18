import sys
import os
sys.path.append(os.getcwd())

from traversal.traversal import inorder


def validate(root):
    if root is None:
        return True
    result = inorder(root)
    for i in range(1, len(result)):
        if result[i - 1].key > result[i].key:
            return False
    return True
