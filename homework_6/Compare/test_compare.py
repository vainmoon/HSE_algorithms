import pytest
from compare import merge_sort, quick_sort
import sys


def test_merge_sort_correct():
    arr = [5, 3, 8, 2, 1]
    assert merge_sort(arr) == sorted(arr)


def test_quick_sort_correct():
    arr = [5, 3, 8, 2, 1]
    assert quick_sort(arr) == sorted(arr)


sys.setrecursionlimit(100000)


def test_time_difference():
    arr = list(range(5000))

    arr1 = arr.copy()
    arr2 = arr.copy()

    merge_sort(arr1)
    quick_sort(arr2)

    merge_time = merge_sort.last_time
    quick_time = quick_sort.last_time

    print("\nMergeSort time:", merge_time)
    print("QuickSort time:", quick_time)

    assert quick_time > merge_time * 5


@pytest.mark.parametrize("data", [[], [1], [3, 2, 1], [10, 5, 2, 3, 1]])
def test_various_inputs(data):
    assert merge_sort(data.copy()) == sorted(data)
    assert quick_sort(data.copy()) == sorted(data)
