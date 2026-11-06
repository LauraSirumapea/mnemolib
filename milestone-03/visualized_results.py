
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Lokasi file
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "reports" / "evaluation_results.csv"
OUTPUT_DIR = BASE_DIR / "reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Baca hasil benchmark
df = pd.read_csv(CSV_FILE)

# Pisahkan data
judged = df[df["expected_doc"].fillna("").str.strip() != ""]
ood = df[df["category"].str.lower().isin(["ood", "out_of_domain"])]

ranks = judged["expected_rank"].astype(int)

# Hitung metrik
metrics = {
    "Precision@1": (ranks == 1).mean(),
    "Precision@5": ((ranks >= 1) & (ranks <= 5)).mean(),
    "Recall@5": ((ranks >= 1) & (ranks <= 5)).mean(),
    "MRR@5": ranks.apply(
        lambda r: 1 / r if 1 <= r <= 5 else 0
    ).mean(),
    "OOD Accuracy": df["decision_correct"].mean()
}

# Grafik 1: Metrik evaluasi
plt.figure(figsize=(10, 6))

bars = plt.bar(
    metrics.keys(),
    [value * 100 for value in metrics.values()]
)

plt.title("MnemoLib Milestone 3 - Evaluation Metrics")
plt.ylabel("Score (%)")
plt.ylim(0, 110)
plt.grid(axis="y", alpha=0.3)

for bar, value in zip(bars, metrics.values()):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{value * 100:.1f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "evaluation_metrics.png",
    dpi=300
)
plt.close()

# Grafik 2: Latensi setiap query
plt.figure(figsize=(11, 6))

plt.bar(
    df["query_id"],
    df["latency_ms"]
)

plt.title("MnemoLib Milestone 3 - Query Latency")
plt.xlabel("Query ID")
plt.ylabel("Latency (ms)")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "query_latency.png",
    dpi=300
)
plt.close()

print("Grafik berhasil dibuat!")
print("Lokasi:", OUTPUT_DIR)
print("1. evaluation_metrics.png")
print("2. query_latency.png")
print("\nMetrik evaluasi:")

for name, value in metrics.items():
    print(f"{name}: {value * 100:.2f}%")

print(
    f"\nMean latency: {df['latency_ms'].mean():.2f} ms"
)