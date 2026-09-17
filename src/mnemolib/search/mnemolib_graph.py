from mnemolib.search.ucs import Graph


MNEMOLIB_SEARCH_GRAPH: Graph = {
    "start": [("query_received", 1)],
    "query_received": [
        ("identify_title_author", 2),
        ("extract_context", 3),
        ("apply_filters", 2),
    ],
    "identify_title_author": [
        ("catalog_lookup", 2),
    ],
    "extract_context": [
        ("identify_story_elements", 2),
    ],
    "identify_story_elements": [
        ("catalog_lookup", 3),
    ],
    "apply_filters": [
        ("catalog_lookup", 3),
    ],
    "catalog_lookup": [
        ("results_presented", 2),
    ],
    "results_presented": [],
}