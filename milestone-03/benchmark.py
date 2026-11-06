from src.evaluation import run_benchmark, summarize_results

def main():
    result = run_benchmark()
    print(result.to_string(index=False))
    print("\nRINGKASAN EVALUASI")
    for key, value in summarize_results(result).items():
        print(f"{key}: {value}")
    print("\nCSV hasil: reports/evaluation_results.csv")

if __name__ == "__main__":
    main()
