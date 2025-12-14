import pytest
from rabin_karp import rabin_karp


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
def test_rabin_karp(s, w, result):
    assert rabin_karp(s, w) == result
