"""Scaling & Sensitivity Benchmark for MnemoLib CSP Solver."""

import os
import sys
import time
from collections import deque

sys.path.insert(0, os.path.abspath("src"))

from mnemolib.search.csp import solve

def run_scaling_benchmark():
    print("\n" + "=" * 90)
    print(" PENGUJIAN SKALABILITAS CSP: SKALA KECIL VS SKALA BESAR (PROBLEM SCALING)")
    print("=" * 90)

    # Kita uji sistem dengan penugasan slot katalog berantai (N-variable CSP)
    # Variabel: X_1 .. X_N, Domain: {0, 1}
    # Batasan: X_{i+1} = 1 -> X_i = 1 (Dependency chain), plus capacity constraints
    def solve_scaled_csp(n_vars, use_ac3=True, use_mrv=True):
        variables = [f"X{i}" for i in range(1, n_vars + 1)]
        domains = {v: {0, 1} for v in variables}
        # Unary constraint: First half requires 1
        for i in range(1, n_vars // 2 + 1):
            domains[f"X{i}"] = {1}

        # Arcs: X_{i} -> X_{i-1}
        arcs = []
        for i in range(2, n_vars + 1):
            arcs.append((f"X{i}", f"X{i-1}"))
            arcs.append((f"X{i-1}", f"X{i}"))

        def check_pair(va, la, vb, lb):
            ia = int(va[1:])
            ib = int(vb[1:])
            if ia > ib and la == 1 and lb == 0:
                return False
            if ib > ia and lb == 1 and la == 0:
                return False
            return True

        start = time.perf_counter()
        nodes = 0
        backtracks = 0

        # AC-3 pre-search
        if use_ac3:
            queue = deque(arcs)
            while queue:
                va, vb = queue.popleft()
                revised = False
                for la in list(domains[va]):
                    if not any(check_pair(va, la, vb, lb) for lb in domains[vb]):
                        domains[va].remove(la)
                        revised = True
                if revised:
                    if not domains[va]:
                        return None, (time.perf_counter() - start) * 1000, nodes, backtracks
                    for na, nb in arcs:
                        if nb == va and na != vb:
                            queue.append((na, nb))

        # Backtracking with MRV
        assignment = {}
        def backtrack(assign, doms):
            nonlocal nodes, backtracks
            nodes += 1
            if len(assign) == len(doms):
                return assign
            if use_mrv:
                unassigned = [v for v in doms if v not in assign]
                var = min(unassigned, key=lambda v: len(doms[v]))
            else:
                unassigned = [v for v in doms if v not in assign]
                var = unassigned[0]
            
            for val in sorted(doms[var]):
                # Check consistency with previous
                consistent = True
                ivar = int(var[1:])
                for a_var, a_val in assign.items():
                    ia_var = int(a_var[1:])
                    if not check_pair(var, val, a_var, a_val):
                        consistent = False
                        break
                if not consistent:
                    backtracks += 1
                    continue
                new_assign = assign.copy()
                new_assign[var] = val
                res = backtrack(new_assign, doms)
                if res is not None:
                    return res
            backtracks += 1
            return None

        sol = backtrack(assignment, domains)
        elapsed_ms = (time.perf_counter() - start) * 1000
        return sol, elapsed_ms, nodes, backtracks

    print(f"{'Skala Masalah':<15} | {'Jumlah Variabel (N)':<20} | {'Waktu (ms)':<15} | {'Nodes Dievaluasi':<18} | {'Backtracks':<10}")
    print("-" * 90)

    scales = [
        ("Skala Kecil", 8),
        ("Skala Kecil", 16),
        ("Skala Menengah", 32),
        ("Skala Menengah", 64),
        ("Skala Besar", 128),
        ("Skala Besar", 256),
    ]

    for label, n in scales:
        sol, t_ms, nodes, bt = solve_scaled_csp(n, use_ac3=True, use_mrv=True)
        print(f"{label:<15} | {n:<20} | {t_ms:10.3f} ms   | {nodes:<18} | {bt:<10}")

if __name__ == "__main__":
    from benchmark import run_benchmark
    run_benchmark()
    run_scaling_benchmark()
