
import time
import pandas as pd

from .config import EVALUATION_DIR, REPORTS_DIR
from .semantic_search import semantic_search


def run_benchmark(query_file=None, output_file=None, top_k=5):
    query_file = query_file or EVALUATION_DIR / "test_queries.csv"
    output_file = output_file or REPORTS_DIR / "evaluation_results.csv"

    df = pd.read_csv(query_file).fillna("")

    required = {"query_id", "category", "query", "expected_doc"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"Kolom CSV wajib tidak ada: {sorted(missing)}"
        )

    rows = []

    for row in df.to_dict("records"):
        started = time.perf_counter()

        result = semantic_search(
            str(row["query"]),
            top_k=top_k
        )

        latency = (time.perf_counter() - started) * 1000
        hits = result["results"]

        expected = str(row["expected_doc"]).strip().lower()
        rank = 0

        if expected:
            for position, hit in enumerate(hits, start=1):
                source = hit["metadata"]["source"].strip().lower()

                if expected == source:
                    rank = position
                    break

        is_ood = (
            str(row["category"]).strip().lower()
            in {"ood", "out_of_domain"}
        )

        rejected = result["status"] == "OUT-OF-DOMAIN"

        rows.append({
            "query_id": row["query_id"],
            "category": row["category"],
            "query": row["query"],
            "top1_doc": (
                hits[0]["metadata"]["source"] if hits else ""
            ),
            "top1_hybrid_score": (
                hits[0]["hybrid_score"] if hits else 0.0
            ),
            "top1_semantic_score": (
                hits[0]["similarity"] if hits else 0.0
            ),
            "expected_doc": row["expected_doc"],
            "expected_rank": rank,
            "hit_at_5": int(1 <= rank <= 5),
            "rejected": int(rejected),
            "decision_correct": int(rejected == is_ood),
            "latency_ms": round(latency, 2),
        })

    output = pd.DataFrame(rows)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    output.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    return output


def summarize_results(results):
    summary = {
        "total_queries": int(len(results)),
        "mean_latency_ms": (
            round(float(results["latency_ms"].mean()), 2)
            if len(results) else 0.0
        ),
        "ood_decision_accuracy": (
            round(float(results["decision_correct"].mean()), 4)
            if len(results) else 0.0
        ),
    }

    judged = results[
        results["expected_doc"].astype(str).str.strip() != ""
    ]

    if len(judged):
        ranks = judged["expected_rank"].astype(int)

        summary.update({
            "judged_queries": int(len(judged)),
            "precision_at_1": round(
                float((ranks == 1).mean()), 4
            ),
            "precision_at_5": round(
                float(((ranks >= 1) & (ranks <= 5)).mean()), 4
            ),
            "recall_at_5": round(
                float(((ranks >= 1) & (ranks <= 5)).mean()), 4
            ),
            "mrr_at_5": round(
                float(
                    ranks.apply(
                        lambda r: 1 / r if 1 <= r <= 5 else 0
                    ).mean()
                ), 4
            ),
        })
    else:
        summary["retrieval_metrics"] = (
            "Belum dihitung: isi expected_doc "
            "dengan nama file target yang telah diverifikasi."
        )

    return summary
