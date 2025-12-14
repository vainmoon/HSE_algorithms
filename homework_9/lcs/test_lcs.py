import pytest
from lcs import get_lcs


@pytest.mark.parametrize(
    "string_1, string_2, lcs",
    [
        ("AGGTAB", "GXTXAYB", "GTAB"),
        ("", "", ""),
        ("abc", "", ""),
        ("", "abc", ""),
        ("abc", "DEF", ""),
        ("abcdef", "abcdef", "abcdef"),
        ("Привет", "ветка", "вет"),
    ],
)
def test_lcs_exact_match(string_1, string_2, lcs):
    assert get_lcs(string_1, string_2) == lcs
