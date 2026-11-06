import argparse
from ingest import main as ingest_main
from src.semantic_search import semantic_search

def main():
    parser = argparse.ArgumentParser(description="MnemoLib Milestone 3")
    parser.add_argument("--ingest", action="store_true", help="Bangun ulang index dari data/raw")
    parser.add_argument("--query", help="Jalankan pencarian")
    args = parser.parse_args()
    if args.ingest:
        ingest_main()
    elif args.query:
        result = semantic_search(args.query)
        print(result["status"], result["top_score"])
        for item in result["results"]:
            print(item["metadata"]["source"], item["hybrid_score"])
            print(item["text"][:500])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
