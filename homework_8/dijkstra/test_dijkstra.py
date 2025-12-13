from dijkstra import dijkstra


def test_single_vertex():
    graph = {"A": {}}
    assert dijkstra(graph, "A") == {"A": 0}


def test_simple_graph():
    graph = {"A": {"B": 1, "C": 4}, "B": {"C": 2}, "C": {}}
    assert dijkstra(graph, "A") == {"A": 0, "B": 1, "C": 3}


def test_medium_graph():
    graph = {
        "A": {"B": 7, "C": 9, "F": 14},
        "B": {"C": 10, "D": 15},
        "C": {"D": 11, "F": 2},
        "D": {"E": 6},
        "E": {"F": 9},
        "F": {},
    }

    distances = dijkstra(graph, "A")

    assert distances == {"A": 0, "B": 7, "C": 9, "D": 20, "E": 26, "F": 11}


def test_disconnected_graph():
    graph = {"A": {"B": 3}, "B": {}, "C": {"D": 1}, "D": {}}
    res = dijkstra(graph, "A")
    assert res["A"] == 0
    assert res["B"] == 3
    assert res["C"] == float("inf")
    assert res["D"] == float("inf")
