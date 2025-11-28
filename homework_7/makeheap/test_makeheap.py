import random
from makeheap import makeheap_n_log_n, makeheap


def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] > arr[l]:
            return False
        if r < n and arr[i] > arr[r]:
            return False
    return True


def test_empty():
    a = []
    makeheap_n_log_n(a)
    assert is_min_heap(a)
    makeheap(a)
    assert is_min_heap(a)


def test_single():
    a = [5]
    makeheap_n_log_n(a)
    assert is_min_heap(a)
    a = [5]
    makeheap(a)
    assert is_min_heap(a)


def test_random_small():
    for _ in range(50):
        a = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        b = a.copy()
        makeheap_n_log_n(a)
        makeheap(b)
        assert is_min_heap(a)
        assert is_min_heap(b)
        assert sorted(a) == sorted(b)
