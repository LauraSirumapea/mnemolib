import pytest
from mnemolib.search.mnemolib_graph import MNEMOLIB_SEARCH_GRAPH
from mnemolib.search.ucs import uniform_cost_search


def test_ucs_finds_lowest_cost_path():
    result = uniform_cost_search(
        MNEMOLIB_SEARCH_GRAPH,
        "start",
        "results_presented",
    )

    assert result is not None

    path, total_cost = result

    assert path[0] == "start"
    assert path[-1] == "results_presented"
    # 5 + 20 + 30 + 10 = 65 ms
    assert total_cost == 65


def test_ucs_finds_context_path_when_title_unavailable():
    """Menguji jalur saat pengguna murni hanya mengingat cerita/konteks."""
    context_only_graph = {
        "start": [("query_received", 5)],
        "query_received": [("extract_context", 45)],
        "extract_context": [("identify_story_elements", 20)],
        "identify_story_elements": [("catalog_lookup", 50)],
        "catalog_lookup": [("results_presented", 10)],
        "results_presented": [],
    }

    result = uniform_cost_search(context_only_graph, "start", "results_presented")
    assert result is not None
    path, total_cost = result
    assert path == [
        "start",
        "query_received",
        "extract_context",
        "identify_story_elements",
        "catalog_lookup",
        "results_presented",
    ]
    # 5 + 45 + 20 + 50 + 10 = 130 ms
    assert total_cost == 130


def test_ucs_returns_none_when_goal_is_unreachable():
    graph = {
        "start": [("middle", 1)],
        "middle": [],
    }

    result = uniform_cost_search(
        graph,
        "start",
        "results_presented",
    )

    assert result is None


def test_ucs_rejects_negative_cost():
    graph = {
        "start": [("goal", -1)],
        "goal": [],
    }

    with pytest.raises(ValueError, match="UCS mensyaratkan bobot biaya bernilai non-negatif."):
        uniform_cost_search(graph, "start", "goal")


def test_ucs_handles_graph_with_cycles():
    cyclic_graph = {
        "start": [("A", 10)],
        "A": [("B", 10), ("start", 5)],
        "B": [("A", 10), ("goal", 15)],
        "goal": [],
    }

    result = uniform_cost_search(cyclic_graph, "start", "goal")
    assert result is not None
    path, total_cost = result
    assert path == ["start", "A", "B", "goal"]
    assert total_cost == 35