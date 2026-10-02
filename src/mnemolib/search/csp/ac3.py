"""AC-3 constraint propagation for the MnemoLib CSP."""

from collections import deque

from .constraints import check_pairwise_constraint


# Binary constraint arcs used by MnemoLib.
ARCS = (
    ("X2", "X3"),
    ("X3", "X2"),
)


def revise(domains, variable_a, variable_b):
    """
    Remove values from variable_a's domain that have
    no compatible value in variable_b's domain.

    Returns:
        True if the domain of variable_a was changed.
        False otherwise.
    """

    revised = False

    for value_a in domains[variable_a].copy():
        has_support = False

        for value_b in domains[variable_b]:
            if check_pairwise_constraint(
                variable_a,
                value_a,
                variable_b,
                value_b,
            ):
                has_support = True
                break

        if not has_support:
            domains[variable_a].remove(value_a)
            revised = True

    return revised


def ac3(domains, arcs=None):
    """
    Apply the AC-3 algorithm to the CSP domains.

    Args:
        domains: Dictionary containing the current domain
                 of every CSP variable.
        arcs: Binary constraint arcs to be processed.

    Returns:
        True if the CSP remains consistent.
        False if one of the domains becomes empty.
    """

    if arcs is None:
        arcs = ARCS

    queue = deque(arcs)

    while queue:
        variable_a, variable_b = queue.popleft()

        if revise(domains, variable_a, variable_b):

            # An empty domain means the CSP has no solution
            # under the current constraints.
            if not domains[variable_a]:
                return False

            # Re-check neighboring arcs after a domain change.
            for neighbor_a, neighbor_b in ARCS:
                if neighbor_b == variable_a and neighbor_a != variable_b:
                    queue.append((neighbor_a, neighbor_b))

    return True