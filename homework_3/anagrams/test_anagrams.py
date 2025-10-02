from anagrams import get_grouped_anagrams
import pytest


@pytest.mark.parametrize(
    "strs, grouped_anagrams",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (
            ["кот", "ток", "окт", "акт", "так", "кит", "тик", "собака"],
            [["собака"], ["кот", "ток", "окт"], ["акт", "так"], ["кит", "тик"]],
        ),
        ([""], [[""]]),
    ],
)
def test_grouped_anagrams(strs, grouped_anagrams):
    assert get_grouped_anagrams(strs).sort() == grouped_anagrams.sort()
