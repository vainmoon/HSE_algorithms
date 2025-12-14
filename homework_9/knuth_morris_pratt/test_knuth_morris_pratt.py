import pytest
from knuth_morris_pratt import knuth_morris_pratt


@pytest.mark.parametrize(
    "s, w, result",
    [
        ("hello world", "world", 6),
        ("abcdef", "gh", -1),
        ("abcdef", "abc", 0),
        ("abcdef", "def", 3),
        ("abc", "", 0),
        ("abc", "abcdef", -1),
        ("aaaaaa", "aaa", 0),
        ("abcabcabc", "abc", 0),
        ("Привет мир", "мир", 7),
    ],
)
def test_knuth_morris_pratt(s, w, result):
    assert knuth_morris_pratt(s, w) == result
