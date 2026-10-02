"""MnemoLib: Sistem Katalog Perpustakaan Cerdas Berbasis Ingatan Pengguna.

Modul utama ini menyediakan antarmuka eksekusi terpadu (CLI) yang mendemonstrasikan
jalur inferensi optimal (Milestone 01: UCS) dan modul inferensi batasan (Milestone 02: CSP).
"""

from typing import Dict, Any
from mnemolib.search.mnemolib_graph import MNEMOLIB_SEARCH_GRAPH
from mnemolib.search.ucs import uniform_cost_search
from mnemolib.search.csp import solve, VARIABLE_NAMES


def main() -> None:
    """Titik masuk eksekusi terminal (CLI) MnemoLib."""
    print("=" * 70)
    print("  MnemoLib - Enterprise Intelligent Library Copilot")
    print("  Institut Teknologi Del - Program Studi Sarjana Sistem Informasi")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1. DEMONSTRASI MILESTONE 01: UCS PATH SEARCH
    # -------------------------------------------------------------
    print("\n[+] [MILESTONE 01] Menjalankan Penelusuran Jalur Optimal (UCS)...")
    start_node = "start"
    goal_node = "results_presented"
    ucs_result = uniform_cost_search(MNEMOLIB_SEARCH_GRAPH, start_node, goal_node)

    if ucs_result is not None:
        path, cost = ucs_result
        print(f"    [V] Jalur Optimal Ditemukan (Latensi: {cost:.2f} ms):")
        print(f"        {' -> '.join(path)}")
    else:
        print("    [X] Tidak ada jalur yang ditemukan.")

    # -------------------------------------------------------------
    # 2. DEMONSTRASI MILESTONE 02: CSP DECISION SOLVER
    # -------------------------------------------------------------
    print("\n[+] [MILESTONE 02] Menjalankan Inferensi Batasan Keputusan (CSP Solver)...")
    sample_query: Dict[str, Any] = {
        "title_author": False,
        "context": True,
        "story": True,
        "filter": False,
    }
    print(f"    - Fitur Kueri Masukan: {sample_query}")
    print("    - Menjalankan AC-3 Arc Consistency & Backtracking MRV...")

    solution, stats = solve(sample_query, return_stats=True)

    if solution is not None:
        print("    [V] Penugasan Keputusan Legal Terverifikasi:")
        for var, val in sorted(solution.items()):
            status_desc = "AKTIF" if val == 1 else "NONAKTIF"
            print(f"        - {var} ({VARIABLE_NAMES.get(var, 'Unknown')}): {status_desc}")
        print(f"    - Statistik: {stats['nodes_visited']} nodes dievaluasi, {stats['backtracks']} backtrack, {stats['time_ms']:.3f} ms")
    else:
        print("    [X] Konflik Batasan: Tidak ada penugasan legal yang memenuhi aturan.")

    print("\n" + "=" * 70)
    print("  Eksekusi Berhasil Selesai.")
    print("=" * 70)


if __name__ == "__main__":
    main()
