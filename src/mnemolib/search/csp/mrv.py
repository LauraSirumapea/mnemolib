"""Minimum Remaining Values (MRV) heuristic for MnemoLib CSP."""



def select_unassigned_variable(assignment, domains):
    """
    Select an unassigned variable using the
    Minimum Remaining Values (MRV) heuristic.

    MRV selects the variable with the smallest
    remaining domain.
    """


    unassigned_variables = [
        variable
        for variable in domains
        if variable not in assignment
    ]

    if not unassigned_variables:
        return None

    return min(
        unassigned_variables,
        key=lambda variable: len(domains[variable]),
    )