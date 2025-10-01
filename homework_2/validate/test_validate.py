from validate import validate
import pytest


@pytest.mark.parametrize(
    "pushed, popped, result",
    [
        ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
        ([1, 2, 3], [3, 1, 2], False),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ([1], [1], True),
        ([1, 2, 3], [2, 1, 3], True),
        ([1, 2, 3], [3, 2, 1], True),
        ([1, 2, 3], [1, 2, 3], True),
    ],
)
def test_validate_parametrized(pushed, popped, result):
    assert validate(pushed, popped) == result
