import pytest
from k_th import quickselect


def test_examples():
    assert quickselect([3, 2, 1, 5, 6, 4], 2) == 5
    assert quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_single():
    assert quickselect([10], 1) == 10


def test_duplicates():
    nums = [5, 5, 5, 5]
    assert quickselect(nums, 1) == 5
    assert quickselect(nums, 2) == 5
    assert quickselect(nums, 4) == 5


@pytest.mark.parametrize(
    "arr",
    [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 1, 2, 1, 2],
        [100, 1, 50, 30, 70],
    ],
)
def test_various(arr):
    for k in range(1, len(arr) + 1):
        expected = sorted(arr, reverse=True)[k - 1]
        assert quickselect(arr.copy(), k) == expected
