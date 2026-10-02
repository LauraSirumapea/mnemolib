"""Constraint Satisfaction Problem (CSP) solver for MnemoLib."""

from .ac3 import ac3
from .constraints import (
    VARIABLES,
    VARIABLE_NAMES,
    DOMAIN_VALUES,
    QUERY_FEATURES,
    create_domains,
    apply_query_constraints,
    check_pairwise_constraint,
    check_assignment,
)
from .mrv import select_unassigned_variable
from .solver import solve, backtracking_search

__all__ = [
    "VARIABLES",
    "VARIABLE_NAMES",
    "DOMAIN_VALUES",
    "QUERY_FEATURES",
    "create_domains",
    "apply_query_constraints",
    "check_pairwise_constraint",
    "check_assignment",
    "ac3",
    "select_unassigned_variable",
    "solve",
    "backtracking_search",
]