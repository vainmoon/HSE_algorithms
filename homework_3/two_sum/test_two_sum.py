import pytest
from two_sum import get_solution


@pytest.mark.parametrize(
    "arr, k, result",
    [
        ([1, 3, 4, 10], 7, (1, 2)),
        ([5, 5, 1, 4], 10, (0, 1)),
        ([1, 2, 3, 4, 5], 9, (3, 4)),
        ([2, 7, 11, 15], 9, (0, 1)),
        ([8, -2, 4], 6, (0, 1)),
    ],
)
def test_two_sum(arr, k, result):
    assert get_solution(arr, k) == result
