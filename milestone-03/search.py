import argparse
from src.semantic_search import semantic_search

def main():
    parser = argparse.ArgumentParser(description="MnemoLib semantic + hybrid search")
    parser.add_argument("query", help="Pertanyaan atau potongan ingatan")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--threshold", type=float, default=0.30)
    args = parser.parse_args()
    result = semantic_search(args.query, args.top_k, args.threshold)
    print(f"\nQuery: {result['query']}")
    print(f"Status: {result['status']} | top-1 semantic similarity: {result['top_score']:.4f}")
    for index, hit in enumerate(result["results"], start=1):
        print(f"\n{index}. [hybrid={hit['hybrid_score']:.4f} | semantic={hit['similarity']:.4f} | lexical={hit['lexical_score']:.2f} | title={hit['title_score']:.2f}] {hit['metadata']['source']}")
        print(hit["text"][:650].replace("\n", " ") + ("..." if len(hit["text"]) > 650 else ""))

if __name__ == "__main__":
    main()
