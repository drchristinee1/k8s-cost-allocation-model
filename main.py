import json
from k8s_allocation.loader import load_namespace_usage
from k8s_allocation.pricing import get_pricing
from k8s_allocation.allocator import allocate_k8s_costs


def main():
    print("=== Kubernetes Cost Allocation Model ===")

    input_file = "data/sample_namespace_usage.json"

    try:
        usage_data = load_namespace_usage(input_file)
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return

    pricing = get_pricing()
    result = allocate_k8s_costs(usage_data, pricing)

    print("\n=== Allocation Result ===\n")
    print(json.dumps(result, indent=4))

    output_file = "outputs/namespace_allocation_output.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"\nOutput saved to {output_file}")


if __name__ == "__main__":
    main()
