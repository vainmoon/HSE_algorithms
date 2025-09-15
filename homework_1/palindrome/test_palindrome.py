import pytest
from palindrome import check_for_palindrome


@pytest.mark.parametrize(
    "num, is_palindrome", [(121, True), (31, False), (7, True), (123321, True)]
)
def test_check_for_palindrome(num, is_palindrome):
    assert check_for_palindrome(num) == is_palindrome


def test_not_integer_input():
    with pytest.raises(TypeError):
        check_for_palindrome(0.1)


def test_non_positive_input():
    with pytest.raises(ValueError):
        check_for_palindrome(-121)
