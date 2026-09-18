from mnemolib.search.ucs import Graph

# Graf alur keputusan MnemoLib berbobot latensi milidetik (ms)
MNEMOLIB_SEARCH_GRAPH: Graph = {
    "start": [("query_received", 5)],
    "query_received": [
        ("identify_title_author", 20),
        ("extract_context", 45),
        ("apply_filters", 15),
    ],
    "identify_title_author": [
        ("catalog_lookup", 30),
    ],
    "extract_context": [
        ("identify_story_elements", 20),
    ],
    "identify_story_elements": [
        ("catalog_lookup", 50),
    ],
    "apply_filters": [
        ("catalog_lookup", 40),
    ],
    "catalog_lookup": [
        ("results_presented", 10),
    ],
    "results_presented": [],
}