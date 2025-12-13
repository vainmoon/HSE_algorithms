from dag import dag


def test_empty_graph():
    assert dag({}) == []


def test_single_vertex():
    assert dag({"A": []}) == ["A"]


def test_single_cycle():
    graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
    result = dag(graph)
    assert result[0] == result[-1]


def test_cycle_with_tail():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
        "D": ["A"],
    }
    result = dag(graph)
    assert result[0] == result[-1]


def test_two_disconnected_cycles():
    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }
    result = dag(graph)
    assert result[0] == result[-1]


def test_no_cycle_simple():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": [],
    }
    result = dag(graph)

    assert result == ["A", "B", "C"]
