def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node)
    return result


def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node)
        inorder(node.right, result)
    return result


def reverse_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node)
        reverse_preorder(node.right, result)
        reverse_preorder(node.left, result)
    return result


def reverse_postorder(node, result=None):
    if result is None:
        result = []
    if node:
        reverse_postorder(node.right, result)
        reverse_postorder(node.left, result)
        result.append(node)
    return result


def reverse_inorder(node, result=None):
    if result is None:
        result = []
    if node:
        reverse_inorder(node.right, result)
        result.append(node)
        reverse_inorder(node.left, result)
    return result
