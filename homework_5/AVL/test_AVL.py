from AVL import AVL


def check_balance(avl, node):
    if node is None:
        return True
    balance = avl._balance_factor(node)
    if balance < -1 or balance > 1:
        return False
    return check_balance(avl, node.left) and check_balance(avl, node.right)


def test_avl_insert_and_find():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        avl.insert(el)

    for el in elements:
        assert avl.find(el) is True

    assert avl.find(100) is False


def test_avl_balance():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        avl.insert(el)
    assert check_balance(avl, avl.root) is True


def test_avl_delete():
    avl = AVL()
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        avl.insert(el)

    avl.delete(20)
    assert avl.find(20) is False
    assert check_balance(avl, avl.root) is True
