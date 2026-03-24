import pandas as pd
import math
import os

CHUNK_SIZE = 45_000


def split_csv_to_excel(input_csv, output_dir, chunk_size=10000):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Count total rows (optional but useful for progress)
    total_rows = sum(1 for _ in open(input_csv)) - 1  # minus header
    total_chunks = math.ceil(total_rows / chunk_size)

    print(f"Total rows: {total_rows}")
    print(f"Creating {total_chunks} Excel files...")

    # Read CSV in chunks
    reader = pd.read_csv(input_csv, chunksize=chunk_size, header=None)

    for i, chunk in enumerate(reader, start=1):
        output_path = os.path.join(output_dir, f"part_{i}.xlsx")
        chunk.to_excel(output_path, index=False, engine="openpyxl")
        print(f"Saved: {output_path}")

    print("Done!")


split_csv_to_excel(
    input_csv="large_input.csv", output_dir="output_excels", chunk_size=CHUNK_SIZE
)
