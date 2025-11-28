from k_th_minheap import find_kth_largest_no_heapq, find_kth_largest_with_heapq


def test_examples():
    nums = [3, 2, 1, 5, 6, 4]
    assert find_kth_largest_no_heapq(nums, 2) == 5
    assert find_kth_largest_with_heapq(nums, 2) == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert find_kth_largest_no_heapq(nums, 4) == 4
    assert find_kth_largest_with_heapq(nums, 4) == 4


def test_edge_cases():
    nums = [1]
    assert find_kth_largest_no_heapq(nums, 1) == 1
    assert find_kth_largest_with_heapq(nums, 1) == 1


def test_duplicates():
    nums = [5, 5, 5, 5, 5]
    assert find_kth_largest_no_heapq(nums, 3) == 5
    assert find_kth_largest_with_heapq(nums, 3) == 5
