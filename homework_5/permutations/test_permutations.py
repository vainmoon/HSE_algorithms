from permutations import get_permutations
import pytest


@pytest.mark.parametrize(
    "nums, result",
    [
        (
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ),
        ([0, 1], [[0, 1], [1, 0]]),
        (
            [1],
            [
                [1],
            ],
        ),
        (
            [],
            [
                [],
            ],
        ),
    ],
)
def test_permutations(nums, result):
    output = get_permutations(nums)
    assert set(map(tuple, output)) == set(map(tuple, result)) and len(output) == len(
        result
    )
