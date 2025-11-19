import pytest
from iterative import merge_sort, quick_sort


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [3, 2, 1],
        [5, 3, 8, 2, 1],
        list(range(100, 0, -1)),
        [7] * 50,
    ],
)
def test_correctness(arr):
    assert merge_sort(arr.copy()) == sorted(arr)
    assert quick_sort(arr.copy()) == sorted(arr)
