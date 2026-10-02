"""Constraints for the MnemoLib Constraint Satisfaction Problem (CSP).

Modul ini mendefinisikan variabel keputusan, domain nilai, batasan uniter (unary),
batasan biner (binary arcs untuk AC-3), serta evaluasi solusi lengkap/parsial.
"""

from typing import Any, Dict, Optional, Set, Tuple

# 1. Definisi Variabel Keputusan Formal (X)
VARIABLES: Tuple[str, ...] = (
    "X1",  # identify_title_author
    "X2",  # extract_context
    "X3",  # identify_story_elements
    "X4",  # apply_filters
)

VARIABLE_NAMES: Dict[str, str] = {
    "X1": "identify_title_author",
    "X2": "extract_context",
    "X3": "identify_story_elements",
    "X4": "apply_filters",
}

# 2. Domain Nilai (D)
# 0 = Jalur/proses tidak diaktifkan
# 1 = Jalur/proses diaktifkan
DOMAIN_VALUES: Set[int] = {0, 1}

# Fitur kueri pengguna yang memicu batasan uniter
QUERY_FEATURES: Tuple[str, ...] = (
    "title_author",
    "context",
    "story",
    "filter",
)


def create_domains() -> Dict[str, Set[int]]:
    """Membuat domain awal untuk setiap variabel keputusan CSP."""
    return {var: set(DOMAIN_VALUES) for var in VARIABLES}


def apply_query_constraints(
    domains: Dict[str, Set[int]],
    query_features: Dict[str, Any],
) -> Dict[str, Set[int]]:
    """Menerapkan batasan uniter (unary constraints) berdasarkan fitur kueri pengguna.

    Aturan Bisnis:
    - C1: Jika title/author teridentifikasi, X1 HARUS bernilai 1.
    - C2: Jika context teridentifikasi, X2 HARUS bernilai 1.
    - C3: Jika story/case teridentifikasi, X3 HARUS bernilai 1.
    - C4: Jika filter kategori/tahun diterapkan, X4 HARUS bernilai 1.
    - Batasan Eksplisit Larangan: Jika fitur diatur False secara eksplisit
      atau dilarang, domain dapat dipangkas ke {0} jika diminta.
    """
    feature_to_var = {
        "title_author": "X1",
        "context": "X2",
        "story": "X3",
        "filter": "X4",
    }

    for feature, var in feature_to_var.items():
        if query_features.get(feature) is True:
            domains[var] = {1}
        elif query_features.get(feature) is False and query_features.get(f"force_no_{feature}", False):
            # Batasan jika proses sengaja dilarang
            domains[var] = {0}

    # Kasus Ekstrem: Konflik langsung yang membuat domain kosong
    if query_features.get("conflict_impossible", False):
        domains["X1"] = set()  # Kosongkan untuk memicu kegagalan AC-3 / solver

    return domains


def check_pairwise_constraint(
    var_a: str,
    val_a: int,
    var_b: str,
    val_b: int,
) -> bool:
    """Memeriksa batasan biner (binary constraints) antar pasangan variabel untuk AC-3.

    Aturan Bisnis Kritis (Regulasi Dependensi):
    - C6: Proses identifikasi elemen cerita (X3=1) mensyaratkan ekstraksi konteks aktif (X2=1).
      Kombinasi terlarang: (X2=0, X3=1).
    - C7: Jika dispesifikasikan batasan mutual exclusion (misal mode eksklusif).
    """
    # Dependensi X3 -> X2
    if var_a == "X3" and var_b == "X2":
        if val_a == 1 and val_b == 0:
            return False

    if var_a == "X2" and var_b == "X3":
        if val_a == 0 and val_b == 1:
            return False

    return True


def check_assignment(
    assignment: Dict[str, int],
    query_features: Dict[str, Any],
) -> bool:
    """Memeriksa apakah penugasan lengkap (complete assignment) memenuhi seluruh batasan.

    Evaluasi:
    - C1..C4: Kesesuaian dengan kebutuhan kueri
    - C5: Setidaknya satu proses komputasi aktif (sum(X) >= 1)
    - C6: Dependensi alur X3=1 -> X2=1
    - C8: Batasan kapasitas kuota proses aktif maksimum (jika didefinisikan)
    """
    # Pastikan seluruh variabel telah terisi
    if len(assignment) < len(VARIABLES):
        return False

    # C1: title/author information
    if query_features.get("title_author", False):
        if assignment.get("X1") != 1:
            return False

    # C2: contextual information
    if query_features.get("context", False):
        if assignment.get("X2") != 1:
            return False

    # C3: story/case information
    if query_features.get("story", False):
        if assignment.get("X3") != 1:
            return False

    # C4: filter information
    if query_features.get("filter", False):
        if assignment.get("X4") != 1:
            return False

    # C5: Setidaknya satu modul harus aktif (sistem tidak boleh idle total)
    if sum(assignment.values()) < 1:
        return False

    # C6: X3 = 1 requires X2 = 1
    if assignment.get("X3") == 1:
        if assignment.get("X2") != 1:
            return False

    # C8: Batasan kapasitas kuota (Resource Quota Constraint) jika diberikan
    max_active = query_features.get("max_active_processes")
    if max_active is not None:
        if sum(assignment.values()) > max_active:
            return False

    min_active = query_features.get("min_active_processes")
    if min_active is not None:
        if sum(assignment.values()) < min_active:
            return False

    return True
