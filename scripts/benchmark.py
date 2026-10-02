"""Benchmark & Sensitivity Analysis Script for MnemoLib CSP Solver."""

import os
import sys
import time

# Ensure src is in python path
sys.path.insert(0, os.path.abspath("src"))

from mnemolib.search.csp import solve

def run_benchmark():
    print("=" * 105)
    print(" MNEMOLIB CSP SOLVER EMPIRICAL BENCHMARK & SENSITIVITY PROFILING")
    print("=" * 105)

    test_cases = [
        ("Normal Unary (Title Only)", {"title_author": True, "context": False, "story": False, "filter": False}),
        ("Normal Dependent (Context+Story)", {"title_author": False, "context": True, "story": True, "filter": False}),
        ("Normal Full (All Features)", {"title_author": True, "context": True, "story": True, "filter": True}),
        ("Edge Case: Conflict (Story No Context)", {"title_author": False, "context": False, "force_no_context": True, "story": True, "filter": False}),
        ("Edge Case: Tight Quota (Max 2)", {"title_author": True, "context": True, "story": False, "filter": False, "max_active_processes": 2}),
    ]

    algorithms = [
        ("Pure Backtracking", False, False),
        ("Backtracking + MRV", False, True),
        ("Backtracking + AC-3", True, False),
        ("Backtracking + AC-3 + MRV", True, True),
    ]

    print(f"{'Skenario Masalah':<35} | {'Strategi Algoritma':<26} | {'Nodes':<6} | {'Backtracks':<10} | {'Waktu Rata-rata':<15}")
    print("-" * 105)

    for case_name, q in test_cases:
        for algo_name, use_ac3, use_mrv in algorithms:
            iters = 1000
            start = time.perf_counter()
            sol, stats = None, None
            for _ in range(iters):
                sol, stats = solve(q, use_ac3=use_ac3, use_mrv=use_mrv, return_stats=True)
            elapsed_us = ((time.perf_counter() - start) / iters) * 1e6
            status = "FOUND" if sol is not None else "NO_SOL"
            print(f"{case_name:<35} | {algo_name:<26} | {stats['nodes_visited']:<6} | {stats['backtracks']:<10} | {elapsed_us:8.2f} us ({status})")
        print("-" * 105)

if __name__ == "__main__":
    run_benchmark()
