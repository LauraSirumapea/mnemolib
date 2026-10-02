"""Tests for the MnemoLib CSP solver."""

import unittest

from mnemolib.search.csp.ac3 import ac3
from mnemolib.search.csp.constraints import (
    apply_query_constraints,
    create_domains,
)
from mnemolib.search.csp.mrv import select_unassigned_variable
from mnemolib.search.csp.solver import solve


class TestCSP(unittest.TestCase):
    """Test cases for MnemoLib CSP."""

    def test_create_domains(self):
        """Every CSP variable should initially have domain {0, 1}."""

        domains = create_domains()

        self.assertEqual(
            domains,
            {
                "X1": {0, 1},
                "X2": {0, 1},
                "X3": {0, 1},
                "X4": {0, 1},
            },
        )

    def test_query_constraint(self):
        """A required query feature should force its variable to 1."""

        domains = create_domains()

        query_features = {
            "title_author": True,
            "context": False,
            "story": False,
            "filter": False,
        }

        apply_query_constraints(
            domains,
            query_features,
        )

        self.assertEqual(domains["X1"], {1})
        self.assertEqual(domains["X2"], {0, 1})
        self.assertEqual(domains["X3"], {0, 1})
        self.assertEqual(domains["X4"], {0, 1})

    def test_ac3_story_requires_context(self):
        """
        If X3 = 1, AC-3 should force X2 = 1
        because X3 requires X2.
        """

        domains = {
            "X1": {0, 1},
            "X2": {0, 1},
            "X3": {1},
            "X4": {0, 1},
        }

        result = ac3(domains)

        self.assertTrue(result)
        self.assertEqual(domains["X2"], {1})
        self.assertEqual(domains["X3"], {1})

    def test_mrv(self):
        """MRV should select the variable with the smallest domain."""

        domains = {
            "X1": {0, 1},
            "X2": {1},
            "X3": {0, 1},
            "X4": {0, 1},
        }

        assignment = {}

        variable = select_unassigned_variable(
            assignment,
            domains,
        )

        self.assertEqual(variable, "X2")

    def test_solver_context_query(self):
        """Context query should activate X2."""

        query_features = {
            "title_author": False,
            "context": True,
            "story": False,
            "filter": False,
        }

        solution = solve(query_features)

        self.assertIsNotNone(solution)
        self.assertEqual(solution["X2"], 1)

    def test_solver_story_query(self):
        """
        Story query should activate X3 and,
        through C6, also activate X2.
        """

        query_features = {
            "title_author": False,
            "context": False,
            "story": True,
            "filter": False,
        }

        solution = solve(query_features)

        self.assertIsNotNone(solution)
        self.assertEqual(solution["X3"], 1)
        self.assertEqual(solution["X2"], 1)

    def test_solver_all_features(self):
        """All query features should activate all processes."""

        query_features = {
            "title_author": True,
            "context": True,
            "story": True,
            "filter": True,
        }

        solution = solve(query_features)

        self.assertIsNotNone(solution)

        self.assertEqual(solution["X1"], 1)
        self.assertEqual(solution["X2"], 1)
        self.assertEqual(solution["X3"], 1)
        self.assertEqual(solution["X4"], 1)

    def test_solver_requires_at_least_one_process(self):
        """
        If no query feature is provided, the solver must still
        produce a solution satisfying C5.
        """

        query_features = {
            "title_author": False,
            "context": False,
            "story": False,
            "filter": False,
        }

        solution = solve(query_features)

        self.assertIsNotNone(solution)

        active_processes = sum(solution.values())

        self.assertGreaterEqual(active_processes, 1)


if __name__ == "__main__":
    unittest.main()