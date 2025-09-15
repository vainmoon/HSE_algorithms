import pytest
from prime import count_prime


@pytest.mark.parametrize(
    "n, num_prime", [(10, 4), (1, 0), (2, 0), (3, 1), (5, 2), (11, 4), (100000, 9592)]
)
def test_count_prime(n, num_prime):
    assert count_prime(n) == num_prime


def test_non_positive_n():
    with pytest.raises(ValueError):
        count_prime(-1)
