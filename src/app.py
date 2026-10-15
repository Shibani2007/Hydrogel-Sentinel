import argparse
import csv
from modules.pipeline import validate_rows, transform_rows

def run(input_path, output_path):
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
    valid = validate_rows(reader)
    transformed = transform_rows(valid)
    keys = transformed[0].keys() if transformed else []
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(transformed)
    print(f"Wrote {len(transformed)} rows to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COSSEN monitoring pipeline")
    parser.add_argument('--input', required=True, help='Path to input CSV')
    parser.add_argument('--output', required=True, help='Path to output CSV')
    args = parser.parse_args()
    run(args.input, args.output)
