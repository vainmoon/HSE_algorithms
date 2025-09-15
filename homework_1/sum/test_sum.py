import pytest
from sum import get_max_even_sum


@pytest.mark.parametrize(
    "array, max_even_sum",
    [
        ([5, 7, 13, 2, 14], 36),
        ([3], 0),
        ([2], 2),
        ([1, 2], 2),
        ([1, 3, 5, 7], 16),
        ([2, 4, 6, 8], 20),
    ],
)
def test_get_max_even_sum(array, max_even_sum):
    assert get_max_even_sum([5, 7, 13, 2, 14]) == 36
    assert get_max_even_sum([3]) == 0
    assert get_max_even_sum([3]) == 0


def test_empty_array():
    with pytest.raises(ValueError):
        get_max_even_sum([])
