from mnemolib.search.mnemolib_graph import (
    MNEMOLIB_SEARCH_GRAPH,
)
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
    assert total_cost == 7


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

    try:
        uniform_cost_search(graph, "start", "goal")
        assert False, "Expected ValueError for negative cost"
    except ValueError:
        pass