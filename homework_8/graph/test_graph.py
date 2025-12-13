from graph import get_graph_components


def test_empty_graph():
    assert get_graph_components({}) == []


def test_single_vertex_no_edges():
    assert get_graph_components({"A": []}) == [["A"]]


def test_two_isolated_vertices():
    component_list = get_graph_components({"A": [], "B": []})
    assert sorted([sorted(c) for c in component_list]) == [["A"], ["B"]]


def test_simple_graph():
    graph = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B"],
    }
    component_list = get_graph_components(graph)
    assert sorted([sorted(c) for c in component_list]) == [["A", "B", "C"]]


def test_disconnected_graph():
    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
        "E": [],
    }
    component_list = get_graph_components(graph)
    assert sorted([sorted(c) for c in component_list]) == [
        ["A", "B"],
        ["C", "D"],
        ["E"],
    ]
