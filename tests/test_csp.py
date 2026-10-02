"""Automated Test Suite for MnemoLib CSP Solver.

Mencakup pengujian unit:
- Kasus Normal (Happy Path)
- Propagasi Batasan AC-3
- Heuristik MRV (Minimum Remaining Values)
- Kasus Ekstrem (Edge Cases & Inconsistency)
- Kasus Batasan Kapasitas / Kuota
- Ablation Study (Kombinasi Heuristik & Propagasi)
"""

import pytest
from mnemolib.search.csp import (
    VARIABLES,
    ac3,
    check_assignment,
    check_pairwise_constraint,
    create_domains,
    select_unassigned_variable,
    solve,
)


# ==============================================================================
# 1. PENGUJIAN KASUS NORMAL (FUNCTIONAL TESTS)
# ==============================================================================


def test_normal_title_author_query():
    """Menguji kueri dengan informasi judul dan pengarang."""
    query = {
        "title_author": True,
        "context": False,
        "story": False,
        "filter": False,
    }
    solution = solve(query)
    assert solution is not None
    assert solution["X1"] == 1
    assert check_assignment(solution, query) is True


def test_normal_context_and_story_query():
    """Menguji kueri konteks dan cerita (memastikan dependensi X3 -> X2 terpenuhi)."""
    query = {
        "title_author": False,
        "context": True,
        "story": True,
        "filter": False,
    }
    solution = solve(query)
    assert solution is not None
    assert solution["X2"] == 1
    assert solution["X3"] == 1
    assert check_assignment(solution, query) is True


def test_normal_all_features_active():
    """Menguji kueri komprehensif di mana seluruh fitur pencarian diminta."""
    query = {
        "title_author": True,
        "context": True,
        "story": True,
        "filter": True,
    }
    solution = solve(query)
    assert solution is not None
    assert all(val == 1 for val in solution.values())
    assert check_assignment(solution, query) is True


def test_empty_query_activates_at_least_one_process():
    """C5: Jika pengguna tidak memilih fitur eksplisit, solver tetap mengaktifkan minimal 1 proses."""
    query = {
        "title_author": False,
        "context": False,
        "story": False,
        "filter": False,
    }
    solution = solve(query)
    assert solution is not None
    assert sum(solution.values()) >= 1


# ==============================================================================
# 2. PENGUJIAN AC-3 & MRV SPESIFIK
# ==============================================================================


def test_ac3_prunes_invalid_arc():
    """Menguji bahwa AC-3 memangkas domain X3 jika X2 dipaksa 0."""
    domains = create_domains()
    # Jika X2 dipaksa 0 (tidak ada konteks)
    domains["X2"] = {0}
    # Domain X3 awalnya {0, 1}
    assert 1 in domains["X3"]

    consistent = ac3(domains)
    assert consistent is True
    # Nilai 1 pada X3 harus terpangkas karena (X2=0, X3=1) melanggar batasan C6
    assert domains["X3"] == {0}


def test_ac3_detects_immediate_domain_wipeout():
    """AC-3 mengembalikan False bila salah satu domain menjadi kosong."""
    domains = create_domains()
    domains["X2"] = {0}
    domains["X3"] = {1}  # Inkonsisten mutlak dengan X2=0

    consistent = ac3(domains)
    assert consistent is False


def test_mrv_selects_smallest_remaining_domain():
    """Heuristik MRV harus memprioritaskan variabel dengan sisa domain terkecil."""
    domains = {
        "X1": {0, 1},
        "X2": {1},       # Domain ukuran 1
        "X3": {0, 1},
        "X4": {0, 1},
    }
    assignment = {}
    chosen = select_unassigned_variable(assignment, domains)
    assert chosen == "X2"


# ==============================================================================
# 3. PENGUJIAN KASUS EKSTREM (EDGE CASES)
# ==============================================================================


def test_edge_case_contradictory_story_without_context():
    """Edge Case: Kueri meminta elemen cerita (X3=1) namun melarang proses konteks (force_no_context)."""
    query = {
        "title_author": False,
        "context": False,
        "force_no_context": True,  # X2 dipaksa {0}
        "story": True,             # X3 dipaksa {1}
        "filter": False,
    }
    solution = solve(query)
    # Harus mengembalikan None (No Solution) karena kontradiksi C6
    assert solution is None


def test_edge_case_empty_initial_domain():
    """Edge Case: Deteksi dini saat domain awal sudah kosong / konflik mustahil."""
    query = {
        "title_author": True,
        "conflict_impossible": True,
    }
    solution = solve(query)
    assert solution is None


def test_edge_case_tight_quota_underflow():
    """Edge Case: Permintaan melebihi kuota sumber daya maksimum (Resource Constraint)."""
    query = {
        "title_author": True,
        "context": True,
        "story": True,
        "filter": True,
        "max_active_processes": 2,  # Padahal butuh 4 proses aktif
    }
    solution = solve(query)
    assert solution is None


def test_edge_case_valid_quota_boundary():
    """Edge Case: Batas tepat kuota sumber daya (Boundary Value Analysis)."""
    query = {
        "title_author": True,
        "context": True,
        "story": False,
        "filter": False,
        "max_active_processes": 2,  # Tepat 2 proses aktif
    }
    solution = solve(query)
    assert solution is not None
    assert sum(solution.values()) == 2
    assert solution["X1"] == 1
    assert solution["X2"] == 1


# ==============================================================================
# 4. PENGUJIAN ABLATION STUDY (PERBANDINGAN STRATEGI SOLVER)
# ==============================================================================


@pytest.mark.parametrize(
    "use_ac3,use_mrv",
    [
        (False, False),  # Pure Backtracking
        (False, True),   # Backtracking + MRV
        (True, False),   # Backtracking + AC-3
        (True, True),    # Full Solver: Backtracking + AC-3 + MRV
    ],
)
def test_all_solver_variants_find_consistent_solution(use_ac3, use_mrv):
    """Memastikan seluruh varian algoritma menghasilkan solusi legal yang konsisten."""
    query = {
        "title_author": True,
        "context": True,
        "story": True,
        "filter": False,
    }
    sol, stats = solve(query, use_ac3=use_ac3, use_mrv=use_mrv, return_stats=True)
    assert sol is not None
    assert check_assignment(sol, query) is True
    assert stats["nodes_visited"] >= 1


def test_stress_and_latency_performance():
    """Menguji kestabilan solver dalam 500 iterasi cepat (konvergensi stabil < 1 detik)."""
    import time
    start = time.perf_counter()
    for _ in range(500):
        sol = solve({"title_author": True, "context": True, "story": True})
        assert sol is not None
    duration = time.perf_counter() - start
    assert duration < 1.0  # Konvergensi super cepat
