"""CSP solver for MnemoLib using AC-3, MRV, and backtracking."""

from .ac3 import ac3
from .constraints import (
    apply_query_constraints,
    check_assignment,
    create_domains,
)
from .mrv import select_unassigned_variable


def check_partial_assignment(assignment, query_features):
    """
    Check whether a partial assignment is still consistent
    with the MnemoLib CSP constraints.
    """

    # C1: title/author information
    if query_features.get("title_author", False):
        if "X1" in assignment and assignment["X1"] != 1:
            return False

    # C2: contextual information
    if query_features.get("context", False):
        if "X2" in assignment and assignment["X2"] != 1:
            return False

    # C3: story/case information
    if query_features.get("story", False):
        if "X3" in assignment and assignment["X3"] != 1:
            return False

    # C4: filter information
    if query_features.get("filter", False):
        if "X4" in assignment and assignment["X4"] != 1:
            return False

    # C6: X3 = 1 requires X2 = 1
    if assignment.get("X3") == 1:
        if "X2" in assignment and assignment["X2"] != 1:
            return False

    return True


def copy_domains(domains):
    """
    Create a deep-enough copy of CSP domains.

    Each domain is copied as a separate set so that
    backtracking does not modify the parent state.
    """

    return {
        variable: set(values)
        for variable, values in domains.items()
    }


def backtracking_search(assignment, domains, query_features):
    """
    Solve the CSP using backtracking with MRV.

    MRV is used to select the next variable.
    AC-3 is applied after assigning a value.
    """

    # Base case:
    # all variables have been assigned.
    if len(assignment) == len(domains):
        if check_assignment(assignment, query_features):
            return assignment.copy()

        return None

    # Select the next variable using MRV.
    variable = select_unassigned_variable(
        assignment,
        domains,
    )

    # Try values in a deterministic order.
    for value in sorted(domains[variable]):

        # Create a new partial assignment.
        new_assignment = assignment.copy()
        new_assignment[variable] = value

        # Check constraints that can already be evaluated.
        if not check_partial_assignment(
            new_assignment,
            query_features,
        ):
            continue

        # Create independent domains for this branch.
        new_domains = copy_domains(domains)

        # Assign the selected value to the variable.
        new_domains[variable] = {value}

        # Apply AC-3 after the assignment.
        if not ac3(new_domains):
            continue

        # Continue recursively.
        result = backtracking_search(
            new_assignment,
            new_domains,
            query_features,
        )

        if result is not None:
            return result

    # No valid assignment was found in this branch.
    return None


def solve(query_features):
    """
    Solve the MnemoLib CSP.

    Args:
        query_features: Dictionary indicating which
                        information exists in the user's query.

        Example:
        {
            "title_author": False,
            "context": True,
            "story": False,
            "filter": False,
        }

    Returns:
        A valid assignment dictionary if a solution exists.
        None if the CSP has no solution.
    """

    # Step 1:
    # Create the initial domain for all variables.
    domains = create_domains()

    # Step 2:
    # Apply constraints derived from the query.
    apply_query_constraints(
        domains,
        query_features,
    )
    

    # Step 3:
    # Run AC-3 before starting backtracking.
    if not ac3(domains):
        return None

    # Step 4:
    # Run MRV + backtracking.
    return backtracking_search(
        assignment={},
        domains=domains,
        query_features=query_features,
    )