"""Constraints for the MnemoLib Constraint Satisfaction Problem (CSP)."""


# Decision variables
VARIABLES = (
    "X1",
    "X2",
    "X3",
    "X4",
)


# Variable meanings
VARIABLE_NAMES = {
    "X1": "identify_title_author",
    "X2": "extract_context",
    "X3": "identify_story_elements",
    "X4": "apply_filters",
}


# Possible values for every variable
# 0 = process is not used
# 1 = process is used
DOMAIN_VALUES = {0, 1}


# Query features used by the unary constraints
QUERY_FEATURES = (
    "title_author",
    "context",
    "story",
    "filter",
)


def create_domains():
    """Create the initial domain for every CSP variable."""

    return {
        variable: set(DOMAIN_VALUES)
        for variable in VARIABLES
    }


def apply_query_constraints(domains, query_features):
    """
    Apply constraints based on the information contained
    in the user's query.

    If a query contains a particular type of information,
    the corresponding process must be activated.
    """

    feature_to_variable = {
        "title_author": "X1",
        "context": "X2",
        "story": "X3",
        "filter": "X4",
    }

    for feature, variable in feature_to_variable.items():
        if query_features.get(feature, False):
            domains[variable] = {1}

    return domains


def check_pairwise_constraint(
    variable_a,
    value_a,
    variable_b,
    value_b,
):
    """
    Check binary constraints between CSP variables.

    C6:
    X3 = 1 requires X2 = 1.

    Therefore, the combination:
        X2 = 0 and X3 = 1
    is not allowed.
    """

    if variable_a == "X3" and variable_b == "X2":
        if value_a == 1 and value_b == 0:
            return False

    if variable_a == "X2" and variable_b == "X3":
        if value_a == 0 and value_b == 1:
            return False

    return True


def check_assignment(assignment, query_features):
    """
    Check whether a complete assignment satisfies
    all defined CSP constraints.
    """

    # C1: title/author information
    if query_features.get("title_author", False):
        if assignment.get("X1") != 1:
            return False

    # C2: contextual information
    if query_features.get("context", False):
        if assignment.get("X2") != 1:
            return False

    # C3: story/case information
    if query_features.get("story", False):
        if assignment.get("X3") != 1:
            return False

    # C4: filter information
    if query_features.get("filter", False):
        if assignment.get("X4") != 1:
            return False

    # C5: at least one process must be active
    if sum(assignment.values()) < 1:
        return False

    # C6: X3 requires X2
    if assignment.get("X3") == 1:
        if assignment.get("X2") != 1:
            return False

    return True