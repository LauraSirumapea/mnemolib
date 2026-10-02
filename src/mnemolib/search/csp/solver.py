"""CSP solver for MnemoLib using AC-3, MRV, and backtracking.

Modul ini mendukung pencarian solusi batasan dengan:
- Propagasi konsistensi busur (AC-3)
- Heuristik Minimum Remaining Values (MRV)
- Backtracking Search dengan pemangkasan dini (early pruning)
- Pengumpulan metrik performa (node assignments, backtracks, latency) untuk analisis sensitivitas.
"""

import time
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .ac3 import ac3
from .constraints import (
    apply_query_constraints,
    check_assignment,
    create_domains,
)
from .mrv import select_unassigned_variable


def check_partial_assignment(
    assignment: Dict[str, int],
    query_features: Dict[str, Any],
) -> bool:
    """Memeriksa apakah penugasan parsial konsisten dengan batasan MnemoLib."""

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

    # C6: Dependensi alur - X3 = 1 mensyaratkan X2 = 1
    if assignment.get("X3") == 1:
        if "X2" in assignment and assignment["X2"] != 1:
            return False

    if assignment.get("X2") == 0:
        if "X3" in assignment and assignment["X3"] == 1:
            return False

    # Batasan kuota maksimum proses jika dispesifikasikan
    max_active = query_features.get("max_active_processes")
    if max_active is not None:
        if sum(assignment.values()) > max_active:
            return False

    return True


def copy_domains(domains: Dict[str, Set[int]]) -> Dict[str, Set[int]]:
    """Membuat salinan independen dari domain untuk menjaga integritas percabangan."""
    return {variable: set(values) for variable, values in domains.items()}


def backtracking_search(
    assignment: Dict[str, int],
    domains: Dict[str, Set[int]],
    query_features: Dict[str, Any],
    use_ac3: bool = True,
    use_mrv: bool = True,
    stats: Optional[Dict[str, int]] = None,
) -> Optional[Dict[str, int]]:
    """Menyelesaikan CSP menggunakan backtracking dengan konfigurasi AC-3 & MRV."""
    if stats is not None:
        stats["nodes_visited"] += 1

    # Kasus Dasar: Seluruh variabel telah terisi
    if len(assignment) == len(domains):
        if check_assignment(assignment, query_features):
            return assignment.copy()
        if stats is not None:
            stats["backtracks"] += 1
        return None

    # Pemilihan variabel: MRV atau urutan deterministik
    if use_mrv:
        variable = select_unassigned_variable(assignment, domains)
    else:
        unassigned = [v for v in domains if v not in assignment]
        variable = unassigned[0] if unassigned else None

    if variable is None:
        return None

    # Urutkan nilai domain untuk keteraturan eksplorasi
    for value in sorted(domains[variable]):
        new_assignment = assignment.copy()
        new_assignment[variable] = value

        # Pengecekan konsistensi parsial
        if not check_partial_assignment(new_assignment, query_features):
            if stats is not None:
                stats["backtracks"] += 1
            continue

        new_domains = copy_domains(domains)
        new_domains[variable] = {value}

        # Propagasi AC-3 pada cabang pencarian jika diaktifkan
        if use_ac3:
            if not ac3(new_domains):
                if stats is not None:
                    stats["backtracks"] += 1
                continue

        result = backtracking_search(
            new_assignment,
            new_domains,
            query_features,
            use_ac3=use_ac3,
            use_mrv=use_mrv,
            stats=stats,
        )

        if result is not None:
            return result

    if stats is not None:
        stats["backtracks"] += 1
    return None


def solve(
    query_features: Dict[str, Any],
    use_ac3: bool = True,
    use_mrv: bool = True,
    return_stats: bool = False,
) -> Union[Optional[Dict[str, int]], Tuple[Optional[Dict[str, int]], Dict[str, Any]]]:
    """Menyelesaikan CSP MnemoLib dengan opsi analisis performa.

    Args:
        query_features: Dictionary representasi fitur input kueri pengguna.
        use_ac3: Mengaktifkan propagasi AC-3 sebelum dan selama pencarian.
        use_mrv: Mengaktifkan heuristik Minimum Remaining Values.
        return_stats: Jika True, mengembalikan tuple (solusi, statistik_eksekusi).

    Returns:
        Assignment dictionary jika solusi ditemukan, atau None jika tidak ada solusi.
    """
    start_time = time.perf_counter()
    stats: Dict[str, Any] = {
        "nodes_visited": 0,
        "backtracks": 0,
        "time_ms": 0.0,
    }

    # Tahap 1: Inisialisasi domain
    domains = create_domains()

    # Tahap 2: Terapkan batasan uniter dari kueri
    apply_query_constraints(domains, query_features)

    # Tahap 3: Propagasi AC-3 awal (Pre-search domain reduction)
    if use_ac3:
        if not ac3(domains):
            elapsed = (time.perf_counter() - start_time) * 1000.0
            stats["time_ms"] = elapsed
            return (None, stats) if return_stats else None

    # Tahap 4: Backtracking search
    solution = backtracking_search(
        assignment={},
        domains=domains,
        query_features=query_features,
        use_ac3=use_ac3,
        use_mrv=use_mrv,
        stats=stats,
    )

    elapsed = (time.perf_counter() - start_time) * 1000.0
    stats["time_ms"] = elapsed

    if return_stats:
        return solution, stats
    return solution